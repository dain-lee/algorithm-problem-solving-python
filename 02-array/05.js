const arr = [87, 89, 92, 100, 76];

function solution(arr) {
  const rank = [...arr];
  rank.sort((a, b) => a - b);

  const len = arr.length;

  const answer = Array.from({ length: len }, () => 0);

  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      if (rank[i] === arr[j]) answer[j] = i + 1;
    }
  }

  return answer;
}

console.log(solution(arr));

// 강사님 풀이

function solution(arr) {
  let n = arr.length;

  let answer = Array.from({ length: n }, () => 1);

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (arr[j] > arr[i]) answer[i]++;
    }
  }

  return answer;
}
