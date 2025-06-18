import os

def write_file(working_directory,file_path,content):
    working_directory=os.path.abspath(working_directory)
    path = os.path.abspath(os.path.join(working_directory, file_path))
    if not path.startswith(working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    os.makedirs(os.path.dirname(path),exist_ok=True)
    with open(path,"w") as f:
        f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    