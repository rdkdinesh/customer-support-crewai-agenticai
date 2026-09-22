````markdown
# 🤖 Agentic AI Customer Support using CrewAI

A multi-agent **Customer Support AI application** built using **CrewAI, Streamlit, and Python**.

The application uses multiple specialized AI agents to handle customer queries:

- 📚 **Agent 1 – FAQ Agent** → Answers questions using a local FAQ knowledge base.
- 🌐 **Agent 2 – Web Search Agent** → Searches the web when additional/current information is required.
- 💾 **Agent 3 – Logger Agent** → Saves the customer query and agent responses into a local text file.
- 🖥️ **Streamlit UI** → Provides a simple and interactive customer-support chat interface.

The entire initial implementation is intentionally kept inside a **single `app.py` file** to make it easy to understand and learn.

---

# 🏗️ Architecture

```text
                         ┌─────────────────────────┐
                         │      Streamlit UI       │
                         │                         │
                         │  Customer Support Chat  │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │       CrewAI Crew       │
                         │                         │
                         │    Multi-Agent System   │
                         └────────────┬────────────┘
                                      │
                ┌─────────────────────┼─────────────────────┐
                │                     │                     │
                ▼                     ▼                     ▼
       ┌────────────────┐    ┌────────────────┐    ┌────────────────┐
       │    Agent 1     │    │    Agent 2     │    │    Agent 3     │
       │                │    │                │    │                │
       │   FAQ Agent    │    │  Web Search    │    │  Logger Agent  │
       │                │    │     Agent      │    │                │
       └───────┬────────┘    └───────┬────────┘    └───────┬────────┘
               │                     │                     │
               ▼                     ▼                     ▼
          ┌─────────┐          ┌───────────┐       ┌──────────────┐
          │ faq.txt │          │ Web Search│       │ support_log  │
          │         │          │   API     │       │    .txt      │
          └─────────┘          └───────────┘       └──────────────┘
````

---

# 🎯 Project Objective

Traditional customer-support systems often depend on static FAQ pages or manual support teams.

This project demonstrates how **Agentic AI** can divide customer-support responsibilities among specialized AI agents.

Instead of asking one AI agent to perform everything, each agent has a specific responsibility.

```text
Customer
   │
   ▼
Customer Query
   │
   ▼
AI Agent System
   │
   ├── Local FAQ Agent
   │
   ├── Web Search Agent
   │
   └── Logger Agent
   │
   ▼
Customer Support Response
```

---

# 🤖 Agents

## Agent 1 – FAQ Agent

### Responsibility

The FAQ Agent answers customer questions using the locally maintained `faq.txt` file.

### Knowledge Source

```text
faq.txt
```

### Example

Customer:

```text
How can I reset my password?
```

FAQ Agent:

```text
You can reset your password from the login page
by selecting "Forgot Password" and following the
instructions sent to your registered email address.
```

The agent is instructed not to invent information that is not present in the FAQ.

---

# 🌐 Agent 2 – Web Search Agent

### Responsibility

The Web Search Agent performs web research when additional or current information is required.

Example:

```text
What is the latest version of Python?
```

The agent can search the internet and provide a current response.

The initial implementation uses:

```text
CrewAI
    │
    ▼
SerperDevTool
    │
    ▼
Serper Web Search API
```

### Environment Variable

```text
SERPER_API_KEY
```

---

# 💾 Agent 3 – Logger Agent

### Responsibility

The Logger Agent maintains a local record of customer-support interactions.

The output is stored in:

```text
customer_support_log.txt
```

Example:

```text
============================================================
CUSTOMER SUPPORT INTERACTION
============================================================

Timestamp:
2026-09-22 10:30:25

Customer Query:
How can I reset my password?

Agent 1 FAQ Response:
You can reset your password from the login page...

Agent 2 Web Response:
Additional information...

============================================================
```

This provides a simple local audit trail.

---

# 🖥️ Streamlit User Interface

The application provides a simple chat interface using Streamlit.

Example:

```text
┌──────────────────────────────────────────────────┐
│ 🤖 AI Customer Support Agent                    │
│                                                  │
│ Multi-Agent Customer Support using CrewAI       │
│                                                  │
│ ┌──────────────────────────────────────────────┐ │
│ │ 💬 Ask your customer-support question...    │ │
│ └──────────────────────────────────────────────┘ │
│                                                  │
│              [AI Response]                       │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

# 🛠️ Technology Stack

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python        | Application development   |
| CrewAI        | Multi-agent orchestration |
| CrewAI Tools  | Agent tools               |
| Streamlit     | Web UI                    |
| OpenAI        | LLM                       |
| Serper        | Web search                |
| python-dotenv | Environment configuration |

---

# 📁 Project Structure

```text
customer-support-crewai-agenticai/
│
├── app.py
│
├── faq.txt
│
├── customer_support_log.txt
│
├── requirements.txt
│
├── .env
│
└── README.md
```

### File Description

```text
app.py
```

Main application containing:

* Streamlit UI
* CrewAI agents
* CrewAI tasks
* Crew configuration
* FAQ loading
* Web search
* Logging

---

```text
faq.txt
```

Local customer-support FAQ knowledge base.

---

```text
customer_support_log.txt
```

Local support interaction log generated by the application.

---

```text
requirements.txt
```

Python dependencies.

---

```text
.env
```

Environment variables and API keys.

> Do not commit `.env` to GitHub.

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/<your-github-username>/customer-support-crewai-agenticai.git
```

Navigate to the project:

```bash
cd customer-support-crewai-agenticai
```

---

# 🐍 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

# 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
crewai
crewai-tools
streamlit
python-dotenv
```

---

# 🔐 4. Configure Environment Variables

Create:

```text
.env
```

Add:

```text
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

### Important

Never commit API keys to GitHub.

Add this to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

# ▶️ 5. Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will start locally.

Open the Streamlit URL shown in the terminal, typically:

```text
http://localhost:8501
```

---

# 💬 Example Questions

### FAQ Question

```text
How can I reset my password?
```

Expected behavior:

```text
Customer Query
      │
      ▼
FAQ Agent
      │
      ▼
Search faq.txt
      │
      ▼
FAQ Answer
```

---

### Another FAQ Question

```text
What are your customer support hours?
```

The FAQ Agent retrieves the relevant information from `faq.txt`.

---

### Web Search Question

```text
What is the latest version of Python?
```

Expected flow:

```text
Customer Query
      │
      ▼
Web Search Agent
      │
      ▼
Serper
      │
      ▼
Web Results
      │
      ▼
AI Generated Response
```

---

# 🔄 Agent Execution Flow

The current learning implementation uses a sequential CrewAI process.

```text
Customer Query
      │
      ▼
┌────────────────────┐
│ Agent 1            │
│ FAQ Specialist     │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Agent 2            │
│ Web Research       │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Agent 3            │
│ Audit / Logger     │
└─────────┬──────────┘
          │
          ▼
customer_support_log.txt
```

---

# 🧠 Why Multi-Agent AI?

Instead of creating one large AI agent with many responsibilities, we divide the problem into specialized agents.

### Traditional approach

```text
Customer
   │
   ▼
Single AI Agent
   │
   ├── FAQ
   ├── Web Search
   ├── Logging
   └── Response
```

### Agentic approach

```text
Customer
   │
   ▼
Multi-Agent System
   │
   ├── FAQ Agent
   │
   ├── Web Search Agent
   │
   └── Logger Agent
```

Each agent has:

* A specific role
* A specific goal
* A specific responsibility
* Potentially different tools
* Its own task

---

# 🔮 Future Enhancements

This project can be extended into a production-oriented Agentic AI customer-support platform.

## 1. Intelligent Router Agent

Add a router that determines whether the customer question should use the local FAQ or web search.

```text
                  Customer Query
                        │
                        ▼
                 ┌──────────────┐
                 │ Router Agent │
                 └──────┬───────┘
                        │
              ┌─────────┴─────────┐
              │                   │
              ▼                   ▼
        Local FAQ             Web Search
              │                   │
              ▼                   ▼
          Agent 1               Agent 2
              │                   │
              └─────────┬─────────┘
                        ▼
                    Agent 3
                     Logger
```

This avoids unnecessary web searches for questions that are already answered in the FAQ.

---

# 2. RAG-Based FAQ

Replace the simple `faq.txt` lookup with:

```text
FAQ Documents
      │
      ▼
Document Loader
      │
      ▼
Text Splitting
      │
      ▼
Embeddings
      │
      ▼
FAISS Vector Database
      │
      ▼
Retriever
      │
      ▼
FAQ Agent
```

Potential technologies:

* LangChain
* Hugging Face Embeddings
* FAISS
* OpenAI Embeddings

---

# 3. Knowledge Graph

Introduce a knowledge graph for relationships between:

```text
Customer
   │
   ├── Order
   │
   ├── Product
   │
   ├── Payment
   │
   └── Support Request
```

Possible technology:

```text
Neo4j
```

---

# 4. Guardrails

Add input and output validation.

```text
Customer Query
      │
      ▼
Input Guardrail
      │
      ▼
Agentic Workflow
      │
      ▼
Output Guardrail
      │
      ▼
Customer
```

Guardrails can help enforce:

* Appropriate queries
* Data protection
* Response format
* Prompt-injection protection
* Sensitive information handling

---

# 5. Evaluation

Add an evaluation layer to measure:

```text
Answer Relevance
Answer Accuracy
Faithfulness
Retrieval Quality
Response Time
```

Possible evaluation technologies:

* RAGAS
* LangSmith
* Custom evaluation agents

---

# 6. Conversation Memory

Add conversation history:

```text
Customer
   │
   ▼
Streamlit Chat
   │
   ▼
Conversation Memory
   │
   ▼
CrewAI Agents
```

This allows the support agent to understand follow-up questions.

Example:

```text
Customer:
How do I reset my password?

AI:
Go to the login page...

Customer:
What if I don't receive the email?
```

The system can understand that "email" refers to the password-reset email.

---

# 7. Human Handoff

For complex cases:

```text
Customer Query
      │
      ▼
Agentic System
      │
      ├── Resolved
      │
      └── Needs Human
               │
               ▼
        Human Support Team
```

---

# 🚀 Target Production Architecture

The learning version can eventually evolve into:

```text
                         Customer
                            │
                            ▼
                    ┌───────────────┐
                    │   Streamlit   │
                    │      UI       │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Router Agent  │
                    └───────┬───────┘
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
        FAQ/RAG Agent   Web Agent    Order Agent
             │              │              │
             ▼              ▼              ▼
           FAISS          Web APIs      Business APIs
             │              │              │
             └──────────────┼──────────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Response      │
                    │ Validation    │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Logger /      │
                    │ Audit Agent   │
                    └───────┬───────┘
                            │
                            ▼
                     Support Record
```

---

# 🔒 Security Considerations

Never commit secrets:

```text
OPENAI_API_KEY
SERPER_API_KEY
```

Use:

```text
.env
```

and add:

```text
.env
```

to `.gitignore`.

For production deployment, use a proper secret-management solution instead of storing secrets directly in source code.

---

# 🧪 Troubleshooting

## `ModuleNotFoundError: No module named 'crewai_tools'`

Run:

```bash
pip install crewai-tools
```

Verify:

```bash
python -c "from crewai_tools import SerperDevTool; print('OK')"
```

---

## Serper `403 Unauthorized`

If you receive:

```text
HTTP STATUS: 403
{"message":"Unauthorized","statusCode":403}
```

verify:

```text
SERPER_API_KEY
```

in `.env`.

Test:

```bash
python -c "import os, requests; from dotenv import load_dotenv; load_dotenv(override=True); key=os.getenv('SERPER_API_KEY'); r=requests.post('https://google.serper.dev/search', headers={'X-API-KEY':key,'Content-Type':'application/json'}, json={'q':'CrewAI'}, timeout=30); print(r.status_code); print(r.text[:500])"
```

A successful authentication should return an HTTP success response rather than `403 Unauthorized`.

---

# 📚 Learning Outcomes

This project demonstrates practical concepts in:

* Agentic AI
* Multi-Agent Systems
* CrewAI
* AI Agents
* Agent Roles and Goals
* Agent Tasks
* Agent Orchestration
* Tool Calling
* Web Search
* Local Knowledge Bases
* Streamlit
* LLM Applications
* AI Customer Support
* AI Automation

---

# 🌟 Key Concepts

```text
LLM
 │
 ▼
AI Agent
 │
 ├── Role
 ├── Goal
 ├── Backstory
 ├── Tools
 └── Task
      │
      ▼
   CrewAI
      │
      ▼
Multi-Agent Workflow
```

---

# 📌 Project Status

### Current Version

```text
✅ Streamlit UI
✅ CrewAI
✅ Agent 1 – Local FAQ
✅ Agent 2 – Web Search
✅ Agent 3 – Local Logger
✅ Local support log
```

### Planned

```text
⬜ Intelligent Router Agent
⬜ FAISS RAG
⬜ Knowledge Graph
⬜ Guardrails
⬜ Evaluation
⬜ Conversation Memory
⬜ Human Handoff
⬜ Production API integration
```

---

# 👨‍💻 Author

**Dinesh Kumar**

AI & Java Full Stack Developer | GenAI | Agentic AI | RAG | Spring Boot

LinkedIn:

[www.linkedin.com/in/dinesh-ai-man](http://www.linkedin.com/in/dinesh-ai-man)

---

# ⭐ If You Find This Project Useful

Consider giving the repository a ⭐ on GitHub and following the project for future updates on:

* Generative AI
* Agentic AI
* CrewAI
* RAG
* LangChain
* Java + AI
* Spring Boot + AI
* AI Automation

---

## 📄 License

This project is intended for learning and demonstration purposes.

````

### Suggested GitHub repository name

```text
customer-support-crewai-agenticai
````

### Suggested repository description

> 🤖 Agentic AI Customer Support application using CrewAI, Streamlit, local FAQ knowledge, web search, and multi-agent response logging.

This README also leaves a clean path for the **next iteration: Router Agent → FAISS RAG → Guardrails → Evaluation → Knowledge Graph**, rather than overcomplicating the first version.
