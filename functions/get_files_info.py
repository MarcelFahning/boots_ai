import os
from google.genai import types
def get_files_info(working_directory, directory="."):
    # checks if directory ends up inside the working path
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, directory))
    rel_path = os.path.relpath(abs_target, abs_work)
    if rel_path == ("..") or rel_path.startswith(f"..{os.sep}"):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(abs_target):
        if os.path.isfile(abs_target):
            return f'Error: "{directory}" is a file, not a directory'
        return f'Error: "{directory}" is not a directory'

    dir_list = os.listdir(abs_target)
    if rel_path == ("."):
        file_stats = "Result for current directory:"
    else:
        file_stats = f"Result for {directory}:"
    for item in dir_list:
        file_path = f"{abs_target}/{item}"
        file_stats += f"\n- {item}: file_size={os.path.getsize(file_path)} bytes is_dir={os.path.isdir(file_path)}"

    return file_stats

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