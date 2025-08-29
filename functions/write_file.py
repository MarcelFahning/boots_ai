import os
from google.genai import types

def write_file(working_directory, file_path, content):
    # checks if directory ends up inside the working path
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, file_path))
    rel_path = os.path.relpath(abs_target, abs_work)
    if rel_path == ("..") or rel_path.startswith(f"..{os.sep}"):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_target):
        try:
            os.makedirs(os.path.dirname(abs_target), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    if os.path.exists(abs_target) and os.path.isdir(abs_target):
        return f'Error: "{file_path}" is a directory, not a file'
    try:
        with open(abs_target, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: writing to file: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes into the specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file": types.Schema(
                type=types.Type.STRING,
                description="The file to write into, relative to the working directory.",
            ),
        },
    ),
)