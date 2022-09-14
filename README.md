# Git History Generator

This repository contains a script for generating random Git commits. The script modifies the **last** line of the `README.md` file in the repository and adds the changes to the Git history with a random date and a randomly chosen emoji as the commit message.

## Usage

1. Install the required dependencies: `pip install gitpython emoji tqdm`
2. Run the script: `python main.py ./ 5` (Change the value of `5` to the desired number of commits)

## Manual Trigger with GitHub Actions

You can also use [GitHub Actions](https://github.com/features/actions) to generate commits. The workflow is defined in the `.github/workflows/main.yml` file.

To trigger the workflow manually, navigate to the "Actions" tab in your GitHub repository and click on the "Run workflow" button. Then, enter the desired number of commits in the "commits" input field, or leave it as "5" to use the default value.

#

<sub><strong><em>Random commit date: 14-09-2022 11:29:26 AM</em></strong></sub>