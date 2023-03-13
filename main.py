import os
import random
from datetime import datetime, timedelta
from git import Repo, Actor

# Get the current user's profile directory
userprofile = os.environ.get('USERPROFILE')

# Specify the local and remote repository paths
local_repo_path = os.path.join(userprofile, 'Desktop', 'TestRepo')
remote_repo_url = "https://github.com/username/repo.git"

# Initialize a new repository if the directory doesn't exist
if not os.path.exists(local_repo_path):
    os.makedirs(local_repo_path)
    repo = Repo.init(local_repo_path)
else:
    # Otherwise, open the existing repository
    repo = Repo(local_repo_path)

# Specify the author and committer information
author = Actor("chrisl7", "wandersonrodriguesf1@gmail.com")
committer = Actor("parixshit", "parikshit.tunlr@slmail.me")

# Generate random commit dates
start_date = datetime(2020, 1, 1)
end_date = datetime.now()
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
commit_dates = [start_date + timedelta(days=random.randrange(days_between_dates)) for i in range(10)]

# Loop through the commit dates and make random commits
for commit_date in commit_dates:
    # Update the README file
    readme_file = os.path.join(local_repo_path, "README.md")
    with open(readme_file, "a") as f:
        f.write(f"\n\nRandom commit on {commit_date}")
    
    # Add the README file to the Git index
    repo.index.add([readme_file])
    
    # Create the commit
    commit_message = f"Random commit on {commit_date}"
    commit = repo.index.commit(commit_message, author=author, committer=committer, author_date=commit_date, commit_date=commit_date)

# Push the commits to the remote repository
origin = repo.remote(name="origin")
origin.push()
