const arr = [130, 135, 148, 140, 145, 150, 150, 153];

function solution(arr) {
  let cnt = 1;
  let max = arr[0];

  for (let i = 0; i < arr.length; i++) {
    if (max < arr[i]) {
      cnt++;
      max = arr[i];
    }
  }

  return cnt;
}

console.log(solution(arr));
