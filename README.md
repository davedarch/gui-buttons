# GUI Buttons

## Overview

**GUI Buttons** is a Python-based graphical user interface (GUI) application designed to execute various shell and AppleScript commands with ease. Built using Python's Tkinter library, the project offers a dynamic and extendable platform where users can load custom command configurations from JSON files and execute them via simple button clicks. This tool is particularly useful for automating repetitive tasks, managing Git repositories, handling virtual environments, and performing system operations seamlessly.

## Features

- **Load Command Configurations**: Dynamically load and parse JSON configuration files to create interactive buttons within the GUI.
- **Execute Shell Commands**: Run a wide range of shell commands directly from the GUI, including Git operations, system commands, and virtual environment management.
- **Execute AppleScript Commands**: Control macOS applications like Finder and Safari through AppleScript commands integrated into the GUI.
- **Tooltips**: Hover over buttons to view detailed descriptions of each command, enhancing usability and understanding.
- **Scrollable Interface**: Navigate through an extensive list of commands effortlessly using a scrollable frame.
- **Virtual Environment Management**: Easily create, activate, deactivate, and remove Python virtual environments.
- **Git Integration**: Perform Git operations such as add, commit, push, rename, and remove directly through the GUI buttons.
- **Customizable GUI Settings**: Tailor the appearance of the GUI including window dimensions, background colors, button styles, and text properties via a JSON settings file.

## Requirements

- **Python 3.11**
- **Tkinter**: Standard Python library for GUI applications.
- **tkmacosx**: Enhances button styling on macOS.
- **Requests**: For fetching `.gitignore` templates and other network operations.
- **Prompt Toolkit**: Used in scripts for enhanced command-line interactions.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/davedarch/gui-buttons.git
   cd gui-buttons
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the main GUI application:**
   ```bash
   python gui/gui_buttons.py
   ```

2. **Load Configuration:**
   - Click on the "Load Config" button to select a JSON file containing your command configurations.
   - Example JSON files are available in the `configs/` directory.

3. **Execute Commands:**
   - After loading a configuration, buttons corresponding to each command will appear.
   - Click on any button to execute its associated command.
   - Hover over buttons to view detailed descriptions of their functionalities.

## JSON Configuration

Commands are defined in JSON files located in the `configs/` directory. Each command follows the structure:

```json
{
  "text": "Button Text",
  "type": "shell or applescript",
  "command": ["command", "arguments"],
  "short_description": "Short description",
  "long_description": "Detailed description"
}
```

- **text**: The label displayed on the button.
- **type**: Specifies the type of command; either `shell` for shell commands or `applescript` for AppleScript commands.
- **command**: The command and its arguments to be executed.
- **short_description**: A brief description of the command.
- **long_description**: A detailed explanation of what the command does.

### Example JSON Files

- **`github_commands.json`**: Commands for creating repositories, managing branches, and other Git operations.
- **`basic_commands.json`**: Simple commands like listing directories (`ls -la`), showing the current date (`date`), and time.
- **`mixed_commands.json`**: A mix of shell and AppleScript commands for both terminal and macOS application control.
- **`terminal_commands.json`**: Advanced terminal commands for process management, file operations, and networking.
- **`venv_commands.json`**: Commands to create, activate, deactivate, and manage Python virtual environments.
- **`system_info_commands.json`**: Commands to display system information like disk usage, memory usage, and running processes.

## Code Structure
```gui-buttons/
├── configs/
│ ├── github_commands.json
│ ├── basic_commands.json
│ ├── mixed_commands.json
│ ├── terminal_commands.json
│ ├── venv_commands.json
│ └── system_info_commands.json
├── gui/
│ ├── gui_buttons.py
│ └── gui_settings.json
├── scripts/
│ ├── create_gitignore.py
│ ├── fetch_python_scripts.py
│ ├── git_add.py
│ ├── git_add_all.py
│ ├── git_commit_message.py
│ ├── git_mv.py
│ ├── git_rename.py
│ └── git_rm.py
├── .gitignore
├── requirements.txt
└── README.md```


### Detailed Description

- **`configs/`**: Contains various JSON configuration files defining commands for different purposes.
- **`gui/`**:
  - `gui_buttons.py`: Main GUI application script that loads configurations, creates buttons, and handles command execution.
  - `gui_settings.json`: JSON file to customize GUI appearance and behavior.
- **`scripts/`**: Python scripts that perform specific tasks, such as managing Git operations, fetching `.gitignore` templates, and handling virtual environments.
  - `create_gitignore.py`: Fetches and creates a `.gitignore` file for a specified language using GitHub's templates.
  - `fetch_python_scripts.py`: Downloads Python scripts from a GitHub repository.
  - `git_add.py`: Adds specified files to Git and commits the changes.
  - `git_add_all.py`: Adds all files to Git, commits with a timestamp, and pushes changes.
  - `git_commit_message.py`: Prompts the user for a commit message and performs the commit.
  - `git_mv.py`: Renames a file or directory in Git, stages, commits, and pushes the changes.
  - `git_rename.py`: Interactive renaming with path completions.
  - `git_rm.py`: Removes a file or directory from Git, commits, and pushes the changes.
- **`.gitignore`**: Specifies files and directories to be ignored by Git.
- **`requirements.txt`**: Lists the required Python packages. *(Ensure to update with actual dependencies)*

## Contributing

Contributions are welcome! If you have suggestions for new features, improvements, or bug fixes, please fork the repository and submit a pull request. Ensure your code follows the project's coding standards and includes necessary documentation.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- Special thanks to the contributors of the [`tkmacosx`](https://github.com/TomSchimansky/tkmacosx) library for providing enhanced button styling on macOS.
- Inspired by various Python GUI projects and command automation tools.