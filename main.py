import random
from datetime import datetime, timedelta
import emoji
from git.repo import Repo


def generate_random_date():
    """
    Generate a random date within the past year.

    Returns:
        datetime: A randomly generated date within the past year.
    """
    # Generate a random float within the range [0, 52]
    week_index = random.uniform(0, 52)
    # Generate a random float within the range [0, 6]
    day_index = random.uniform(0, 6)

    # Calculate the date by adding the appropriate number of weeks and days to the current date
    date = (datetime.now() - timedelta(days=365)) + timedelta(
        weeks=week_index, days=day_index
    )
    return date


def write_date_to_readme(date):
    """
    Modify the first line of the README.md file by adding the commit date.

    Args:
        date (datetime): The commit date to be added to the file.
    """
    # Read the contents of the README.md file
    with open("./README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Modify the first line (add commit date after this # Random Commit Generated on:)
    lines[0] = f'# Random Commit Generated on: {date.strftime("%d %B %Y")}\n'
    # Write the modified contents back to the file
    with open("./README.md", "w", encoding="utf-8") as f:
        f.writelines(lines)


# Initialize the Repo object
repo = Repo("./")

# Create a list of emojis
emoji_list = [c for c in emoji.EMOJI_DATA]

# Make 5 commits to the current branch
for i in range(5):
    # Generate a random date within the past year
    random_date = generate_random_date()

    # Modify the README.md file with the commit date
    write_date_to_readme(random_date)

    # Add the file to the staging area and commit it
    print(random_date)
    repo.git.add(["./README.md"])

    # Set the commit message to include the random emoji
    random_emoji = random.choice(emoji_list)
    repo.git.commit(
        "-a",
        "-s",
        "-m",
        f'{random_emoji} {random_date.strftime("%d-%m-%Y %H:%M:%S")}',
        "--date",
        random_date.strftime("%d-%m-%Y %H:%M:%S"),
    )

    # Push the commits to the remote repository
    repo.git.push("origin", "py")
