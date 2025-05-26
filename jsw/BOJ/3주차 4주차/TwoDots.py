N , M = map(int, input().split())
N_list = []
for _ in range(N):
    N_list.append(list(input()))
# 상우하좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]
visited = [[0 for _ in range(M)] for _ in range(N)]
res = []
def dfs(x,y,prex,prey,count):
    if visited[x][y] and count > 4:
        res.append("yes")
        return
    visited[x][y] = 1
    for i in range(4):
        nx = dr[i] + x
        ny = dc[i] + y
        if 0<= nx < N and 0<= ny < M and N_list[nx][ny] == N_list[x][y]:
            if [nx,ny] != [prex,prey]:
                dfs(nx,ny,x,y,count+1)
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            dfs(i,j,i,j,0)
if res:
    print("Yes")
else:
    print("No")