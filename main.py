import git
import random
from datetime import datetime, timedelta
from pathlib import Path
from random import choice


def generate_random_commit(file_path: Path, repo: git.Repo) -> None:
    """Generate a random commit to the current branch.

    The commit message will include a randomly selected emoji and the commit date. The file specified by `file_path` will be
    modified and added to the staging area. The commit will then be made to the current branch and pushed to the remote
    repository.

    Args:
        file_path: The path to the file that will be modified and committed.
        repo: The Repo object for the current directory.
    """
    # Generate a random date within the past year
    weeks = random.randint(0, 54)
    days = random.randint(0, 6)
    random_date = (datetime.now() - timedelta(days=365)) + \
        timedelta(days=1 + weeks * 7 + days)

    # Use the random.choice() function to select a random emoji from a hardcoded list
    emojis = ['😂', '❤', '💥', '❄️', '⛄', '⚡', '🌀', '😴', '🌌', '🚣', '⚓', '🚀', '😎', '🎉', '🎊', '🎈', '🔮', '📷', '📹', '🎥',
              '💻', '👾', '🎮', '💣']
    emoji = choice(emojis)

    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Modify the first line
    lines[0] = f'# Random Commit Generated on: {random_date.strftime("%d/%m/%y")}\n'

    # Write the updated content to the file
    with open(file_path, 'w') as file:
        file.write(''.join(lines))

    # Generate a commit message with the random emoji and commit date
    commit_message = f'{emoji} {random_date.strftime("%d/%m/%y")}'

    # Add the file to the staging area and commit it
    repo.git.add([file_path])
    repo.git.commit('-s', '-m', commit_message, '--date',
                    random_date.strftime('%Y-%m-%d %H:%M:%S'))


# Make only 1 commit
for _ in range(1):
    # Initialize a Repo object for the current directory
    repo = git.Repo('./')

    # File path for the data file
    file_path = Path('./README.md')

    generate_random_commit(file_path, repo)

    # Push the commits to the remote repository
    repo.git.push()
