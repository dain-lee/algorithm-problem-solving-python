const arr = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0];

function solution(arr) {
  let correctCnt = 0;
  let answer = 0;

  for (let x of arr) {
    if (x === 1) {
      correctCnt++;
      answer += correctCnt;
    } else {
      correctCnt = 0;
    }
  }

  return answer;
}

console.log(solution(arr));
