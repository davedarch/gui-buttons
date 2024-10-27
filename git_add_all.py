import os
from datetime import datetime

def add_all_and_commit():
    # Add all files
    add_command = 'git add -A'
    print(f"Executing command: {add_command}")
    os.system(add_command)
    
    # Commit with date and time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    commit_message = f'update: {current_time}'
    commit_command = f'git commit -m "{commit_message}"'
    print(f"Executing command: {commit_command}")
    os.system(commit_command)
    
    # Push the changes
    push_command = 'git push origin main'
    print(f"Executing command: {push_command}")
    os.system(push_command)

if __name__ == "__main__":
    add_all_and_commit()

