# Hands-On Session Guide
## Agentic AI Workshop — Practical Exercises

This guide walks you through both hands-on examples step by step. No prior experience with AI APIs or Python frameworks is required — just follow the instructions in order.

---

## Prerequisites

- Python 3.9 or higher (check with `python --version`)
- An Anthropic API key ([get one free at console.anthropic.com](https://console.anthropic.com))
- A terminal / command prompt

---

## Step 1 — Get the Code

If you received a ZIP file, unzip it and open a terminal inside the `agentic-ai-workshop` folder.

If you are cloning from a repository:

```bash
git clone <repo-url>
cd agentic-ai-workshop
```

---

## Step 2 — Install Dependencies

Run this once to install everything the workshop needs:

```bash
uv venv --python 3.12
uv pip install -r requirements.txt
source .venv/bin/activate
```

The `requirements.txt` includes:

| Package | What it does |
|---------|-------------|
| `anthropic` | Python SDK for Claude — the AI model we use |
| `langchain` | Tooling for building LLM-powered agents |
| `langgraph` | Stateful multi-agent workflow framework |
| `fastmcp` | Framework for building MCP tool servers |
| `python-dotenv` | Loads environment variables from a `.env` file |
| `ipykernel` + `notebook` | Runs Jupyter notebooks in your browser |

---

## Step 3 — Set Up Your API Key

Your Anthropic API key is like a password — it lets you use Claude. We store it in a `.env` file (never in code).

1. Open `.env` in any text editor and replace the placeholder:

```
ANTHROPIC_API_KEY=your_api_key_here
OPENAI_API_KEY=your_api_key_here
```

with your actual key:

```
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxxxxx
OPENAI_API_KEY=sk-ope-xxxxxxxxxxxxxxxxxxxxxxxx
```

2. Save the file. **Do not share this file or commit it to Git.**

> 💡 **How to get a free API key:** Go to [console.anthropic.com](https://console.anthropic.com), sign up, and click "API Keys" → "Create Key".

---

## Step 4 — Launch Jupyter Notebook

From inside the `agentic-ai-workshop` folder, run:

```bash
jupyter notebook
```

This opens a browser tab. Navigate to the `notebooks/` folder and you'll see two notebooks.

---


## Step 5 - Run the MCP server

The MCP server is a small Python program that runs in the background and exposes the weather tool. Open a **separate terminal** window, navigate to the `agentic-ai-workshop` folder, and run:

```bash
python mcp_server/weather_server.py
```

You should see something like:

```
Starting MCP server: weather-server
```

Leave this terminal running while you work through the notebook.

## Step 6 - Run the notebooks


