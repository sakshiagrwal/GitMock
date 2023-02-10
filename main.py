"""
Making Git commits
"""

import argparse
import random
from datetime import datetime, timedelta
import os
import subprocess
import emoji
from tqdm import tqdm


def generate_random_date():
    """
    Generate a random date within the past year.
    Returns:
        datetime: A randomly generated date within the past year.
    """
    # Generate a random float within the range [0, 52]
    week_index = random.randint(0, 52)
    # Generate a random float within the range [0, 6]
    day_index = random.randint(0, 6)

    # Calculate the date by adding the appropriate number of weeks and days to the current date
    date = (datetime.now() - timedelta(days=365)) + timedelta(
        weeks=week_index, days=day_index
    )
    return date


def main(repo_path, num_commits):
    """
    The main function that performs the Git commits.

    :param repo_path: The path to the Git repository.
    :param num_commits: The number of commits to make.
    :return: None
    """
    # Create a list of single emojis
    emoji_list = [c for c in emoji.EMOJI_DATA if len(c) == 1]
    # Join the repository path and the README file name
    readme_file = os.path.join(repo_path, "README.md")

    # Change the current working directory to the repository path
    os.chdir(repo_path)

    # Read the lines of the README file
    with open(readme_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Get the index of the last line
    last_line_index = len(lines) - 1

    # Create a progress bar using tqdm
    with tqdm(total=num_commits) as pbar:
        # Loop to make the specified number of commits
        for _ in range(num_commits):
            # Generate a random date and emoji
            random_date = generate_random_date()
            random_emoji = random.choice(emoji_list)

            # Update the last line in the lines list
            lines[last_line_index] = f"{random_date.strftime('%d %B %Y')}\n"

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
                        f"{random_emoji} {random_date.strftime('%d-%m-%Y %H:%M:%S')}",
                        "--date",
                        random_date.strftime("%d-%m-%Y %H:%M:%S"),
                    ],
                    check=True,
                )
            except subprocess.CalledProcessError as exc:
                print(f"Error committing changes: {exc}")
                continue

            # Update the progress bar
            pbar.update(1)

    # Push the commits to the remote repository
    os.system("git push origin py")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make random Git commits.")
    parser.add_argument("repo_path", type=str, help="The path to the Git repository.")
    parser.add_argument("num_commits", type=int, help="The number of commits to make.")
    args = parser.parse_args()
    main(args.repo_path, args.num_commits)
