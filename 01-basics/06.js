function solution(arr) {
  let odd = [];
  let sum = 0;

  for (let i = 0; i < 7; i++) {
    if (arr[i] % 2 == 1) odd.push(arr[i]);
  }

  let min = odd[0];

  for (let j = 0; j < odd.length; j++) {
    sum += odd[j];
    if (odd[j] < min) min = odd[j];
  }

  return '홀수들의 합: ' + sum + ', 홀수들 중 최솟값: ' + min;
}

let arr = [12, 77, 38, 41, 53, 92, 85];

console.log(solution(arr));

// 강사님 풀이

function solution(arr) {
  let answer = [];
  let sum = 0,
    min = 1000;

  for (let x of arr) {
    if (x % 2 === 1) {
      sum += x;
      if (x < min) min = x;
    }
  }

  answer.push(sum);
  answer.push(min);

  return answer;
}
