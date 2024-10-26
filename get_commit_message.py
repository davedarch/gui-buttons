import subprocess

def get_commit_message():
    # Prompt the user for a commit message via CLI
    commit_message = input("Enter your commit message: ").strip()
    return commit_message

def main():
    # Get the commit message from the user
    commit_message = get_commit_message()
    if commit_message:
        try:
            # Execute the git commit command
            subprocess.run(['git', 'commit', '-m', commit_message], check=True)
            print("Commit successful.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to commit: {e}")
    else:
        print("No commit message provided.")

if __name__ == "__main__":
    main()
