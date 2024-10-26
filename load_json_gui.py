import tkinter as tk
from tkinter import ttk, filedialog, simpledialog, messagebox
import subprocess
import platform
from functools import partial
import tkmacosx as tkm
from tkmacosx import SFrame
import json
import os

class Tooltip:
    def __init__(self, widget, long_description='widget info', text_widget=None):
        self.widget = widget
        self.long_description = long_description
        self.text_widget = text_widget
        self.widget.bind("<Enter>", self.show_tip)
        self.widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        if self.text_widget:
            self.text_widget.config(state='normal')
            self.text_widget.delete('1.0', tk.END)
            # Insert only the long description
            self.text_widget.insert(tk.END, self.long_description, 'description')
            self.text_widget.tag_configure('description', foreground="#5A9")
            self.text_widget.config(state='disabled')

    def hide_tip(self, event=None):
        if self.text_widget:
            self.text_widget.config(state='normal')
            self.text_widget.delete('1.0', tk.END)
            self.text_widget.insert(tk.END, "Hover over a button to see its description here.", 'description')
            self.text_widget.config(state='disabled')

def get_commit_message():
    # Prompt the user for a commit message
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    commit_message = simpledialog.askstring("Commit Message", "Enter your commit message:")
    root.destroy()
    return commit_message

def run_shell_command_in_frontmost_terminal(command):
    try:
        # Check if the command is a git commit and needs a message
        if 'git commit -m <message>' in " ".join(command):
            commit_message = get_commit_message()
            if not commit_message:
                messagebox.showwarning("Commit Cancelled", "No commit message provided. Commit cancelled.")
                return
            # Replace the placeholder with the actual commit message
            command = [part.replace('<message>', commit_message) for part in command]
        
        # Join the command list into a single string with proper spacing
        full_command = " ".join(command)
        
        # Check for the placeholder and replace it with the actual folder name
        if '`basename "$PWD"`' in full_command:
            folder_name = os.path.basename(os.getcwd())
            full_command = full_command.replace('`basename "$PWD"`', folder_name)
        
        # Escape double quotes for AppleScript
        full_command_escaped = full_command.replace('"', '\\"')
        
        # Construct the AppleScript command to execute normally
        applescript_command = f'''
        tell application "Terminal"
            activate
            do script "{full_command_escaped}" in front window
        end tell
        '''
        
        # Execute the AppleScript command
        subprocess.run(['osascript', '-e', applescript_command], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Shell command failed: {e}")

def create_button(parent, text, long_description, command, args=(), bg_color="#2C2C2E", fg_color="white", font_size=22, description_text=None):
    # Create a frame to hold the button and its command
    frame = tk.Frame(parent, bg=bg_color)
    frame.pack(pady=2, fill='x', padx=10)

    # Create the button
    btn = tkm.Button(
        frame, 
        text=text, 
        command=partial(command, *args), 
        bg=bg_color, 
        fg=fg_color, 
        font=('Helvetica', font_size),
        borderless=1
    )
    btn.pack(side='left', padx=5, pady=5)

    # Add tooltip to the button using the long description
    Tooltip(btn, long_description=long_description, text_widget=description_text)

    # Create the command text widget
    command_text = " ".join(args[0]) if isinstance(args[0], list) else args[0]
    command_text_widget = tk.Text(
        frame,
        height=1,
        bg=bg_color,
        fg="#5A9",  # Set the command text color to a grey/blue
        font=('Helvetica', font_size),
        wrap='none',
        borderwidth=0,
        highlightthickness=0
    )
    command_text_widget.insert(tk.END, command_text)
    command_text_widget.config(state='disabled')  # Make it read-only
    command_text_widget.pack(side='left', padx=5)

    # Enable selection and copying
    command_text_widget.bind("<Button-1>", lambda event: command_text_widget.config(state='normal'))
    command_text_widget.bind("<FocusOut>", lambda event: command_text_widget.config(state='disabled'))

def load_button_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config['buttons']

def create_gitignore_file(language):
    gitignore_content = {
        "python": """
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class
# ... other Python entries ...
""",
        "node": """
# Logs
logs
*.log
npm-debug.log*
# ... other Node.js entries ...
""",
        "javascript": """
# Logs
logs
*.log
npm-debug.log*
# ... other JavaScript entries ...
"""
    }

    content = gitignore_content.get(language.lower(), "")
    if content:
        with open('.gitignore', 'w') as file:
            file.write(content)
        print(f".gitignore file created for {language}.")
    else:
        print(f"No .gitignore template found for {language}.")

def load_buttons_from_file(scrollable_frame, description_text):
    # Set the initial directory to the current working directory
    initial_dir = os.getcwd()
    
    file_path = filedialog.askopenfilename(
        initialdir=initial_dir,  # Start in the current working directory
        filetypes=[("JSON files", "*.json")]
    )
    
    if file_path:
        button_config = load_button_config(file_path)
        for widget in scrollable_frame.winfo_children():
            widget.destroy()  # Clear existing buttons
        for button in button_config:
            if button['type'] == 'shell':
                create_button(
                    scrollable_frame,
                    button['text'],
                    button['long_description'],
                    run_shell_command_in_frontmost_terminal,
                    args=[button['command']],
                    description_text=description_text
                )
            elif button['type'] == 'applescript':
                create_button(
                    scrollable_frame,
                    button['text'],
                    button['long_description'],
                    run_applescript,
                    args=[button['command']],
                    description_text=description_text
                )
            elif button['type'] == 'gitignore':
                create_button(
                    scrollable_frame,
                    button['text'],
                    button['long_description'],
                    create_gitignore_file,
                    args=[button['language']],
                    description_text=description_text
                )

def main():
    root = tk.Tk()
    root.title("Scrollable Command GUI")
    root.geometry("400x600")
    root.configure(bg="#1E1E1E")

    scrollable_frame = SFrame(root, bg="#1E1E1E", mousewheel=True)
    scrollable_frame.pack(expand=1, fill='both')

    # Text widget to display descriptions and commands
    description_text = tk.Text(
        root,
        height=2,
        bg="#1E1E1E",
        fg="#5A9",
        font=('Helvetica', 22),
        wrap='word',
        state='disabled'
    )
    description_text.pack(pady=5, fill='x', padx=10)

    # Add a Load button to load configurations
    load_button = tkm.Button(
        root,
        text="Load Config",
        command=lambda: load_buttons_from_file(scrollable_frame, description_text),
        bg="#2C2C2E",
        fg="white",
        font=('Helvetica', 22),
        borderless=1
    )
    load_button.pack(pady=5, fill='x', padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()
