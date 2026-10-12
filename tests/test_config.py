import pytest

from config import ConfigManager


@pytest.fixture
def config_manager():
    """Create a config manager using the real prompts file."""
    return ConfigManager()


def test_persona_configuration_loads(config_manager):
    persona = config_manager.get_persona("student_analyzer")

    assert persona
    assert "system_prompt" in persona


def test_prompt_template_formats_topic(config_manager):
    prompt = config_manager.format_prompt(
        "student_analysis",
        topic="Python",
        subject_category="programming",
        knowledge_level="beginner",
        learning_goal="learn basics",
        time_available="2 hours a week",
        learning_style="visual",
    )

    assert prompt is not None
    assert "Python" in prompt
    assert "beginner" in prompt


def test_unknown_prompt_returns_none(config_manager):
    assert config_manager.get_prompt("missing_prompt_type") is None


def test_prompt_formatting_reports_missing_variable(config_manager):
    with pytest.raises(KeyError):
        config_manager.format_prompt("student_analysis")
