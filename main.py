# Copyright (C) 2022  Sakshi Aggarwal

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import random
import logging
from datetime import datetime, timedelta
from git import GitCommandError
from git.repo import Repo


# Set up a logger with the desired log level and format
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

# Create a file handler and add it to the logger
file_handler = logging.FileHandler('main.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# You can also add a stream handler to print log messages to the console
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


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
    date = (datetime.now() - timedelta(days=365)) + \
        timedelta(weeks=week_index, days=day_index)
    return date


def write_date_to_readme(date):
    """
    Modify the first line of the README.md file by adding the commit date.

    Args:
        date (datetime): The commit date to be added to the file.
    """
    # Read the contents of the README.md file
    try:
        with open('./README.md', 'r') as f:
            lines = f.readlines()
    except IOError as e:
        logger.error(f'Error reading README.md file: {e}')
        return

    # Modify the first line (add commit date after this # Random Commit Generated on:)
    lines[0] = f'# Random Commit Generated on: {date.strftime("%d %B %Y")}\n'
    # Write the modified contents back to the file
    try:
        with open('./README.md', 'w') as f:
            f.writelines(lines)
    except IOError as e:
        logger.error(f'Error writing to README.md file: {e}')
        return


def read_emojis_from_file(filepath):
    logger.debug(f'Reading emojis from file {filepath}')
    try:
        # Open the emojis.txt file and read the emojis into the list
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                logger.debug(f'Yielding emoji {line.strip()}')
                yield line.strip()
    except IOError as e:
        logger.error(f'Error reading emojis file {filepath}: {e}')


# Initialize a generator to read the emojis from the emojis.txt file
try:
    emoji_generator = read_emojis_from_file('emojis.txt')
except IOError as e:
    logger.error(f'Error initializing emoji generator: {e}')
    exit(1)

# Initialize a Repo object for the current directory
try:
    repo = Repo('./')
except Exception as e:
    logger.error(f'Error initializing Repo object: {e}')
    exit(1)

# Make 1100 commits to the current branch
for i in range(1100):
    # Re-initialize the generator at the beginning of each iteration
    emoji_generator = read_emojis_from_file('emojis.txt')

    # Generate a random date within the past year
    try:
        date = generate_random_date()
    except Exception as e:
        logger.error(f'Error generating random date: {e}')
        continue

        # Modify the README.md file with the commit date
    try:
        write_date_to_readme(date)
    except Exception as e:
        logger.error(f'Error modifying README.md file: {e}')
        continue

    # Add the file to the staging area and commit it
    repo.git.add(['./README.md', './main.log'])
    # Log the date
    logger.info(date)
    try:
        # Select the next emoji from the generator
        emoji = random.choice(list(emoji_generator))
    except StopIteration:
        # Reset the generator if it has been exhausted
        try:
            emoji_generator = read_emojis_from_file('emojis.txt')
        except IOError as e:
            logger.error(f'Error resetting emoji generator: {e}')
            continue
        emoji = random.choice(list(emoji_generator))
    except Exception as e:
        logger.error(f'Error selecting emoji: {e}')
        continue

    # Set the commit message to include the emoji
    try:
        repo.git.commit('-a', '-s', '-m', f'{emoji} {date.strftime("%d-%m-%Y %H:%M:%S")}',
                        '--date', date.strftime('%d-%m-%Y %H:%M:%S'))
    except Exception as e:
        logger.error(f'Error committing changes: {e}')
        continue

    # Try to push the commits to the remote repository
    try:
        repo.git.push('origin', 'py')
    except GitCommandError as e:
        # Log the error message and continue making commits
        logger.error(f'Error pushing commits: {e}')
