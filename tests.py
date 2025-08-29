from functions.write_file import write_file
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
def main():

    print(run_python_file("calculator", "main.py"))
    print("-----")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print("-----")
    print(run_python_file("calculator", "tests.py"))
    print("-----")
    print(run_python_file("calculator", "../main.py"))
    print("-----")
    print(run_python_file("calculator", "nonexistent.py"))
    

if __name__ == "__main__":
    main()