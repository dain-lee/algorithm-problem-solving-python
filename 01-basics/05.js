function solution(arr) {
  let answer = arr[0];

  for (let i = 1; i < 7; i++) {
    if (arr[i] < answer) answer = arr[i];
  }

  return answer;
}

let arr = [5, 7, 1, 3, 2, 9, 11];

console.log(solution(arr));

// 강사님 풀이

function solution(arr) {
  let answer,
    min = Number.MAX_SAFE_INTEGER;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < min) min = arr[i];
  }

  answer = min;

  return answer;
}

// [보충 내용] 내장 함수로 최소 최대 구하는 방법

function solution(arr) {
  let max = Math.max(...arr);
  let min = Math.min(...arr);

  return '최대: ' + max + ', 최소: ' + min;
}
