"""
Making Git commits
"""

import argparse
import random
from datetime import datetime, timedelta
import os
import subprocess
import emoji


def generate_random_date():
    """
    Generate a random datetime within the past year.
    Returns:
        datetime: A randomly generated datetime within the past year.
    """
    # Generate a random number of seconds within the past year (31,536,000 seconds)
    random_seconds = random.randint(0, 31536000)
    # Generate a random number of microseconds within one second (1,000,000 microseconds)
    random_microseconds = random.randint(0, 1000000)

    # Calculate the datetime by subtracting the appropriate number of seconds and microseconds from the current datetime
    date = datetime.now() - timedelta(
        seconds=random_seconds, microseconds=random_microseconds
    )
    return date


def main(repo_path, num_commits):
    """
    The main function that performs the Git commits.

    :param repo_path: The path to the Git repository.
    :param num_commits: The number of commits to make.
    :return: None
    """
    # Create a list of supported single emojis
    emoji_list = [c for c in emoji.EMOJI_DATA if len(c) == 1 and emoji.emoji_count(c) == 1]
    # Join the repository path and the README file name
    readme_file = repo_path + "/README.md"

    # Change the current working directory to the repository path
    os.chdir(repo_path)

    # Read the lines of the README file
    with open(readme_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Get the index of the last line
    last_line_index = len(lines) - 1

    # Loop to make the specified number of commits
    for _ in range(num_commits):
        # Generate a random date and emoji
        random_date = generate_random_date()
        random_emoji = random.choice(emoji_list)

        # Update the last line in the lines list
        lines[
            last_line_index
        ] = f"<sub><strong><em>Random commit date: {random_date.strftime('%d-%m-%Y %I:%M:%S %p')}</em></strong></sub>"

        # Write the lines back to the README file
        with open(readme_file, "w", encoding="utf-8") as file:
            file.writelines(lines)

        # Add the README file to the Git index
        subprocess.run(["git", "add", readme_file], check=True)

        # Create the commit with the commit message and random date
        try:
            subprocess.run(
                [
                    "git",
                    "commit",
                    "-a",
                    "-s",
                    "-m",
                    f"{random_emoji} {random_date.strftime('%d-%m-%Y %I:%M:%S %p')}",
                    "--date",
                    random_date.strftime("%d-%m-%Y %H:%M:%S"),
                ],
            )
        except subprocess.CalledProcessError as exc:
            print(f"Error committing changes: {exc}")
            continue

    # Push the commits to the remote repository
    os.system("git push origin py")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make random Git commits.")
    parser.add_argument("repo_path", type=str, help="The path to the Git repository.")
    parser.add_argument("num_commits", type=int, help="The number of commits to make.")
    args = parser.parse_args()
    main(args.repo_path, args.num_commits)
