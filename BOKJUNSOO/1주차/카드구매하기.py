n = int(input())
card_ = [0] + list(map(int, input().split()))
dp = [0] * 1001
dp[1] = card_[1]
for i in range(2,n+1):
    max_ = dp[i]
    for j in range(1,i+1):
        # (i-j) + (j) = i 를 항상 만족해야 한다.
        if max_ < (dp[i-j] + card_[j]):
            max_ = dp[i-j] + card_[j]
        # dp 테이블 초기화
        dp[i] = max_
print(dp[n])