from collections import deque
from copy import deepcopy
from itertools import combinations

n,m = map(int,input().split())
maep = []

def solution(grid, N, M):
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    queue = deque()
    
    # (x, y, 벽 부순 횟수)
    queue.append((0, 0, 0))
    visited[0][0][0] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y, b = queue.popleft()
        
        if x == N-1 and y == M-1:
            return visited[x][y][b]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                # 벽이 아닌 경우
                if grid[nx][ny] == 0 and visited[nx][ny][b] == 0:
                    visited[nx][ny][b] = visited[x][y][b] + 1
                    queue.append((nx, ny, b))
                # 벽인 경우 -> 부술 수 있다면
                if grid[nx][ny] == 1 and b == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][b] + 1
                    queue.append((nx, ny, 1))
    
    return -1
    
for i in range(n):
    maep.append(list(map(int,input())))

answer = solution(maep,n,m)
print(answer)