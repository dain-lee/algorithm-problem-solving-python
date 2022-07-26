function solution(s) {
  return s.toUpperCase();
}

let str = 'ItisTimeToStudy';

console.log(solution(str));

// 강사님 풀이 01

function solution(s) {
  let answer = '';

  for (let x of s) {
    let num = x.charCodeAt();

    if (num >= 97 && num <= 122) answer += String.fromCharCode(num - 32);
    else answer += x;
  }

  return answer;
}

// 강사님 풀이 02

function solution(s) {
  let answer = '';

  for (let x of s) {
    if (x === x.toLowerCase()) answer += x.toUpperCase();
    else answer += x;
  }

  return answer;
}
