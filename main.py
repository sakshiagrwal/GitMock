"""
Module for parsing command-line arguments.
"""
import argparse
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make random Git commits.")
    parser.add_argument("repo_path", type=str, help="The path to the Git repository.")
    parser.add_argument("num_commits", type=int, help="The number of commits to make.")
    args = parser.parse_args()

    # Initialize the Repo object
    repo = Repo(args.repo_path)

    # Create a list of single emojis
    emoji_list = [c for c in emoji.EMOJI_DATA if len(c) == 1]

    for i in range(args.num_commits):
        # Generate a random date within the past year
        random_date = generate_random_date()

        # Open the README.md file for reading and writing
        with open("./README.md", "r+", encoding="utf-8") as f:
            lines = f.readlines()

            # Modify the line 19 of the README.md file with the commit date
            with open("./README.md", "r", encoding="utf-8") as f:
                lines = f.readlines()

            lines[18] = f'##### _{random_date.strftime("%d %B %Y")}_'

            with open("./README.md", "w", encoding="utf-8") as f:
                f.writelines(lines)

            # Add the file to the staging area and commit it
            repo.git.add(["./README.md"])
            print(random_date)

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
