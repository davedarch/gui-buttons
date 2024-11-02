from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
import os

class PathCompleter(Completer):
    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        dirname = os.path.dirname(text)
        if not dirname:
            dirname = '.'
        basename = os.path.basename(text)
        try:
            for name in os.listdir(dirname):
                if name.startswith(basename) and (os.path.isdir(os.path.join(dirname, name)) or os.path.isfile(os.path.join(dirname, name))):
                    yield Completion(name, start_position=-len(basename))
        except OSError:
            pass

def git_mv():
    cwd = os.getcwd()
    completer = PathCompleter()
    
    # Prompt for the source file or directory name
    source_name = prompt("Enter the source file or directory name: ", completer=completer)
    if source_name:
        # Prompt for the destination file or directory name
        destination_name = prompt("Enter the destination file or directory name: ", completer=completer)
        
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
