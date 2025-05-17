import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] * m for _ in range(n)]
for i in range(n):
    graph[i] = list(map(str, input().strip()))

ans = False
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def dfs(x,y,letter,count,start_x,start_y):
    global ans
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny <0 or nx >=n or ny >=m:
            continue
        if visited[nx][ny] == False and graph[nx][ny] == letter:
            visited[nx][ny] = True
            dfs(nx,ny,letter,count+1,start_x, start_y)
        # 더 이상 방문할 곳이 없거나 방문할 수 있는 곳이 없을때
        # 아래의 조건을 만족한다면
        elif count >= 4 and start_x == nx and start_y == ny:
            ans = True
            return

for i in range(n):
    for j in range(m):
        start_x = i
        start_y = j
        visited = [[False] * m for _ in range(n)]
        visited[start_x][start_y] = True
        dfs(i,j,graph[i][j],1,start_x,start_y)
        if ans:
            print("Yes")
            exit()
        else:
            continue
print("No")
            