# file_handling_assignment.py

def create_and_write_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("This is the first line of text.\n")
            file.write("The number 42 is included here.\n")
            file.write("End of the initial content.\n")
        print("File created and initial content written.")
    except Exception as e:
        print(f"An error occurred while creating/writing the file: {e}")

def read_and_display_file():
    try:
        with open("my_file.txt", 'r') as file:
            contents = file.read()
        print("File content:\n" + contents)
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Appending first new line.\n")
            file.write("Another line with the number 24.\n")
            file.write("Final line of the appended content.\n")
        print("New content appended to the file.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    create_and_write_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()

if __name__ == "__main__":
    main()
