from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os

def remove_file():
    cwd = os.getcwd()
    files = os.listdir(cwd)
    completer = WordCompleter(files, ignore_case=True)
    file_name = prompt("Enter the file name to remove: ", completer=completer)
    if file_name:
        # Remove the file
        remove_command = f'git rm "{file_name}"'
        print(f"Executing command: {remove_command}")
        os.system(remove_command)
        
        # Commit the change
        commit_message = f'Deleted {file_name}'
        commit_command = f'git commit -m "{commit_message}"'
        print(f"Executing command: {commit_command}")
        os.system(commit_command)
        
        # Push the changes
        push_command = 'git push origin main'
        print(f"Executing command: {push_command}")
        os.system(push_command)

if __name__ == "__main__":
    remove_file()

