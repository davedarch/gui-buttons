from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os

def rename_file():
    cwd = os.getcwd()
    files = os.listdir(cwd)
    completer = WordCompleter(files, ignore_case=True)
    
    # Prompt for the old file name
    old_file_name = prompt("Enter the file name to rename: ", completer=completer)
    if old_file_name:
        # Prompt for the new file name
        new_file_name = prompt("Enter the new file name: ")
        
        # Rename the file
        rename_command = f'git mv "{old_file_name}" "{new_file_name}"'
        print(f"Executing command: {rename_command}")
        os.system(rename_command)
        
        # Stage the changes
        stage_command = 'git add -A'
        print(f"Executing command: {stage_command}")
        os.system(stage_command)
        
        # Commit the change
        commit_message = f'Rename file from {old_file_name} to {new_file_name}'
        commit_command = f'git commit -m "{commit_message}"'
        print(f"Executing command: {commit_command}")
        os.system(commit_command)
        
        # Push the changes
        push_command = 'git push origin main'
        print(f"Executing command: {push_command}")
        os.system(push_command)

if __name__ == "__main__":
    rename_file()

