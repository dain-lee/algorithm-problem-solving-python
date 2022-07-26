function solution(a, b, c) {
  for (let i = 0; i < 3; i++) {
    if (a <= b) {
      if (a <= c) return a;
      else return c;
    } else {
      if (b <= c) return b;
      else return c;
    }
  }
}

console.log(solution(2, 4, 6));
console.log(solution(4, 2, 6));
console.log(solution(4, 6, 2));

// 강사님 풀이

function solution(a, b, c) {
  let answer;

  if (a < b) answer = a;
  else answer = b;

  if (c < answer) answer = c;

  return answer;
}
