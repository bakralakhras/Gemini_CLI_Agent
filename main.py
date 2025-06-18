import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from schemas import available_functions
from functions.call_function import call_function

args=sys.argv[1:]
if len(sys.argv)<2:
    print("error")
    sys.exit(1)

verbose = "--verbose" in sys.argv
user_prompt=" ".join(args)
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)
user_prompt=" ".join(args)
system_prompt=system_prompt = system_prompt = """
You are a helpful AI coding agent.

When a user asks to run a Python file, do not ask for clarification.
Ignore any flags like --verbose or --test unless you are specifically asked to include them as part of the file path.

Assume the file is in the working directory and can be safely executed as-is.

You can perform the following operations:
- List files and directories
- Read file contents
- Execute Python files
- Write or overwrite files

All paths must be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected.
"""




messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

for _ in range(20):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(tools=
         [available_functions],system_instruction=system_prompt)
    )
    for candidate in response.candidates:
         messages.append(candidate.content)
    if response.function_calls:
         for call in response.function_calls:
              tool_response=call_function(call)
              messages.append(tool_response)
    else:
         print(f"final resposne: {response.text}")
         break

if verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")



