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
from datetime import datetime, timedelta
from git import GitCommandError, Repo


def generate_random_date():
    """
    Generate a random date within the past year.

    Returns:
        datetime: A randomly generated date within the past year.
    """
    week_index = random.randint(0, 52)
    day_index = random.randint(0, 6)
    date = (datetime.now() - timedelta(days=365)) + \
        timedelta(days=1 + week_index * 7 + day_index)
    return date


def write_date_to_readme(date):
    """
    Modify the first line of the README.md file by adding the commit date.

    Args:
        date (datetime): The commit date to be added to the file.
    """
    # Read the contents of the README.md file
    with open('./README.md', 'r') as f:
        lines = f.readlines()
    # Modify the first line (add commit date after this # Random Commit Generated on:)
    lines[0] = f'# Random Commit Generated on: {date.strftime("%Y-%m-%d")}\n'
    # Write the modified contents back to the file
    with open('./README.md', 'w') as f:
        f.writelines(lines)


# Initialize a Repo object for the current directory
repo = Repo('./')

# Make 1000 commits to the current branch
for i in range(1000):
    # Generate a random date within the past year
    date = generate_random_date()
    # Modify the README.md file with the commit date
    write_date_to_readme(date)
    # Add the file to the staging area and commit it
    repo.git.add(['./README.md'])
    repo.git.commit('-s', '-m', date.strftime('%Y-%m-%d'), '--date',
                    date.strftime('%Y-%m-%d %H:%M:%S'))

    # Try to push the commits to the remote repository
    try:
        repo.git.push()
    except GitCommandError as e:
        # Print the error message and exit the loop
        print(f'Error pushing commits: {e}')
        break
