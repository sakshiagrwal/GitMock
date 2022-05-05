# Random Commit Generated on: 05 May 2022

A simple script that generates random commits to a git repository.

## Usage

1. Install the required dependencies: `pip install gitpython emoji`
2. Run the script: `python main.py`

## Customization

- You can change the number of commits made by modifying the `range()` function in the script
- You can change the file that is being committed by modifying the file path in the `write_date_to_readme()` and `repo.git.add()` functions
- You can change the emoji list by modifying the `emoji_list` variable

## Note

- The script uses the current date and time as the starting point for generating random dates.
- Make sure to use the correct file path for the repository and the file you want to commit.
