from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from google.genai import types



def call_function(function_call_part,verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    working_directory="./calculator"
    function_map={"get_files_info":get_files_info,"get_file_content":get_file_content,"run_python_file":run_python_file,"write_file":write_file}
    func=function_map.get(function_call_part.name)
    if function_call_part.name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )
    try:
        result=func(working_directory,**function_call_part.args)
    except Exception as e:
             result = f"Function raised an error: {str(e)}"

    return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": result},
                )
            ],
        )