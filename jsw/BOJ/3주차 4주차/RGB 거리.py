N = int(input())
N_list = []
dp = [[0]*3 for _ in range(N)]
for _ in range(N):
    N_list.append(list(map(int, input().split())))
dp[0] = N_list[0]
for i in range(1,N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + N_list[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + N_list[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + N_list[i][2]
print(min(dp[-1]))