# Git Mock

This script generates mock Git commits with random dates.

## Requirements

- Node.js 10.12.0 or higher
- npm

## Installation

1. Clone the repository:

```bash
git clone https://github.com/[username]/git-mock.git
```

2. Install the dependencies:

```bash
cd git-mock && npm install
```

## Usage

To generate 20 mock commits, run the following command:

```bash
node script.js 20
```

You can specify any number of commits as the argument. The script will create a file called `data.json` and commit it to the repository with a random date. The dates will be generated randomly within the past year.

## License

This project is licensed under the MIT License.
