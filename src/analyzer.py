from google import genai
from prompts import ANALYZE_PROMPT
import os

key = os.getenv("Gemini_API_KEY")

client = genai.Client(api_key=key)


def analyze_workflow(workflow):
    prompt = ANALYZE_PROMPT.format(workflow=workflow)
    response = client.models.generate_content(
      model="gemini-2.5-flash", 
      contents=prompt
    )
    return response.text
 