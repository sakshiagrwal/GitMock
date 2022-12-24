const jsonfile = require("jsonfile");
const simpleGit = require("simple-git");
const moment = require("moment");
const crypto = require("crypto");
const FILE_PATH = "./data.json";

/**
 * Generates mock Git commits with random dates.
 * @param {number} n - The number of commits to generate.
 */
async function makeCommit(n) {
  // If no more commits are needed, push to the repository
  if (n === 0) {
    try {
      await simpleGit().push();
    } catch (error) {
      console.error(`Error pushing commits: ${error}`);
    }
    return;
  }

  // Generate random values for the number of weeks and days to add to the date
  const x = Math.floor(crypto.randomBytes(4).readUInt32BE() % 55);
  const y = Math.floor(crypto.randomBytes(4).readUInt32BE() % 7);

  // Generate a random date within the past year
  const DATE = moment()
    .subtract(1, "y")
    .add(1, "d")
    .add(x, "w")
    .add(y, "d")
    .format();

  // Write the date to a JSON file
  const data = {
    date: DATE,
  };
  console.log(DATE);
  try {
    await jsonfile.writeFile(FILE_PATH, data);
    // Add and commit the file with the random date
    await simpleGit().add([FILE_PATH]).commit(`${DATE}`, { "--date": DATE });
    // Recursively generate more commits
    makeCommit(--n);
  } catch (error) {
    console.error(`Error making commit: ${error}`);
  }
}

// Generate 20 mock commits
makeCommit(20);
