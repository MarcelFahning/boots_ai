import os
def write_file(working_directory, file_path, content):
    # checks if directory ends up inside the working path
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, file_path))
    rel_path = os.path.relpath(abs_target, abs_work)
    if rel_path == ("..") or rel_path.startswith(f"..{os.sep}"):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    elif not os.path.exists(abs_target):
        path, file_name = os.path.split(abs_target)
        if not os.path.exists(path):
            os.makedirs(path)
    with open(abs_target, "w") as f:
        f.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'