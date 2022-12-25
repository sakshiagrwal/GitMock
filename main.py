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

import json
import random
from datetime import datetime, timedelta
from git import GitCommandError, Repo


def generate_random_date():
    """Generate a random date within the past year."""
    week_index = random.randint(0, 52)
    day_index = random.randint(0, 6)
    date = (datetime.now() - timedelta(days=365)) + \
        timedelta(days=1 + week_index * 7 + day_index)
    return date


def write_date_to_file(date, file_path):
    """Write the given date to the specified data file and print it to the log."""
    data = {
        'date': date.strftime('%Y-%m-%d')
    }
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f)
    except IOError as e:
        print(f'Error writing to file: {e}')
    # Print the date to the log
    print(date.strftime('%Y-%m-%d'))


# File path for the data file
FILE_PATH = './data.json'

# Initialize a Repo object for the current directory
repo = Repo('./')

# Make 1000 commits to the current branch
for i in range(1000):
    # Generate a random date within the past year
    date = generate_random_date()
    # Write the date to the data file
    write_date_to_file(date, FILE_PATH)
    # Add the file to the staging area and commit it
    repo.git.add([FILE_PATH])
    repo.git.commit('-m', date.strftime('%Y-%m-%d'), '--date',
                    date.strftime('%Y-%m-%d %H:%M:%S'))

    # Try to push the commits to the remote repository
    try:
        repo.git.push()
    except GitCommandError as e:
        # Print the error message and exit the loop
        print(f'Error pushing commits: {e}')
        break
