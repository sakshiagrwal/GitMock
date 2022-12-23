import json
import random
from datetime import datetime, timedelta
from git import Repo

# File path for the data file
FILE_PATH = './data.json'

# Initialize a Repo object for the current directory
repo = Repo('./')

# Make 20 commits to the current branch
for i in range(20):
    # Generate a random date within the past year
    x = random.randint(0, 54)
    y = random.randint(0, 6)
    date = (datetime.now() - timedelta(days=365)) + \
        timedelta(days=1 + x * 7 + y)
    # Write the date to the data file
    data = {
        'date': date.strftime('%Y-%m-%d')
    }
    print(date.strftime('%Y-%m-%d'))
    with open(FILE_PATH, 'w') as f:
        json.dump(data, f)
    # Add the file to the staging area and commit it
    repo.git.add([FILE_PATH])
    repo.git.commit('-m', date.strftime('%Y-%m-%d'), '--date',
                    date.strftime('%Y-%m-%d %H:%M:%S'))

# Push the commits to the remote repository
repo.git.push()
