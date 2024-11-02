import requests
import os

def fetch_gitignore_template(language):
    # Base URL for the GitHub gitignore repository
    base_url = "https://raw.githubusercontent.com/github/gitignore/main/"
    
    # Construct the URL for the specific language
    url = f"{base_url}{language.capitalize()}.gitignore"
    
    try:
        # Send a GET request to fetch the .gitignore template
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Write the content to a .gitignore file in the current directory
        with open('.gitignore', 'w') as file:
            file.write(response.text)
        
        print(f".gitignore file created for {language}.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch .gitignore for {language}: {e}")

def main():
    # Ask the user for the language
    language = input("Enter the language for the .gitignore file (e.g., Python, Node, JavaScript): ").strip()
    
    # Fetch and create the .gitignore file
    fetch_gitignore_template(language)

if __name__ == "__main__":
    main()

