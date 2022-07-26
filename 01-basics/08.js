function solution(arr) {
  let sum = 0;
  let num = 0;

  for (let x of arr) {
    sum += x;
  }

  for (let i = 0; i < 8; i++) {
    for (let j = i + 1; j < 9; j++) {
      num = arr[i] + arr[j];

      if (sum - num == 100) {
        let temp = arr.filter(element => element !== arr[i]);
        let answer = temp.filter(element => element !== arr[j]);

        return answer;
      }
    }
  }
}

let arr = [20, 7, 23, 19, 10, 15, 25, 8, 13];

console.log(solution(arr));

// 강사님 풀이

function solution(arr) {
  let answer = arr;
  let sum = answer.reduce((a, b) => a + b, 0);

  for (let i = 0; i < 8; i++) {
    for (let j = i + 1; j < 9; j++) {
      if (sum - (answer[i] + answer[j]) == 100) {
        answer.splice(j, 1);
        answer.splice(i, 1);
      }
    }
  }
  return answer;
}
