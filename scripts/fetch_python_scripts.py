import requests
import os
from urllib.parse import urlparse

def fetch_files_from_directory(repo_url, local_dir):
    # Parse the GitHub repository URL
    parsed_url = urlparse(repo_url)
    path_parts = parsed_url.path.strip("/").split("/")

    if len(path_parts) < 5 or path_parts[2] != "tree":
        print("Invalid GitHub repository URL format.")
        return

    owner = path_parts[0]
    repo = path_parts[1]
    branch = path_parts[3]
    directory = "/".join(path_parts[4:])

    # GitHub API URL to list contents of the directory
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{directory}?ref={branch}"

    try:
        # Send a GET request to the GitHub API
        response = requests.get(api_url)
        response.raise_for_status()
        files = response.json()

        # Ensure the local directory exists
        os.makedirs(local_dir, exist_ok=True)

        # Download each file
        for file in files:
            if file['type'] == 'file':
                download_url = file['download_url']
                file_response = requests.get(download_url)
                file_response.raise_for_status()

                # Save the file locally
                with open(os.path.join(local_dir, file['name']), 'w') as f:
                    f.write(file_response.text)
                print(f"Downloaded: {file['name']}")
            elif file['type'] == 'dir':
                # Recursively fetch files from subdirectories
                subdirectory = file['path']
                fetch_files_from_directory(f"https://github.com/{owner}/{repo}/tree/{branch}/{subdirectory}", local_dir)

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch files: {e}")

if __name__ == "__main__":
    repo_url = "https://github.com/davedarch/gui-buttons/tree/main/scripts"
    local_dir = "scripts"
    fetch_files_from_directory(repo_url, local_dir)
