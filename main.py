import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from schemas import available_functions
from functions.call_function import call_function
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Load API key
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# System prompt
system_prompt = """
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

# Intro
print(Fore.CYAN + "🤖 Welcome to your AI CLI agent!")
print(Fore.YELLOW + "Type 'exit' to quit or 'help' for guidance.\n")

# Shared memory across turns
messages = []

# Main interaction loop
while True:
    user_input = input(Fore.GREEN + "You: " + Style.RESET_ALL)
    if user_input.strip().lower() in ["exit", "quit"]:
        print(Fore.CYAN + "👋 Goodbye!")
        break

    if user_input.strip().lower() == "help":
        print(Fore.BLUE + """
📘 Available commands:
- Natural language tasks like:
    - "run main.py"
    - "list files"
    - "write to file.txt"
    - "read lorem.txt"
- LLM will choose the right tool.
- Type 'exit' to quit the assistant.
""")
        continue

    # Add user message
    messages.append(types.Content(role="user", parts=[types.Part(text=user_input)]))

    for _ in range(20):
        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt
            )
        )

        for candidate in response.candidates:
            messages.append(candidate.content)

        if response.function_calls:
            for call in response.function_calls:
                tool_response = call_function(call)
                messages.append(tool_response)
        else:
            print(Fore.MAGENTA + "AI:", Fore.WHITE + response.text)
            break
