import os
import subprocess

def run_python_file(working_directory,file_path):
    working_directory=os.path.abspath(working_directory)
    path = os.path.abspath(os.path.join(working_directory, file_path))
    if not path.startswith(working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(path):
        return f'Error: File "{file_path}" not found.'
    if not path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result=subprocess.run(["python3",path],timeout=30,capture_output=True)
        output=f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"
        if result.returncode == 0:
            output+=f"Process exited with code {result.returncode}"
        if not result.stdout and not result.stderr:
            output="No output produced." 
        return output
    except subprocess.TimeoutExpired:
        return f'Error: Execution of "{file_path}" timed out.'