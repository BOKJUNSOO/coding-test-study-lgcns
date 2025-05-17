# re commit
n = int(input())

cost = [[0]*3 for _ in range(n+1)]

for _ in range(1,n+1):
    new_row = list(map(int, input().split()))
    cost[_] = new_row

# dp
dp = [[0] *3 for _ in range(n+1)]
# init
for j in range(3):
    dp[1][j] = cost[1][j]

# dp 탐색
for i in range(2, n+1):
    for j in range(3):
        # 이전 행에서 k != j 인 값 중 최소를 직접 찾기
        min_prev = 1001
        for k in range(3):
            if k == j:
                continue
            if dp[i-1][k] < min_prev:
                min_prev = dp[i-1][k]
        dp[i][j] = cost[i][j] + min_prev

print(min(dp[n]))