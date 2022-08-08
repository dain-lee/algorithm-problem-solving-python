const str = 'abcde';

function solution(s) {
  let answer = 'YES';
  const len = s.length;
  const upper = s.toUpperCase();

  for (let i in s) {
    if (upper[i] !== upper[len - 1 - i]) {
      answer = 'NO';
      break;
    }
  }

  return answer;
}

console.log(solution(str));

// 강사님 풀이 01

function solution(s) {
  let answer = 'YES';
  s = s.toLowerCase();
  let len = s.length;

  for (let i = 0; i < Math.floor(len / 2); i++) {
    if (s[i] != s[len - i - 1]) return 'NO';
  }

  return answer;
}

// 강사님 풀이 02

function solution(s) {
  let answer = 'YES';
  s = s.toLowerCase();

  if (s.split('').reverse().join('') != s) return 'NO';

  return answer;
}
