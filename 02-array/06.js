const arr = [
  [10, 13, 10, 12, 15],
  [12, 39, 30, 23, 11],
  [11, 25, 50, 53, 15],
  [19, 27, 29, 37, 27],
  [19, 13, 30, 13, 19],
];

function solution(arr) {
  const sumList = [];
  const len = arr.length;
  let sum = 0;

  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      sum += arr[i][j];
    }

    sumList.push(sum);
    sum = 0;
  }

  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      sum += arr[j][i];
    }

    sumList.push(sum);
    sum = 0;
  }

  for (let i = 0; i < len; i++) {
    sum += arr[i][i];

    if (i === len - 1) {
      sumList.push(sum);
      sum = 0;
    }
  }

  for (let i = 0; i < len; i++) {
    for (let j = len - 1; j >= 0; j--) {
      sum += arr[j][i];
    }

    sumList.push(sum);
    sum = 0;
  }

  return Math.max(...sumList);
}

console.log(solution(arr));

// 강사님 풀이

function solution(arr) {
  let answer = Number.MIN_SAFE_INTEGER;
  let n = arr.length;
  let sum1 = (sum2 = 0);

  for (let i = 0; i < n; i++) {
    sum1 = sum2 = 0;

    for (let j = 0; j < n; j++) {
      sum1 += arr[i][j];
      sum2 += arr[j][i];
    }

    answer = Math.max(answer, sum1, sum2);
  }

  sum1 = sum2 = 0;

  for (let i = 0; i < n; i++) {
    sum1 += arr[i][i];
    sum2 += arr[i][n - i - 1];
  }

  answer = Math.max(answer, sum1, sum2);

  return answer;
}
