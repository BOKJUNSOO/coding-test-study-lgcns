from collections import deque
M, N = map(int,input().split())
miro = []
for _ in range(N):
    miro.append(list(map(int,input())))
#상우하좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]
visited = [[-1] * M for _ in range(N)]
visited[0][0] = 0
q= deque()
q.append((0,0))
while q:
    rSpot, cSpot = q.popleft()
    for i in range(4):
        nr = dr[i] + rSpot
        nc = dc[i] + cSpot
        if 0 <= nr < N and 0 <= nc < M:
            #방문 안한곳이 벽이 없을 때
            if visited[nr][nc] == -1:
                if miro[nr][nc] == 0:
                    visited[nr][nc]= visited[rSpot][cSpot]
                    #벽이 없는 좌표부터 먼저 순회해야하니니
                    q.appendleft((nr,nc))
                elif miro[nr][nc] == 1:
                    #벽이 있으면 벽을 깼으니까 count +1
                    visited[nr][nc] = visited[rSpot][cSpot] + 1
                    #우선순위 밀려 남으로 젤 뒤에 추가가
                    q.append((nr,nc))
print(visited[-1][-1])