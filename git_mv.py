from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os

def git_mv():
    cwd = os.getcwd()
    # List both files and directories
    items = [item for item in os.listdir(cwd) if os.path.isfile(item) or os.path.isdir(item)]
    completer = WordCompleter(items, ignore_case=True)
    
    # Prompt for the source file or directory name
    source_name = prompt("Enter the source file or directory name: ", completer=completer)
    if source_name:
        # Prompt for the destination file or directory name
        destination_name = prompt("Enter the destination file or directory name: ")
        
        # Execute the git mv command
        mv_command = f'git mv "{source_name}" "{destination_name}"'
        print(f"Executing command: {mv_command}")
        os.system(mv_command)
        
        # Stage the changes
        stage_command = 'git add -A'
        print(f"Executing command: {stage_command}")
        os.system(stage_command)
        
        # Commit the change
        commit_message = f'Move {source_name} to {destination_name}'
        commit_command = f'git commit -m "{commit_message}"'
        print(f"Executing command: {commit_command}")
        os.system(commit_command)
        
        # Push the changes
        push_command = 'git push origin main'
        print(f"Executing command: {push_command}")
        os.system(push_command)

if __name__ == "__main__":
    git_mv()
