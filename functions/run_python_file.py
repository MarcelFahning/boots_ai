import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    # checks if directory ends up inside the working path
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, file_path))
    rel_path = os.path.relpath(abs_target, abs_work)
    if rel_path == ("..") or rel_path.startswith(f"..{os.sep}"):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_target):
        return f'Error: File "{file_path}" not found.'
    if not abs_target.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        completed_process = subprocess.run(
            ["python3", abs_target] + args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=working_directory,
            timeout=30
            )

        output_string = f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"
        if completed_process.returncode != 0:
            output_string += f"\nProcess exited with code {completed_process.returncode}"
        if output_string == "":
            output_string = "No output produced"
        return output_string
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the spedified Python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING
                )
            )
        },
        required=["file_path"],
    ),
)
    