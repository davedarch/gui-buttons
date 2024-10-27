import tkinter as tk
from tkinter import ttk, filedialog, simpledialog, messagebox
import subprocess
import platform
from functools import partial
import tkmacosx as tkm
from tkmacosx import SFrame, Button
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
    root = tk.Tk()
    root.withdraw()
    commit_message = simpledialog.askstring("Commit Message", "Enter your commit message:")
    root.destroy()
    return commit_message

def run_shell_command_in_frontmost_terminal(command):
    try:
        if 'git commit -m <message>' in " ".join(command):
            commit_message = get_commit_message()
            if not commit_message:
                messagebox.showwarning("Commit Cancelled", "No commit message provided. Commit cancelled.")
                return
            command = [part.replace('<message>', commit_message) for part in command]
        
        full_command = " ".join(command)
        
        if '`basename "$PWD"`' in full_command:
            folder_name = os.path.basename(os.getcwd())
            full_command = full_command.replace('`basename "$PWD"`', folder_name)
        
        full_command_escaped = full_command.replace('"', '\\"')
        
        applescript_command = f'''
        tell application "Terminal"
            activate
            do script "{full_command_escaped}" in front window
        end tell
        '''
        
        subprocess.run(['osascript', '-e', applescript_command], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Shell command failed: {e}")

def create_button(parent, text, long_description, command, args=(), gui_settings=None, description_text=None):
    if gui_settings is None:
        gui_settings = {}

    bg_color = gui_settings.get("button", {}).get("background_color", "#2C2C2E")
    fg_color = gui_settings.get("button", {}).get("text_color", "white")
    font_size = gui_settings.get("button", {}).get("font_size", 22)
    font_family = gui_settings.get("button", {}).get("font_family", "Helvetica")
    borderless = gui_settings.get("button", {}).get("borderless", True)
    padding_x = gui_settings.get("button", {}).get("padding", {}).get("x", 10)
    padding_y = gui_settings.get("button", {}).get("padding", {}).get("y", 5)

    frame = tk.Frame(parent, bg=bg_color)
    frame.pack(pady=2, fill='x', padx=padding_x)

    btn = tkm.Button(
        frame, 
        text=text, 
        command=partial(command, *args), 
        bg=bg_color, 
        fg=fg_color, 
        font=(font_family, font_size),
        borderless=borderless
    )
    btn.pack(side='left', padx=padding_x, pady=padding_y)

    Tooltip(btn, long_description=long_description, text_widget=description_text)

    command_text = " ".join(args[0]) if isinstance(args[0], list) else args[0]
    command_text_widget = tk.Text(
        frame,
        height=1,
        bg=gui_settings.get("command_text", {}).get("background_color", "#2C2C2E"),
        fg=gui_settings.get("command_text", {}).get("text_color", "#5A9"),
        font=(gui_settings.get("command_text", {}).get("font_family", "Helvetica"),
              gui_settings.get("command_text", {}).get("font_size", 22)),
        wrap='none',
        borderwidth=0,
        highlightthickness=0
    )
    command_text_widget.insert(tk.END, command_text)
    command_text_widget.config(state='disabled')
    command_text_widget.pack(side='left', padx=padding_x)

    command_text_widget.bind("<Button-1>", lambda event: command_text_widget.config(state='normal'))
    command_text_widget.bind("<FocusOut>", lambda event: command_text_widget.config(state='disabled'))

def load_button_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config['buttons']

def load_gui_settings(file_path):
    with open(file_path, 'r') as file:
        settings = json.load(file)
    return settings

def load_buttons_from_file(scrollable_frame, description_text, gui_settings):
    initial_dir = os.getcwd()
    
    file_path = filedialog.askopenfilename(
        initialdir=initial_dir,
        filetypes=[("JSON files", "*.json")]
    )
    
    if file_path:
        button_config = load_button_config(file_path)
        for widget in scrollable_frame.winfo_children():
            widget.destroy()
        for button in button_config:
            if button['type'] == 'shell':
                create_button(
                    scrollable_frame,
                    button['text'],
                    button['long_description'],
                    run_shell_command_in_frontmost_terminal,
                    args=[button['command']],
                    gui_settings=gui_settings,
                    description_text=description_text
                )
            elif button['type'] == 'applescript':
                create_button(
                    scrollable_frame,
                    button['text'],
                    button['long_description'],
                    run_applescript,
                    args=[button['command']],
                    gui_settings=gui_settings,
                    description_text=description_text
                )
        
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        root.title(file_name.replace("_", " "))

def run_applescript(script):
    """Executes an AppleScript command."""
    try:
        subprocess.run(['osascript', '-e', script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running AppleScript: {e}")

def main():
    global root
    root = tk.Tk()

    gui_settings = load_gui_settings("gui_settings.json")

    root.title(gui_settings.get("window", {}).get("title", "Scrollable Command GUI"))
    root.geometry(f"{gui_settings.get('window', {}).get('width', 400)}x{gui_settings.get('window', {}).get('height', 600)}")
    root.configure(bg=gui_settings.get("window", {}).get("background_color", "#1E1E1E"))

    scrollable_frame = SFrame(
        root,
        bg=gui_settings.get("scrollable_frame", {}).get("background_color", "#1E1E1E"),
        mousewheel=gui_settings.get("scrollable_frame", {}).get("mousewheel", True)
    )
    scrollable_frame.pack(expand=1, fill='both')

    description_text = tk.Text(
        root,
        height=gui_settings.get("text_box", {}).get("height", 2),
        bg=gui_settings.get("text_box", {}).get("background_color", "#1E1E1E"),
        fg=gui_settings.get("text_box", {}).get("text_color", "#5A9"),
        font=(gui_settings.get("text_box", {}).get("font_family", "Helvetica"),
              gui_settings.get("text_box", {}).get("font_size", 22)),
        wrap=gui_settings.get("text_box", {}).get("wrap", "word"),
        state='disabled'
    )
    description_text.pack(pady=gui_settings.get("text_box", {}).get("padding", {}).get("y", 5),
                          fill='x',
                          padx=gui_settings.get("text_box", {}).get("padding", {}).get("x", 10))

    load_button = Button(
        root,
        text="Load Config",
        command=lambda: load_buttons_from_file(scrollable_frame, description_text, gui_settings),
        bg=gui_settings.get("button", {}).get("background_color", "#2C2C2E"),
        fg=gui_settings.get("button", {}).get("text_color", "white"),
        font=(gui_settings.get("button", {}).get("font_family", "Helvetica"),
              gui_settings.get("button", {}).get("font_size", 22)),
        borderless=gui_settings.get("button", {}).get("borderless", True)
    )
    load_button.pack(pady=gui_settings.get("button", {}).get("padding", {}).get("y", 5),
                     fill='x',
                     padx=gui_settings.get("button", {}).get("padding", {}).get("x", 10))

    scrollable_frame.config(avoidmousewheel=(description_text,))

    root.mainloop()

if __name__ == "__main__":
    main()
