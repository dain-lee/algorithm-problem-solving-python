function solution(s) {
  for (let i = 0; i < s.length; i++) {
    s = s.replace('A', '#');
  }

  return s;
}

let str = 'BANANA';

console.log(solution(str));

// 강사님 풀이 01

function solution(s) {
  let answer = '';

  for (let x of s) {
    if (x == 'A') answer += '#';
    else answer += x;
  }

  return answer;
}

// 강사님 풀이 02

function solution(s) {
  let answer = s;

  answer = answer.replace(/A/g, '#');

  return answer;
}
