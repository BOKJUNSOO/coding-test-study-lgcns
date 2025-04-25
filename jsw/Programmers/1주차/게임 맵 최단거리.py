from collections import deque
def solution(maps):
    answer = 0
    q = deque()
    n = len(maps)
    m = len(maps[0])
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    s_row, s_col = 0, 0
    q.append([s_row,s_col])
    while q:
        length = len(q)
        for _ in range(length):
            r,c = q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1:
                    maps[nr][nc] = maps[r][c] + 1
                    q.append([nr,nc])
    if maps[-1][-1] == 1:
        answer = -1
    else:
        answer = maps[-1][-1]
    return answer

회고록
일단 BFS로 푸는 것은 깨우쳤습니다!!(하지만 다시 연습해야겠지요...)
