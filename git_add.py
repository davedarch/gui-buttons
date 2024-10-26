from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os

def add_file():
    cwd = os.getcwd()
    files = os.listdir(cwd)
    completer = WordCompleter(files, ignore_case=True)
    file_name = prompt("Enter the file name to add: ", completer=completer)
    if file_name:
        command = f'git add "{file_name}"'
        print(f"Executing command: {command}")  # Print the command to be executed
        os.system(command)

if __name__ == "__main__":
    add_file()
