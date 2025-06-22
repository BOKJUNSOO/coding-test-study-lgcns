import sys
input = sys.stdin.readline
N = int(input())
S = list()
minn = 10000000
for _ in range(N):
    S.append(list(map(int,input().split())))
visited = [False] * N
def backtrack(d,idx):
    global minn
    if N // 2 == d:
        team1 = 0
        team2 = 0
        for i in range(N-1):
            for j in range(i+1, N):
                if visited[i] and visited[j]:
                    team1 += S[i][j] + S[j][i]
                if not visited[i] and not visited[j]:
                    team2 += S[i][j] + S[j][i]
        minn = min(minn,abs(team1 - team2))
        return
    for i in range(idx,N):
        if not visited[i]:
            visited[i] = True
            backtrack(d+1,i+1)
            visited[i] = False
backtrack(0,0)
print(minn)