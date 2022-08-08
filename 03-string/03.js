const str = 'g0en2T0s8eSoft';

function solution(str) {
  const regex = /[^0-9]/gi;
  const num = str.replace(regex, '');

  return Number(num);
}

console.log(solution(str));

// 강사님 풀이

function solution(str) {
  let answer = '';

  for (let x of str) {
    if (!isNaN(x)) answer += x;
  }

  return parseInt(answer);
}
