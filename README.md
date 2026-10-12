# 📚 Multi-Agent AI Study Assistant

A powerful, personalized learning platform powered by multiple specialized AI agents. Get custom learning roadmaps, practice quizzes, AI tutoring, and RAG-powered document Q&A to supercharge your studies!

## 🚀 Live Demo

This project is designed to be deployed as a Streamlit app.

Live app URL:
https://your-app-name.streamlit.app

> Replace the placeholder URL with your actual deployed app URL after publishing to Streamlit Cloud.

## 📦 Push to GitHub

```bash
git init
git branch -M main
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/rohanbhati0912/Multi-Agent-Study-Assistant.git
git push -u origin main
```

## ☁️ Deploy to Streamlit Cloud

1. Push the project to GitHub.
2. Go to https://streamlit.io/cloud
3. Sign in with GitHub.
4. Select the repository and set the app file to `app.py`.
5. Add the required secrets in the deployment settings:
   - `GROQ_API_KEY`
   - `OPENAI_API_KEY`
6. Deploy the app.

This keeps the app publicly available with a stable URL while keeping your API keys secure.

## 🌟 Features

### 🎯 Personalized Learning Analysis
- **Student Profiling**: AI analyzes your knowledge level, goals, and learning style
- **Gap Analysis**: Identifies what you need to learn and prerequisite knowledge
- **Custom Recommendations**: Tailored approach based on your unique needs

### 🗺️ Smart Learning Roadmaps
- **Structured Learning Paths**: Break down complex topics into manageable phases
- **Time-Optimized**: Plans adapted to your available study time
- **Milestone Tracking**: Clear checkpoints to measure progress
- **Flexible Scheduling**: Adjust pace based on your schedule

### 📝 Dynamic Quiz Generation
- **Adaptive Difficulty**: Questions matched to your knowledge level
- **Multiple Question Types**: MCQ, True/False, Short Answer, Problem-Solving
- **Detailed Explanations**: Learn from both correct and incorrect answers
- **Custom Focus Areas**: Target specific topics you want to practice

### 🤖 AI Tutor
- **24/7 Availability**: Get help whenever you need it
- **Personalized Explanations**: Adapted to your learning style
- **Step-by-Step Guidance**: Break down complex concepts
- **Real-World Examples**: Understand through practical applications

### 📄 RAG-Powered Document Q&A
- **Upload Study Materials**: PDFs, textbooks, lecture notes
- **Intelligent Search**: Find relevant information instantly
- **Context-Aware Answers**: Get answers grounded in your materials
- **Source Citations**: Know where information comes from

### 🔍 Resource Finder
- **Curated Resources**: AI finds the best learning materials
- **Quality Filtered**: Only high-quality, relevant resources
- **Learning Style Matched**: Resources suited to how you learn best

## 🏗️ Architecture

This project uses a multi-agent architecture where specialized AI agents collaborate:

```
study_agents.py          # Specialized AI agents (Analyzer, roadmap Creator, Quiz Generator, Tutor, Resource Finder, RAG Tutor)
agent_handler.py         # Orchestrates agent workflows and manages state
rag_helper.py            # RAG functionality for document-based learning
config.py                # Configuration management
prompts.yaml             # Agent personas and prompt templates
app.py                   # Streamlit web interface
```
### Agent Roles

1. **Student Analyzer Agent**: Assesses learning needs, identifies gaps, recommends approaches
2. **Roadmap Creator Agent**: Designs personalized learning paths with phases and milestones
3. **Quiz Generator Agent**: Creates adaptive assessments with explanations
4. **Tutor Agent**: Provides explanations and answers questions
5. **Resource Finder Agent**: Searches and recommends learning materials
6. **RAG Tutor Agent**: Answers questions using uploaded study documents

## 🛠️ Technologies Used

- **Phidata**: Multi-agent orchestration framework
- **Streamlit**: Web interface
- **LangChain**: Document processing and RAG
- **ChromaDB**: Vector database for RAG
- **OpenAI/Groq**: LLM providers
- **DuckDuckGo**: Web search for resource finding

## 📝 Tips for Best Results

1. **Be Specific**: The more detailed your learning goals, the better the roadmap
2. **Honest Assessment**: Accurately rate your knowledge level for best recommendations
3. **Upload Materials**: Use the RAG feature with your textbooks and notes for personalized help
4. **Regular Quizzes**: Test yourself frequently to reinforce learning
5. **Follow the Roadmap**: Trust the AI's structured approach
6. **Ask Questions**: Use the tutor liberally - there are no dumb questions!

## 🎨 Learning Styles Explained

The AI adapts to your preferred learning style to maximize effectiveness. Choose the one that best describes how you learn:

### 👁️ Visual Learners
**How you learn best:** Through seeing and observing

**Characteristics:**
- Prefer diagrams, charts, and images
- Remember faces better than names
- Like color-coded notes and mind maps
- Benefit from watching demonstrations

**Recommended resources:**
- 📊 Infographics and flowcharts
- 🎥 Video tutorials and demonstrations
- 🗺️ Mind maps and concept diagrams
- 📈 Visual data representations
- 🎨 Color-coded study materials

**Study tips:**
- Use highlighters and color coding
- Draw diagrams to understand concepts
- Watch video explanations
- Create visual summaries

---

### 🎧 Auditory Learners
**How you learn best:** Through listening and speaking

**Characteristics:**
- Prefer verbal instructions
- Remember what you hear
- Enjoy discussions and lectures
- Often talk through problems

**Recommended resources:**
- 🎙️ Podcasts and audio lectures
- 💬 Discussion forums and study groups
- 🗣️ Verbal explanations and debates
- 🎵 Educational songs or mnemonics
- 📻 Audio books and recordings

**Study tips:**
- Read notes aloud
- Record and listen to lectures
- Discuss topics with others
- Use verbal repetition
- Explain concepts out loud

---

### 🤸 Kinesthetic Learners
**How you learn best:** Through doing and hands-on experience

**Characteristics:**
- Learn by doing and practicing
- Prefer physical activity and movement
- Like real-world applications
- Need to try things yourself

**Recommended resources:**
- 💻 Interactive coding platforms (for programming)
- 🔬 Lab experiments and simulations
- 🎮 Educational games and interactive tools
- 🛠️ Hands-on projects and exercises
- 🏃 Physical models and manipulatives

**Study tips:**
- Build projects while learning
- Use interactive simulations
- Take frequent breaks to move
- Practice with real examples
- Create physical models or demonstrations

---

### 📖 Reading/Writing Learners
**How you learn best:** Through reading and writing

**Characteristics:**
- Prefer written information
- Love taking detailed notes
- Enjoy reading textbooks and articles
- Learn by writing summaries

**Recommended resources:**
- 📚 Textbooks and comprehensive guides
- 📝 Written tutorials and documentation
- ✍️ Note-taking and summary exercises
- 📄 Articles and research papers
- 📋 Lists, definitions, and glossaries

**Study tips:**
- Take extensive notes
- Rewrite information in your own words
- Create written summaries
- Use flashcards with written content
- Read and re-read materials

---

### 💡 How the AI Uses Your Learning Style

When you select your learning style, the AI agents will:

1. **Roadmap Creator**: Structures your learning path with style-appropriate milestones
2. **Resource Finder**: Prioritizes resources matching your preferred format
3. **Tutor Agent**: Adapts explanations using style-specific techniques
4. **Quiz Generator**: Includes questions that align with your learning preferences

**Not sure which style fits you?** Try the **Mixed/Multimodal** approach, which combines elements from all styles!

## 🐛 Troubleshooting

### ModuleNotFoundError: No module named 'X'
**Solution:** Install missing dependencies
```bash
pip install -r requirements.txt
```

Common missing modules and their fixes:
- `phidata` → `pip install phidata`
- `openai` → `pip install openai`
- `chromadb` → `pip install chromadb`
- `langchain_chroma` → `pip install langchain-chroma`
- `langchain_openai` → `pip install langchain-openai`
- `duckduckgo_search` → `pip install duckduckgo-search`

### "streamlit: command not found"
**Solution:** Use Python module syntax
```bash
python3 -m streamlit run app.py
```

Or add `~/.local/bin` to your PATH:
```bash
export PATH="$HOME/.local/bin:$PATH"
```

### "No API key found" or API errors
**Solution:**
1. Ensure `.env` file exists in the project root
2. Verify your API key is correctly formatted:
   - Groq keys start with `gsk_`
   - OpenAI keys start with `sk-`
3. Check that the key is valid and active
4. For OpenAI: Ensure you have credits in your account

### "Failed to load document" (RAG feature)
**Solution:**
- Ensure PDF is not password-protected
- Check file is not corrupted
- Try converting to text format first
- Verify file size is reasonable (< 50MB recommended)

### "Agent not responding" or timeout errors
**Solution:**
- Check your internet connection
- Verify API key is valid and active
- Try switching to a different model in the app settings
- For Groq: Check [status.groq.com](https://status.groq.com)
- For OpenAI: Check [status.openai.com](https://status.openai.com)

### ChromaDB errors
**Solution:**
```bash
# Delete the vector database and restart
rm -rf chroma_db/
python3 -m streamlit run app.py
```

Ensure you have write permissions:
```bash
chmod -R 755 .
```

### Port already in use (Address already in use)
**Solution:**
```bash
# Kill existing Streamlit processes
pkill -f streamlit

# Or use a different port
streamlit run app.py --server.port 8502
```

## 🚀 Future Enhancements

- [ ] Progress tracking and analytics
- [ ] Spaced repetition scheduling
- [ ] Collaborative study groups
- [ ] Integration with learning platforms (Coursera, Udemy, etc.)
- [ ] Mobile app version
- [ ] Voice interaction for auditory learners
- [ ] Gamification and achievements
- [ ] Export to Anki flashcards

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- Built with [Phidata](https://docs.phidata.com/) multi-agent framework
- Powered by Groq and OpenAI LLMs
- Uses LangChain for document processing and RAG functionality

## 💬 Support

For issues, questions, or suggestions:
1. Check the troubleshooting section above
2. Review the configuration in `prompts.yaml`
3. Ensure all dependencies are correctly installed

---

**Happy Learning! 📚✨**

*Remember: The best way to learn is to start. Let AI agents guide your journey!*
