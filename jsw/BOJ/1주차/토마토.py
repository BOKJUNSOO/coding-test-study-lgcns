import sys
from collections import deque
input = sys.stdin.readline
M , N = map(int, input().split())
#인접한 토마토에 접근하기 위한 dr, dc정의
#상우하좌 정의
dr, dc = [-1,0,1,0], [0,1,0,-1]

q = deque([])
tomato_list = []
for _ in range(N):
    tomato_list.append(list(map(int,input().split())))
#익은 토마토 큐에 삽입
for i in range(N):
    for j in range(M):
        if tomato_list[i][j] == 1:
            q.append([i,j])
#익은 토마토가 없을 때 까지 반복
def bfs():
    while q:
        length = len(q)
        # 현재 큐에 삽입되어있는 익은 토마토 개수만큼 출력
        for _ in range(length):
            # 익은 토마토 하나 꺼내기
            r, c = q.popleft()

            for i in range(4):
                #예제 1번 기준으로 (2,5) (3,4)가 됨됨
                nr = r + dr[i]
                nc = c + dc[i]

                if 0<= nr < N and 0 <= nc < M and tomato_list[nr][nc] == 0:
                    # r c에 비해 하루가 더 걸렸다는 의미를 기록
                    tomato_list[nr][nc] = tomato_list[r][c] + 1
                    q.append([nr,nc])
bfs()
day = 0
for row in tomato_list:
    for col in row:
        if col == 0:
            print(-1)
            exit(0)
    day = max(day,max(row))
print(day-1)