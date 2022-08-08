function solution(s) {
  const regex = /[^a-z]/gi;

  const str = s.replace(regex, '').toUpperCase();
  const reverse = str.split('').reverse().join('');

  return str === reverse ? 'YES' : 'NO';
}

const str = 'found7, time: study; Yduts; emit, 7Dnuof';

console.log(solution(str));
