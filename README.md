# 🚀 MCP-ADK (Message Control Protocol - Agent Development Kit)

> A Python-based toolkit for building and managing agents with Wikipedia article extraction capabilities.

## 📋 Overview

MCP-ADK is a powerful toolkit that combines the Message Control Protocol (MCP) with an Agent Development Kit (ADK) to create intelligent agents capable of processing and extracting information from Wikipedia articles. The project provides a robust server implementation with real-time communication capabilities using Server-Sent Events (SSE).

## ✨ Features

- 📚 Wikipedia article extraction and conversion to markdown
- 🔄 Real-time communication using Server-Sent Events (SSE)
- 🛡️ Robust error handling and validation
- 🎯 Clean and modern API interface
- ⚡ Asynchronous processing capabilities

## 🛠️ Requirements

- Python >= 3.10
- Dependencies (automatically installed with the package):
  - `beautifulsoup4`
  - `deprecated`
  - `google-adk`
  - `html2text`
  - `mcp[cli]`
  - `requests`

## 🚀 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/mcp-adk.git
cd mcp-adk
```

2. **Create and activate a virtual environment:**
```bash
uv venv
source .venv/bin/activate
uv init
```

3. **Install the package by adding them in pyproject.toml:**
```bash
uv add "beautifulsoup4==4.12.3"
```

## 💻 Usage

### 🖥️ Starting the Server

Run the server using:
```bash
uv run server.py
```

The server will start on `localhost:8001`.

### 🔍 Using MCP Inspector

```bash
uv run mcp dev server.py
```

### 🌐 Launching ADK Server

After stopping MCP Inspector, launch the ADK server:
```bash
uv run adk web
```

### 🔌 API Endpoints

- `/sse` - Server-Sent Events endpoint for real-time communication
- `/messages/` - Endpoint for posting messages

### 📝 Example Usage

```python
from mcp_adk import agent

# Example code for using the agent
# (Add specific examples based on your implementation)
```

## 📁 Project Structure

```
mcp-adk/
├── adk-agent/          # Agent implementation
├── server.py           # Main server implementation
├── main.py            # Entry point
├── pyproject.toml     # Project configuration
└── README.md          # This file
```

