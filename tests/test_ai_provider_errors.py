import os
from types import SimpleNamespace
from unittest import TestCase
from unittest.mock import Mock, patch

from agent_handler import StudyAssistantHandler
from study_agents import StudyAgents


class AuthenticationError(Exception):
    """Test double named after the provider authentication error."""


class RateLimitError(Exception):
    """Test double named after the provider rate-limit error."""


class APIConnectionError(Exception):
    """Test double named after the provider connection error."""


class NotFoundError(Exception):
    """Test double named after the provider model-not-found error."""


class StudyAgentsModelTests(TestCase):
    def make_agents(self, provider):
        return StudyAgents(
            topic="Python",
            subject_category="programming",
            knowledge_level="beginner",
            learning_goal="Learn the basics",
            time_available="3-5 hours per week",
            learning_style="visual",
            provider=provider,
        )

    def test_missing_groq_key_has_actionable_message(self):
        with patch.dict(os.environ, {"GROQ_API_KEY": ""}, clear=False):
            with self.assertRaisesRegex(ValueError, "GROQ_API_KEY is not configured"):
                self.make_agents("groq")._get_model()

    def test_missing_openai_key_has_actionable_message(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": ""}, clear=False):
            with self.assertRaisesRegex(ValueError, "OPENAI_API_KEY is not configured"):
                self.make_agents("openai")._get_model()

    def test_unsupported_provider_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unsupported AI provider"):
            self.make_agents("unknown-provider")._get_model()

    def test_valid_groq_key_creates_model(self):
        with patch.dict(os.environ, {"GROQ_API_KEY": "test-groq-key"}, clear=False):
            with patch("study_agents.Groq") as model_class:
                self.make_agents("groq")._get_model(temperature=0.2)

        model_class.assert_called_once_with(
            id="gpt-4o", temperature=0.2
        )

    def test_valid_openai_key_creates_model(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-openai-key"}, clear=False):
            with patch("study_agents.OpenAIChat") as model_class:
                self.make_agents("openai")._get_model(temperature=0.2)

        model_class.assert_called_once_with(
            id="gpt-4o", temperature=0.2
        )


class AgentRequestErrorTests(TestCase):
    def setUp(self):
        # The request helper does not need a fully initialized Streamlit handler.
        self.handler = StudyAssistantHandler.__new__(StudyAssistantHandler)

    def run_with_error(self, error):
        agent = Mock()
        agent.run.side_effect = error
        with patch("agent_handler.st.error") as show_error:
            result = self.handler._run_agent(agent, "test prompt")
        return result, show_error.call_args.args[0]

    def test_invalid_key_is_safe_and_does_not_expose_the_key(self):
        secret = "sk-this-must-not-be-displayed"
        result, message = self.run_with_error(
            AuthenticationError(f"Invalid key: {secret}")
        )

        self.assertIsNone(result)
        self.assertIn("credentials", message)
        self.assertNotIn(secret, message)

    def test_unexpected_value_error_does_not_expose_its_contents(self):
        secret = "sk-this-must-not-be-displayed"
        result, message = self.run_with_error(ValueError(secret))

        self.assertIsNone(result)
        self.assertIn("AI request failed", message)
        self.assertNotIn(secret, message)

    def test_rate_limit_error_is_actionable(self):
        result, message = self.run_with_error(RateLimitError("Too many requests"))

        self.assertIsNone(result)
        self.assertIn("rate limiting", message)

    def test_network_error_is_actionable(self):
        result, message = self.run_with_error(APIConnectionError("Connection failed"))

        self.assertIsNone(result)
        self.assertIn("internet connection", message)

    def test_model_not_found_error_is_actionable(self):
        error = NotFoundError("Model does not exist")
        error.status_code = 404
        result, message = self.run_with_error(error)

        self.assertIsNone(result)
        self.assertIn("model is unavailable", message)

    def test_empty_response_is_reported(self):
        agent = Mock()
        agent.run.return_value = SimpleNamespace(content="")

        with patch("agent_handler.st.error") as show_error:
            result = self.handler._run_agent(agent, "test prompt")

        self.assertIsNone(result)
        self.assertIn("empty response", show_error.call_args.args[0])

    def test_successful_request_returns_content(self):
        agent = Mock()
        agent.run.return_value = SimpleNamespace(content="Helpful response")

        with patch("agent_handler.st.error") as show_error:
            result = self.handler._run_agent(agent, "test prompt")

        self.assertEqual(result, "Helpful response")
        show_error.assert_not_called()
