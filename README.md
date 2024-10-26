# GUI Buttons

## Overview

This project provides a graphical user interface (GUI) for executing various shell and AppleScript commands. It is built using Python's Tkinter library and is designed to be easily extendable with new commands. The GUI allows users to load command configurations from JSON files and execute them with a simple button click.

## Features

- **Load Command Configurations**: Load command configurations from JSON files to dynamically create buttons in the GUI.
- **Execute Shell Commands**: Run shell commands directly from the GUI.
- **Execute AppleScript Commands**: Run AppleScript commands on macOS to control applications like Finder and Safari.
- **Tooltips**: Hover over buttons to see detailed descriptions of what each command does.
- **Scrollable Interface**: Easily navigate through a list of commands using a scrollable frame.

## Requirements

- Python 3.11
- Tkinter
- tkmacosx (for enhanced button styling on macOS)
- Requests library (for fetching .gitignore templates)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gui-buttons.git
   cd gui-buttons
   ```

2. Create and activate a virtual environment:
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main GUI application:
   ```bash
   python load_json_gui.py
   ```

2. Click "Load Config" to select a JSON file containing command configurations. Example JSON files are provided in the repository.

3. Click on any button to execute the associated command. Hover over buttons to see detailed descriptions.

## JSON Configuration

Commands are defined in JSON files. Each command has the following structure:
  ```json
{
  "text": "Button Text",
  "type": "shell or applescript",
  "command": ["command", "arguments"],
  "short_description": "Short description",
  "long_description": "Detailed description"
}
  ```

## Example JSON Files

- `github_commands.json`: Contains commands for Git and GitHub operations.
- `basic_commands.json`: Contains basic shell commands like listing directories and showing the date.
- `mixed_commands.json`: Contains a mix of shell and AppleScript commands.

## Code Structure

- `load_json_gui.py`: Main application file for the GUI.
- `create_gitignore.py`: Script to fetch and create a `.gitignore` file for a specified language.
- `get_commit_message.py`: Script to prompt for a commit message and execute a git commit.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- Thanks to the contributors of the `tkmacosx` library for providing enhanced button styling on macOS.
