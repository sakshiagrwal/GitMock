const jsonfile = require("jsonfile");
const simpleGit = require("simple-git");
const moment = require("moment");
const random = require("random-js");
const FILE_PATH = "./data.json";

const makeCommit = (n) => {
  if (n === 0) return simpleGit().push();
  const x = Math.floor(Math.random() * (54 + 1));
  const y = Math.floor(Math.random() * (6 + 1));
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
  jsonfile.writeFile(FILE_PATH, data, () => {
    simpleGit()
      .add([FILE_PATH])
      .commit(DATE, { "--date": DATE }, makeCommit.bind(this, --n));
  });
};
makeCommit(2000);
