import os
import git
import requests
import json
import shutil

GITLAB_URL = 'https://gitlab.example.com/api/v4'
GITLAB_TOKEN = 'glpat-S98rHkNz_CZxmsQzmJZG'
GITLAB_REPO_NAME = 'test-project'
LOCAL_DIR = '/path/to/local/directory'

def create_repository(name, description):
    headers = {
        'PRIVATE-TOKEN': GITLAB_TOKEN,
        'Content-Type': 'application/json'
    }
    payload = {
        'name': name,
        'description': description,
        'visibility': 'private'
    }
    response = requests.post(GITLAB_URL + '/projects', headers=headers, data=json.dumps(payload))
    if response.status_code == 201:
        print('Repository created:', response.json()['web_url'])
        return response.json()['web_url']
    else:
        print('Error creating repository:', response.json()['message'])
        return None

def push_directory_to_repository(repo_url, local_dir):
    # Clone the remote repository to a local directory
    local_repo_path = os.path.join(os.getcwd(), GITLAB_REPO_NAME)
    repo = git.Repo.clone_from(repo_url, local_repo_path)

    # Copy the local directory tree to the local repository directory
    shutil.copytree(local_dir, os.path.join(local_repo_path, 'my-directory'))

    # Add the files to the Git index
    repo.git.add(all=True)

    # Commit the changes
    repo.git.commit('-m', 'Added directory tree with files')

    # Push the changes to the remote repository
    repo.git.push()

    print('Directory tree with files pushed to GitLab repository.')

# Create the GitLab repository
git.refresh()
repo_url = create_repository(GITLAB_REPO_NAME, 'This is a test repository.')

if repo_url:
    # Push the local directory tree to the GitLab repository
    push_directory_to_repository(repo_url + '.git', LOCAL_DIR)
