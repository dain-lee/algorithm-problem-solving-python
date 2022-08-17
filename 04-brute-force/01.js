const arr = [128, 460, 603, 40, 521, 137, 123];

function solution(arr) {
	let max = 0;
	let answer = 0;

	for (let x of arr) {
		const arr = x
			.toString()
			.split('')
			.map(x => Number(x));

		const sum = arr.reduce((a, b) => a + b);

		if (max < sum) {
			max = sum;
			answer = x;
		} else if (max === sum) {
			if (answer < x) answer = x;
		}
	}

	return answer;
}

console.log(solution(arr));

// 강사님 풀이

function solution(arr) {
	let answer,
		max = Number.MIN_SAFE_INTEGER;

	for (let x of arr) {
		let sum = 0,
			tmp = x;

		while (tmp) {
			sum += tmp % 10;
			tmp = Math.floor(tmp / 10);
		}

		if (sum > max) {
			max = sum;
			answer = x;
		} else if (sum === max) {
			if (x > answer) answer = x;
		}
	}

	return answer;
}
