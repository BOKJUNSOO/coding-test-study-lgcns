tc = int(input())
inputs = [int(input()) for _ in range(tc)]

mod_ = 1000000009
max_n = max(inputs)
dp = [0] * (max_n + 1)
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_n + 1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % mod_

for n in inputs:
    print(dp[n])
