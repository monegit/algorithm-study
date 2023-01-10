/**
 * @param {string} today
 * @param {string[]} terms
 * @param {string[]} privacies
 * @returns
 */
function solution(today, terms, privacies) {
  var answer = [];

  let _today = new Date(today);
  // 1일을 더해준다
  _today.setDate(_today.getDate() + 1);

  privacies.forEach((date, dateIndex) => {
    // date의 날짜를 가져옴
    let _privacyData = date.split(" ");
    let _privacyDate = new Date(_privacyData[0]);
    // 1일을 더해준다
    _privacyDate.setDate(_privacyDate.getDate() + 1);
    let _privacyType = _privacyData[1];

    // today.year - privacyDate.year 하면 1970년을 시작으로 year의 차가 나온다.
    let month =
      (_today.getFullYear() - _privacyDate.getFullYear()) * 12 +
      (_today.getMonth() - _privacyDate.getMonth());
    let day = _today.getDate() - _privacyDate.getDate();

    terms.forEach((term) => {
      let _termData = term.split(" ");
      let _termType = _termData[0];
      let _termMonth = _termData[1];

      if (
        _privacyType === _termType &&
        dateToDay(month, day) >= _termMonth * 28
      )
        answer.push(...[dateIndex + 1]);
    });
  });

  return answer;
}

/**
 * @param {number} month
 * @param {number} day
 */
function dateToDay(month, day) {
  // 한 달은 28일까지 있다고 가정한 일 수.
  return month * 28 + day;
}

console.log(
  solution(
    "2022.05.19",
    ["A 6", "B 12", "C 3"],
    ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
  )
);

console.log(
  solution(
    "2020.01.01",
    ["Z 3", "D 5"],
    [
      "2019.01.01 D",
      "2019.11.15 Z",
      "2019.08.02 D",
      "2019.07.01 D",
      "2018.12.28 Z",
    ]
  )
);
