import requests
import streamlit as st

def fetch_github_repo(repo_url):
    response = requests.get(repo_url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch repository details. Status code: {response.status_code}")
        return None

st.title("GitHub Repository Details")

# Input field for the GitHub repository API URL
repo_url = st.text_input("Enter GitHub Repository API URL:", "https://api.github.com/repos/psf/requests")

if st.button("Fetch Repository Details"):
    repo_details = fetch_github_repo(repo_url)
    if repo_details:
        st.write("Repository details:")
        st.json(repo_details)
