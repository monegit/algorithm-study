const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let counter = 0;
  let T = 0;
  let sum = 0;

  for await (const line of rl) {
    if (counter === 0) {
      T = line;
    } else {
      const math = line.split(" ");
      const firstNumber = Number(math[0]);
      const operator = math[1];
      const lastNumber = Number(math[2]);

      switch (operator) {
        case "+":
          sum += firstNumber + lastNumber;
          break;

        case "-":
          sum += firstNumber - lastNumber;
          break;

        case "/":
          sum += Math.floor(firstNumber / lastNumber);
          break;

        case "*":
          sum += firstNumber * lastNumber;
          break;

        default:
          break;
      }
    }

    if (counter >= T) rl.close();
    counter++;
  }

  console.log(sum);
})();
