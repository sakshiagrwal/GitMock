import random
import emoji
import emot
from datetime import datetime, timedelta
from git import Repo

# File path for the data file
FILE_PATH = './README.md'

# Initialize a Repo object for the current directory
repo = Repo('./')

# Make only 1 commit to the current branch
for i in range(1):
    # Generate a random date within the past year
    x = random.randint(0, 54)
    y = random.randint(0, 6)
    date = (datetime.now() - timedelta(days=365)) + \
        timedelta(days=1 + x * 7 + y)

    # Use the random.choice() function to select a random emoji from a hardcoded list
    emojis_list = ['😂', '❤', '💥', '❄️', '⛄', '⚡', '🌀', '😴', '🌌', '🚣', '⚓', '🚀',
                   '😎', '🎉', '🎊', '🎈', '🔮', '📷', '📹', '🎥', '💻', '👾', '🎮', '💣']
    emoji = random.choice(emojis_list)

    # Read the contents of the README.md file
    with open(FILE_PATH, 'r') as f:
        lines = f.readlines()
    # Modify the first line
    lines[0] = '# Random Commit Generated on: {}\n'.format(
        date.strftime("%d/%m/%y"))
    # Write the updated content to the file
    with open(FILE_PATH, 'w') as f:
        f.write(''.join(lines))
    # Generate a commit message with the random emoji and commit date
    commit_message = '{} {}'.format(emoji, date.strftime("%d/%m/%y"))
    # Add the file to the staging area and commit it
    repo.git.add([FILE_PATH])
    repo.git.commit('-s', '-m', commit_message, '--date',
                    date.strftime('%Y-%m-%d %H:%M:%S'))

# Push the commits to the remote repository
repo.git.push()
