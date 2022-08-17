const arr = [32, 55, 62, 20, 250, 370, 200, 30, 100];

function isPrime(n) {
	if (n === 1) return false;

	for (let i = 2; i < Math.sqrt(n); i++) {
		if (n % i === 0) return false;
	}

	return true;
}

function solution(arr) {
	let answer = [];

	for (let x of arr) {
		const reversedNum = Number(x.toString().split('').reverse().join(''));

		if (isPrime(reversedNum)) answer.push(reversedNum);
	}

	return answer;
}

console.log(solution(arr));
