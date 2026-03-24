# AI Workflow Analyzer

An AI-powered tool that analyzes workflows, identifies inefficiencies, and suggests automation opportunities using Large Language Models.


## Overview

This project helps teams understand and improve their internal processes by leveraging AI. Users can input a workflow description, and the system returns a structured analysis including problems, automation opportunities, and AI-driven solutions.


## Features

- Analyze workflows in real time
- Identify inefficiencies and bottlenecks
- Suggest AI-based automation strategies
- Generate prototype ideas for implementation
- Export analysis as a Markdown (.md) file
- Simple and interactive UI using Streamlit


## Demo
[Live demo](https://workflow-analyzer-y9lzx6np6hykxzewv6covz.streamlit.app/)

Users can:
1. Enter a workflow description
2. Receive structured AI analysis
3. Download the results as a Markdown report


## Example Input

 - Our engineering team manually reviews logs and writes daily summaries. This process is slow and inconsistent.


## Example Output

- **Problems**
  - Manual and repetitive work
  - Time-consuming process
  - Inconsistent results

- **Automation Opportunities**
  - Automate log summarization
  - Standardize reporting

- **AI Solution**
  - Use an LLM to extract key insights and generate summaries

- **Prototype Idea**
  - Python script that processes logs and generates summaries using an AI API


## Tech Stack

- Python
- Streamlit
- Google Gemini API (LLM)


## Project Structure
 ```
src/
  ├── main.py
  ├── analyzer.py
  ├── prompts.py
```


## Installation

```bash
git clone https://github.com/YamenRM/workflow-analyzer.git
cd workflow-analyzer
pip install -r requirements.txt
```

## Setup
Set your API key as an environment variable:
 - Windows (PowerShell)
   ```
    setx GEMINI_API_KEY "your_api_key_here"
   ```
 
 - Linux / macOS
   ```
    export GEMINI_API_KEY="your_api_key_here"
   ```

### Run the App
```
streamlit run main.py
```

## Use Cases
 - Engineering workflow optimization
 - AI adoption analysis
 - Process automation planning
 - Internal tooling prototyping


## Future Improvements
 - Structured JSON output
 - Workflow visualization (diagrams)
 - History tracking of analyses
 - Multi-workflow comparison
 - Integration with team tools (e.g., GitLab, Notion)


##Author

**YamenRM**
