import gitlab
import os

# Set up the GitLab connection
gl = gitlab.Gitlab('https://gitlab.com', private_token=os.environ.get('GITLAB_ACCESS_TOKEN'))

# Select the project you want to push to
project = gl.projects.get('your-project-id')

# Add a file to the project
file_path = 'path/to/your/file'
file_name = 'your_file_name.txt'
file_content = 'This is the content of your file'
commit_message = 'Add a new file to the project'

# Create a new file
new_file = project.files.create({'file_path': file_path, 'branch': 'main', 'content': file_content, 'commit_message': commit_message})

print('File created:', new_file['file_name'])
