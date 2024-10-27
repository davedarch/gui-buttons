from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os

def add_file():
    cwd = os.getcwd()
    files = os.listdir(cwd)
    completer = WordCompleter(files, ignore_case=True)
    file_name = prompt("Enter the file name to add: ", completer=completer)
    if file_name:
        # Add the file
        add_command = f'git add "{file_name}"'
        print(f"Executing command: {add_command}")
        os.system(add_command)
        
        # Commit the change
        commit_message = f'Added {file_name}'
        commit_command = f'git commit -m "{commit_message}"'
        print(f"Executing command: {commit_command}")
        os.system(commit_command)
        
        # Push the changes
        push_command = 'git push origin main'
        print(f"Executing command: {push_command}")
        os.system(push_command)

if __name__ == "__main__":
    add_file()
