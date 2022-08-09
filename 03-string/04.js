const str = 'teachermode';

function solution(s, t) {
  const len = s.length;
  let index = [];
  let temp = [];
  let answer = [];

  for (let i = 0; i < len; i++) {
    if (s[i] === t) index.push(i);
  }

  for (let i = 0; i < len; i++) {
    for (let j = 0; j < index.length; j++) {
      temp.push(Math.abs(index[j] - i));
    }
    answer.push(Math.min(...temp));
    temp = [];
  }

  return answer;
}

console.log(solution(str, 'e'));

// 강사님 풀이

function solution(s, t) {
  let answer = [];
  let p = 1000;

  for (let x of s) {
    if (x === t) {
      p = 0;
      answer.push(p);
    } else {
      p++;
      answer.push(p);
    }
  }

  p = 1000;

  for (let i = s.length - 1; i >= 0; i--) {
    if (s[i] === t) p = 0;
    else {
      p++;
      answer[i] = Math.min(answer[i], p);
    }
  }

  return answer;
}
