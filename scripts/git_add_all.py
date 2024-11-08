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
    
    # Ask user for the branch to push to
    branch = input("Enter the branch to push to: ")
    
    # Push the changes
    push_command = f'git push origin {branch}'
    print(f"Executing command: {push_command}")
    os.system(push_command)

if __name__ == "__main__":
    add_all_and_commit()

