import requests

def fetch_github_repo(repo_url):
    response = requests.get(repo_url)
    if response.status_code == 200:
        print("Repository details:")
        print(response.json())
    else:
        print(f"Failed to fetch repository details. Status code: {response.status_code}")

if __name__ == "__main__":
    # URL of a public GitHub repository's API endpoint
    repo_url = "https://api.github.com/repos/psf/requests"
    fetch_github_repo(repo_url)
