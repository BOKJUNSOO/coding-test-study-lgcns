from collections import deque
def solution(maps):
    answer = 0
    q = deque([])
    n = len(maps)
    m = len(maps[0])
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                q.append([i,j])
    while q:
        length = len(q)
        for _ in range(length):
            r,c = q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<= nr < n and 0 <= nc < m and maps[nr][nc] != 0:
                    maps[nr][nc] += maps[r][c] +1
    if maps[-1][-1] == 1:
        print(-1)
        return
    else:
        answer = maps[-1][-1]
    return answer