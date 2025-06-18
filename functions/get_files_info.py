import os

def get_files_info(working_directory, directory=None):
    working_directory = os.path.abspath(working_directory)
    path = os.path.abspath(os.path.join(working_directory, directory))

    if not path.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'

    lines = []
    try:
        for item in os.listdir(path):
            full_item_path = os.path.join(path, item)
            size = os.path.getsize(full_item_path)
            is_dir = os.path.isdir(full_item_path)
            lines.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error listing files: {e}"




