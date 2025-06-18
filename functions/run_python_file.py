import os
import subprocess

def run_python_file(working_directory, file_path):
    working_directory = os.path.abspath(working_directory)
    path = os.path.abspath(os.path.join(working_directory, file_path))

    if not path.startswith(working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(path):
        filename = os.path.basename(file_path)
        found = False
        for root, _, files in os.walk(working_directory):
            if filename in files:
                path = os.path.join(root, filename)
                found = True
                break
        if not found:
            return f'Error: File "{file_path}" not found.'

    if not path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(["python3", path], timeout=30, capture_output=True)
        stdout = result.stdout.decode().strip()
        stderr = result.stderr.decode().strip()

        output = ""
        if stdout:
            output += f"✅ STDOUT:\n{stdout}\n"
        if stderr:
            output += f"⚠️ STDERR:\n{stderr}\n"
        if not stdout and not stderr:
            output = "🤖 No output produced."

        output += f"\nProcess exited with code {result.returncode}"
        return output

    except subprocess.TimeoutExpired:
        return f'Error: Execution of "{file_path}" timed out.'
