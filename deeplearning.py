# deep_research_agents/main.py ( using Tavily + HuggingFace + LangGraph)

import os
import requests
from dotenv import load_dotenv
from langgraph.graph import StateGraph
from transformers import pipeline

summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base")

def split_text(text, max_chunk_length=500):
    words = text.split()
    for i in range(0, len(words), max_chunk_length):
        yield ' '.join(words[i:i + max_chunk_length])

research_data_chunks = list(split_text(research_data, max_chunk_length=450))

summaries = []
for chunk in research_data_chunks:
    summary = summarizer(chunk, max_length=200, min_length=50, do_sample=False)[0]['summary_text']
    summaries.append(summary)

final_summary = "\n".join(summaries)

# Load environment variables
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Agent 1: Research Agent using Tavily API #
def research_agent(state):
    query = state["query"]
    print(f"[Research Agent] Searching Tavily for: {query}")

    url = "https://api.tavily.com/search"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TAVILY_API_KEY}"
    }

    payload = {
        "query": query,
        "search_depth": "advanced",  # Changed from basic to advanced for more in-depth results
        "include_answer": True,
        "include_raw_content": True,  # Set to True to get full text instead of summary
        "include_images": False,
        "max_results": 5
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        # Debug: Print entire response content for validation
        print("\n[DEBUG] Full Tavily Response:\n", data)

        articles = "\n\n".join(
            [item.get("raw_content", "") or item.get("content", "") for item in data.get("results", [])]
        )

        print("\n[Raw Research Data]\n", articles[:1000],
              "..." if len(articles) > 1000 else "")  # Print only first 1000 chars

        return {"query": query, "research_data": articles if articles else "No relevant content found."}

    except Exception as e:
        print(f"[ERROR] Tavily API failed: {e}")
        return {"query": query, "research_data": "No data found."}


#  Agent 2: Drafting Agent using HuggingFace  #
def draft_agent(state):
    research_data = state["research_data"]
    print("[Drafting Agent] Summarizing research data...")
    summarizer = pipeline("summarization", model="google/flan-t5-base")
    summary = summarizer(research_data, max_length=200, min_length=50, do_sample=False)
    return {"final_answer": summary[0]['summary_text']}

# LangGraph Setup #
from langgraph.graph import StateGraph

# Use dict to define a flexible schema
workflow = StateGraph(dict)

workflow.add_node("research", research_agent)
workflow.add_node("draft", draft_agent)

workflow.set_entry_point("research")
workflow.add_edge("research", "draft")
workflow.set_finish_point("draft")

compiled_graph = workflow.compile()

# Run  #
if __name__ == "__main__":
    user_query = input("Enter your research topic: ")
    result = compiled_graph.invoke({"query": user_query})
    print("\n[Generated Answer]\n")
    print(result["final_answer"])
