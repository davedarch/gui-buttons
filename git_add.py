import os
import readline

def complete(text, state):
    # Get the current working directory
    cwd = os.getcwd()
    # List all files and directories in the current working directory
    options = [f for f in os.listdir(cwd) if f.startswith(text)]
    # Return the state-th completion option
    return options[state] if state < len(options) else None

def input_with_completion(prompt):
    # Set the completer function
    readline.set_completer(complete)
    # Use tab for completion
    readline.parse_and_bind('tab: complete')
    # Get user input
    return input(prompt)

def add_file():
    # Prompt the user for the file name with tab completion
    file_name = input_with_completion("Enter the file name to add: ").strip()
    if file_name:
        # Run the git add command with the specified file
        os.system(f'git add "{file_name}"')

if __name__ == "__main__":
    add_file()
