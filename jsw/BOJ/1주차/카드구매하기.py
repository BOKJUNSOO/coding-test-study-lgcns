import sys
input = sys.stdin.readline
N = int(input())
p = [0] +list(map(int,input().split()))
dp = [0 for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,i+1):
        #카드를 사는 경우의 수 
        # ex) 3일때
        # j = 1이면 원래의 dp[3]의 값과 dp[2] + p[1]의 값을 비교
        # j = 2이면 원래의 dp[3]의 값과 dp[1] + p[2]의 값을 비교
        # j = 3이면 원래의 dp[3]의 값과 dp[0] + p[3]의 값을 비교
        # dp 0은 임의로 0으로 맞춰줬기 때문에 문제 x
        dp[i] = max(dp[i-j] + p[j], dp[i])
print(max(dp))