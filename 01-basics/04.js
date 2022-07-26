function solution(n) {
  let answer = 0;

  for (let i = 1; i <= n; i++) {
    answer += i;
  }

  return answer;
}

console.log(solution(5));
console.log(solution(10));
console.log(solution(20));

// 강사님 풀이

function solution(n) {
  let answer = 0;

  for (let i = 1; i <= n; i++) {
    answer = answer + i;
  }

  return answer;
}
