# deepresearch1
# DeepResearch - AI Agent-Based Deep Research System

This is a **dual-agent AI system** designed to perform **deep web research** and **answer drafting** automatically.  
The system uses **Tavily API** for real-time information gathering, and **HuggingFace Transformers** for text summarization.  
The agent workflow is built with **LangGraph**, offering a lightweight, flexible graph-based orchestration.

---

## 📚 Project Overview

| Component | Description |
|:----------|:------------|
| Research Agent | Queries Tavily API to gather raw research articles and data. |
| Drafting Agent | Summarizes the collected research into a concise, human-readable answer. |
| Workflow Engine | LangGraph is used to define the flow between agents easily and modularly. |

---

## ⚙️ Technology Stack

- **Python 3.9+**
- **LangGraph** (`langgraph`)
- **Tavily API** (external service for search results)
- **HuggingFace Transformers** (for summarization using T5 model)
- **dotenv** (to manage API keys securely)

---

## 🚀 Installation Instructions

Follow these steps to set up and run the project:

1. **Clone the repository**
   ```bash
   git clone https://github.com/itsayali1012/deepresearch1.git
   cd deepresearch1
Create a virtual environment (recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # For Linux/Mac
venv\Scripts\activate       # For Windows
Install the required Python packages

bash
Copy
Edit
pip install -r requirements.txt
Set up your environment variables

Create a .env file in the project directory.

Add your Tavily API Key inside .env:

ini
Copy
Edit
TAVILY_API_KEY=your_actual_tavily_api_key_here
Run the main program

bash
Copy
Edit
python deep_research_agents/main.py
