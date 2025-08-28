from functions.write_file import write_file
from functions.get_file_content import get_file_content
def main():

    #print(get_file_content("calculator", "lorem.txt"))
    #print("-----")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(get_file_content("calculator", "lorem.txt"))
    print("-----")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(get_file_content("calculator", "pkg/morelorem.txt"))
    print("-----")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print(get_file_content("calculator", "/tmp/temp.txt"))
    #print("-----")
    #print(get_file_content("calculator", "pkg/does_not_exist.py"))
    

if __name__ == "__main__":
    main()