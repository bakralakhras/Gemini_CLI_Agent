import os

def get_file_content(working_directory,file_path):
    working_directory=os.path.abspath(working_directory)
    path = os.path.abspath(os.path.join(working_directory, file_path))
    print(f"wc is {working_directory}")
    print(f"path is :{path}")

    if not path.startswith(working_directory):
        return f'Error: cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(path):
        f'Error: File not found or is not a regular file: "{file_path}"'
    try:

        MAX_CHARS= 10000
        with open(path,"r") as f:
            file_content_string=f.read(MAX_CHARS)
            truncated=f.read(1)!=""
        if truncated:
            return file_content_string+'[...File "{file_path}" truncated at 10000 characters]'
        else:
            return file_content_string
    except Exception as e:
            return f"Error listing files: {e}"