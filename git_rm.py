from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os
import shutil

def remove_file():
    cwd = os.getcwd()
    files_and_dirs = os.listdir(cwd)
    completer = WordCompleter(files_and_dirs, ignore_case=True)
    file_or_dir_name = prompt("Enter the file or directory name to remove: ", completer=completer)
    if file_or_dir_name:
        full_path = os.path.join(cwd, file_or_dir_name)
        if os.path.isdir(full_path):
            # Remove the directory
            remove_command = f'git rm -r "{file_or_dir_name}"'
        else:
            # Remove the file
            remove_command = f'git rm "{file_or_dir_name}"'
        
        print(f"Executing command: {remove_command}")
        os.system(remove_command)
        
        # Commit the change
        commit_message = f'Deleted {file_or_dir_name}'
        commit_command = f'git commit -m "{commit_message}"'
        print(f"Executing command: {commit_command}")
        os.system(commit_command)
        
        # Push the changes
        push_command = 'git push origin main'
        print(f"Executing command: {push_command}")
        os.system(push_command)

if __name__ == "__main__":
    remove_file()
