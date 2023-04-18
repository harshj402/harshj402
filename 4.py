import gitlab
import os
import git

# Set up the GitLab connection
gl = gitlab.Gitlab('https://gitlab.com', private_token=os.environ.get('GITLAB_ACCESS_TOKEN'))

# Select the project you want to push to
project = gl.projects.get('your-project-id')

# Set up the Git repository
repo_path = '/path/to/your/repo'
repo = git.Repo.init(repo_path)

# Add the directory and its contents to the repository
dir_path = '/path/to/your/directory'
repo.git.add(dir_path)

# Commit the changes
commit_message = 'Add a new directory to the project'
repo.git.commit('-m', commit_message)

# Push the changes to GitLab
origin = repo.remote(name='origin')
origin.push()

print('Directory added and pushed to GitLab')
