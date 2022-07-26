function solution(s) {
  let answer = 0;

  for (let i = 0; i < s.length; i++) {
    let ascii = s.charCodeAt(i);

    if (65 <= ascii && ascii <= 90) answer++;
  }

  return answer;
}

let str = 'KoreaTimeGood';

console.log(solution(str));

// 강사님 풀이 01

function solution(s) {
  let answer = 0;

  for (let x of s) {
    if (x === x.toUpperCase()) answer++;
  }

  return answer;
}

// 강사님 풀이 02

function solution(s) {
  let answer = 0;

  for (let x of s) {
    let num = x.charCodeAt();

    if (num >= 65 && num <= 90) answer++;
  }

  return answer;
}
