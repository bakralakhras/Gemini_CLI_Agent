import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content=types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a file within the specified working directory, up to 10,000 characters. Prevents access to files outside the allowed path and detects if the file was truncated.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path":types.Schema(
                type=types.Type.STRING,
                description="Reads the content of a file within the specified working directory, up to 10,000 characters. Prevents access to files outside the allowed path and detects if the file was truncated."

            )
        }
    ),
)
schema_run_python_file=types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file located within the specified working directory and captures its output. Enforces security by preventing access outside the allowed path.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path":types.Schema(
                type=types.Type.STRING,
                description="Executes a Python file located within the specified working directory and captures its output. Enforces security by preventing access outside the allowed path."
            )
    
        }
    )

)
schema_write_file=types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the specified working directory. Automatically creates any missing directories and prevents writing outside the allowed path.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path":types.Schema(
                type=types.Type.STRING,
                description="Writes content to a file within the specified working directory. Automatically creates any missing directories and prevents writing outside the allowed path."

            ),
            "content":types.Schema(
                type=types.Type.STRING,
                description="the text content to write into the file"
            )
        }
    )
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,schema_run_python_file,schema_get_file_content,schema_write_file

    ]
)