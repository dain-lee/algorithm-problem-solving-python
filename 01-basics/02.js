function solution(a, b, c) {
  if (a > b) {
    if (a > c) {
      if (b + c > a) {
        return 'YES';
      } else return 'NO';
    } else {
      if (a + b > c) {
        return 'YES';
      } else return 'NO';
    }
  } else {
    if (b > c) {
      if (a + c > b) {
        return 'YES';
      } else return 'NO';
    } else {
      if (a + b > c) {
        return 'YES';
      } else return 'NO';
    }
  }
}

console.log(solution(6, 7, 11));
console.log(solution(13, 33, 17));
console.log(solution(40, 33, 17));

// 강사님 풀이

function solution(a, b, c) {
  let answer = 'YES',
    max;
  let tot = a + b + c;

  if (a > b) max = a;
  else max = b;

  if (c > max) max = c;

  if (tot - max <= max) answer = 'NO';

  return answer;
}
