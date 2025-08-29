import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.get_files_info import schema_get_files_info

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
def main():
    system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
        ]
    )

    if len(sys.argv) < 2:
        print("Usage: uv run main.py <prompt>")
        sys.exit(1)
    user_prompt = sys.argv[1]
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    is_verbose = False
    if len(sys.argv) > 2:
        is_verbose = False
        if sys.argv[2] == "--verbose":
            is_verbose = True
    generated_content = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
        ),
    )
    if generated_content.function_calls:
        for function_call_part in generated_content.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(generated_content.text)
    if is_verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {generated_content.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {generated_content.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
