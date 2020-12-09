// https://programmers.co.kr/learn/courses/30/lessons/68644

function solution(numbers) {
  var answer = [];

  for (let i = 0; i <= numbers.length; i++) {
    for (let ii = 0; ii <= numbers.length; ii++) {
      var result = numbers[i] + numbers[ii];
      if (i != ii && !isNaN(result)) {
        answer.push(result);
      }
    }
  }

  // 중복 숫자 제거
  let uniqueArray = [];
  answer.forEach((element) => {
    if (!uniqueArray.includes(element)) {
      uniqueArray.push(element);
    }
  });

  // 오름차순 정렬
  uniqueArray.sort(function (a, b) {
    return a - b;
  });

  console.log(uniqueArray);
  return uniqueArray;
}

solution([2, 1, 3, 4, 1]);
