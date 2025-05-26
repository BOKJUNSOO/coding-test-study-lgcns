N, K = map(int, input().split())
arr = [[0,0]]
for _ in range(N):
    arr.append(list(map(int ,input().split())))
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        if j < arr[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i][0]] + arr[i][1])
print(dp[N][K])