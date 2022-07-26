function solution(s, t) {
  let answer = 0;

  for (let x of s) {
    if (x === t) answer++;
  }

  return answer;
}

let str = 'COMPUTERPROGRAMMING';

console.log(solution(str, 'R'));

// 강사님 풀이 01

function solution(s, t) {
  let answer = 0;

  for (let x of s) {
    if (x === t) answer++;
  }

  return answer;
}

// 강사님 풀이 02

function solution(s, t) {
  let answer = s.split(t).length - 1;

  return answer;
}
