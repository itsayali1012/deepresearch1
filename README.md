
# DeepResearch - AI Agent-Based Deep Research System

This is a **dual-agent AI system** designed to perform **deep web research** and **answer drafting** automatically.  
The system uses **Tavily API** for real-time information gathering, and **HuggingFace Transformers** for text summarization.  
The agent workflow is built with **LangGraph**, offering a lightweight, flexible graph-based orchestration.

---

##  Project Overview

| Component | Description |
|:----------|:------------|
| Research Agent | Queries Tavily API to gather raw research articles and data. |
| Drafting Agent | Summarizes the collected research into a concise, human-readable answer. |
| Workflow Engine | LangGraph is used to define the flow between agents easily and modularly. |

---

## ⚙ Technology Stack

- **Python 3.9+**
- **LangGraph** (`langgraph`)
- **Tavily API** (external service for search results)
- **HuggingFace Transformers** (for summarization using T5 model)
- **dotenv** (to manage API keys securely)

---

##  Installation Instructions

Follow these steps to set up and run the project:

1. **Clone the repository**
   ```bash
   git clone https://github.com/itsayali1012/deepresearch1.git
   cd deepresearch1

