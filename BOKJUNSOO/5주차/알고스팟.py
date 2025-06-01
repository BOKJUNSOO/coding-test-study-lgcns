from collections import deque

col, row = map(int, input().split())
graph = [[0] * col for _ in range(row)]

for _ in range(row):
    list_ = list(map(int, input().strip()))
    graph[_] = list_

visted = [[-1] * col for _ in range(row)]
queue = deque()
dx = [1,0,0,-1]
dy = [0,-1,1,0]

def bfs(a,b):
    queue.append((a,b))
    visted[0][0] = 0

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny < 0 or nx >= row or ny >= col:
                continue

            # 아직 방문을 하지 않은 graph에 대해서
            if visted[nx][ny] == -1:
                # 벽이 없는 방이라면
                if graph[nx][ny] == 0:
                    # 전까지 깻던 벽의 횟수를 그대로 전달(벽이 없으므로 count 하지 않음)
                    visted[nx][ny] = visted[x][y]
                    # 우선적으로 벽이 아닌 그래프를 탐색 (비용이 발생안했으므로 아직 기회가 있다다)
                    queue.appendleft((nx,ny)) 
                    continue
                # 벽이 있는 방인경우
                if graph[nx][ny] == 1:
                    # 벽을 깼으므로 +1 을 하고, 전까지 부쉈던 벽의 갯수를 함께 넘겨줌
                    visted[nx][ny] = visted[x][y] + 1
                    # 나중에 탐색 (벽을 깨는 것에 비용이 발생했으므로 기회가 더이상 없다)
                    queue.append((nx,ny))
bfs(0,0)
print(visted[row-1][col-1])

