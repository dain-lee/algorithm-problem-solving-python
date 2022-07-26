function solution(n, s) {
  let num = 0;
  let answer = '';

  for (let x of s) {
    if (num < x.length) {
      answer = x;
      num = x.length;
    }
  }

  return answer;
}

let num = 5;
let str = ['teacher', 'time', 'student', 'beautiful', 'good'];

console.log(solution(num, str));

// 강사님 풀이

function solution(n, s) {
  let answer = '',
    max = Number.MIN_SAFE_INTEGER;

  for (let x of s) {
    if (x.length > max) {
      max = x.length;
      answer = x;
    }
  }

  return answer;
}
