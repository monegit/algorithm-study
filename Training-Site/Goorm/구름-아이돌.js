// Run by Node.js
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let N = 0;
  let S = [];
  let counter = 0;
  let result = [];

  for await (const line of rl) {
    if (N === 0) {
      N = line;
    } else {
      S = line.split(" ").map(Number);
      let ranked_S = [...S].sort((s1, s2) => s2 - s1).slice(0, 3);

      // console.log(S)

      for (let i = 0; i < ranked_S.length; i++) {
        result.push(S.indexOf(ranked_S[i]) + 1);
      }

      console.log(result.join(" "));
    }

    counter++;
    if (counter >= 2) rl.close();
  }

  process.exit();
})();
