const jsonfile = require("jsonfile");
const simpleGit = require("simple-git");
const moment = require("moment");
const crypto = require("crypto");
const FILE_PATH = "./data.json";

async function makeCommit(n) {
  if (n === 0) return simpleGit().push();

  const x = Math.floor(crypto.randomBytes(4).readUInt32BE() % 55);
  const y = Math.floor(crypto.randomBytes(4).readUInt32BE() % 7);
  const DATE = moment()
    .subtract(1, "y")
    .add(1, "d")
    .add(x, "w")
    .add(y, "d")
    .format();
  const data = {
    date: DATE,
  };
  console.log(DATE);
  try {
    await jsonfile.writeFile(FILE_PATH, data);
    await simpleGit().add([FILE_PATH]).commit(`${DATE}`, { "--date": DATE });
    makeCommit(--n);
  } catch (error) {
    console.error(`Error making commit: ${error}`);
  }
}

makeCommit(2000);
