function solution(n) {
  if (n <= 12) return 1;

  const dozen = n / 12;
  const pencil = n % 12;

  if (0 < pencil) return Math.floor(dozen + 1);
  else return Math.floor(dozen);
}

console.log(solution(24));
console.log(solution(36));
console.log(solution(178));

// 강사님 풀이

function solution(n) {
  let answer;

  answer = Math.ceil(n / 12);

  return answer;
}
