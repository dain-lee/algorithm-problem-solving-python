# 동전 0
# https://www.acmicpc.net/problem/11047
# 실버 4 | 시간 제한 1초 | 메모리 제한 256MB

'''
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
'''

'''
입력 조건
- 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
- 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

출력 조건
- 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
'''

n, k = map(int, input().split())
coin_types = []
count = 0

for i in range(n):
    coin_types.append(int(input()))

coin_types.sort(reverse=True) # 큰 동전부터 나눠보기 위해 reverse

for coin in coin_types:
    if coin > k: # 동전의 가치가 k보다 크면 나눌 수 없기 때문에 continue
        continue
    count += k // coin
    k %= coin

print(count)

# 시간 68ms | 메모리 30840KB | 코드 길이 255B