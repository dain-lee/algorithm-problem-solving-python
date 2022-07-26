function solution(s) {
  let answer = '';
  const num = s.length;
  const index = Math.floor(num / 2);

  if (num % 2 !== 0) answer = s[index];
  else answer = s.slice(index - 1, index + 1);

  return answer;
}

console.log(solution('study'));
console.log(solution('good'));

// 강사님 풀이 01

function solution(s) {
  let answer;
  let mid = Math.floor(s.length / 2);

  if (s.length % 2 === 1) answer = s.substring(mid, mid + 1);
  else answer = s.substring(mid - 1, mid + 1);

  return answer;
}

// 강사님 풀이 02

function solution(s) {
  let answer;
  let mid = Math.floor(s.length / 2);

  if (s.length % 2 === 1) answer = s.substr(mid, 1);
  else answer = s.substr(mid - 1, 2);

  return answer;
}
