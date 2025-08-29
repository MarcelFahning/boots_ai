import os
from google.genai import types

def get_file_content(working_directory, file_path):
    # checks if directory ends up inside the working path
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, file_path))
    rel_path = os.path.relpath(abs_target, abs_work)
    if rel_path == ("..") or rel_path.startswith(f"..{os.sep}"):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(abs_target):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    MAX_CHARS = 10000
    with open(abs_target, "r") as f:
        file_content_string = f.read(MAX_CHARS + 1)
        if len(file_content_string) > MAX_CHARS:
            file_content_string = file_content_string[:MAX_CHARS]
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
    
    return file_content_string


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists the content of the specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file, relative to the working directory. If file is too long, truncates at 10000 characters",
            ),
        },
        required=["file_path"],
    ),
)