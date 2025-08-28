import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
def main():
    if len(sys.argv) < 2:
        print("Usage: uv run main.py <prompt>")
        sys.exit(1)
    user_prompt = sys.argv[1]
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    is_verbose = False
    if sys.argv[2] == "--verbose":
        is_verbose = True
    generated_content = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    print(generated_content.text)
    if is_verbose:
        print(f"Prompt tokens: {generated_content.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {generated_content.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
