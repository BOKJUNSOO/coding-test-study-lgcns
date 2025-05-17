# N,K = map(int, input().split())
# items=[]
# for _ in range(N):
#     w,v = map(int,input().split())
#     items.append((w,v))

# dp = [0] * (K + 1)

# for W, V in items:
#     # 뒤에서부터 순회
#     for w in range(K, W - 1, -1):
#         dp[w] = max(dp[w], dp[w - W] + V)

# print(dp[K])


N,K = map(int, input().split())
items = []
for _ in range(N):
    w,v = map(int,input().split())
    items.append((w,v))

# dp[i][j] : 'i' 개의 물건으로 무게 'j' 를 채웠을때 가치가 최대인 상태로 dp테이블 정의
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1,N+1): # i: 1~ N 개까지 입력으로 주어진 물건을 하나씩 적용시켜봄
    W,V = items[i-1]
    for w in range(K+1): # w: 0 ~ K까지인 가방 사용가능 범위
        if w < W:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w - W] + V)
print(dp[N][K])