import os
import random
from datetime import datetime, timedelta
from git import Repo, Actor

# Get the current user's profile directory
userprofile = os.environ.get('USERPROFILE')

# Specify the local repository path
local_repo_path = os.path.join(userprofile, 'Desktop', 'TestRepo')

# Initialize a new repository in the local_repo_path directory
repo = Repo.init(local_repo_path)

# Specify the remote repository URL
remote_repo_url = "https://github.com/username/repo.git"

# Add the remote repository as a remote named "origin"
origin = repo.create_remote('origin', remote_repo_url)

# Specify the author and committer information
author = Actor("chrisl7", "wandersonrodriguesf1@gmail.com")
committer = Actor("parixshit", "parikshit.tunlr@slmail.me")

# Create a README file with some initial content
readme_file = os.path.join(local_repo_path, "README.md")
with open(readme_file, "w") as f:
    f.write("Initial commit")

# Add the README file to the Git index
repo.index.add([readme_file])

# Create an initial commit with the README file
commit_message = "Initial commit"
commit = repo.index.commit(commit_message, author=author, committer=committer)

# Generate random commit dates
start_date = datetime(2020, 1, 1)
end_date = datetime.now()
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
commit_dates = [start_date + timedelta(days=random.randrange(days_between_dates)) for i in range(10)]

# Loop through the commit dates and make random commits
for commit_date in commit_dates:
    # Update the README file
    with open(readme_file, "a") as f:
        f.write(f"\n\nRandom commit on {commit_date}")
    
    # Add the README file to the Git index
    repo.index.add([readme_file])
    
    # Create the commit
    commit_message = f"Random commit on {commit_date}"
    commit = repo.index.commit(commit_message, author=author, committer=committer, author_date=commit_date, commit_date=commit_date)

# Push the commits to the remote repository
origin.push()
