#시간 구해야 하니 BFS로 풀어야

from collections import deque

#인자값입력
n,m = map(int,input().split())
tomato = []

for i in range(m):
    tomato.append(list(map(int,input().split())))

#탐색할때 쓸 배열(상하좌우탐색)
karo = [0,0,1,-1]
sero = [1,-1,0,0]

#탐색함수
def tosso(dachs):
    # BFS에 쓸 큐 생성(visited는 방문 확인)
    queue = deque([])
    visited = set([])
    
    # 큐에 초기 익은토마토 위치 넣기
    # queue의 0은 최초 시간
    for i in dachs:
        a,b = i
        queue.append((a,b,0))
        visited.add((a,b))
    
    # 시간변수
    ee = 0

    # 다들 아는대로 BFS탐색 진행
    while queue:
        x, y, z = queue.popleft()
        # 초기 익은토마토가 여러개일때는 가장 늦게 전부 탐색된 토마토 시간 기준이 되어야 하므로 최대값
        ee = max(z,ee)

        for i in range(4):
            nx = x + karo[i]
            ny = y + sero[i]

            if 0 <= nx < len(tomato) and 0 <= ny < len(tomato[0]):
                if (nx, ny) not in visited and tomato[nx][ny] == 0:
                    visited.add((nx, ny))
                    # 탐색 완료이므로 시간에 1 추가
                    queue.append((nx, ny, z+1))
    #
    return ee, len(visited)

# 초기 익은토마토들이 담길 변수
# 전부 익는 시간 계산이므로 한번에 전부 BFS 돌아야해
dachs = set([])    

# 막힌 칸 개수가 담긴 변수
minuscount = 0

for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            dachs.add((i,j))
        elif tomato[i][j] == -1:
            minuscount += 1
            
# q는 시간, w는 탐색된 칸 개수
q,w = tosso(dachs)
# 전체 칸개수에서 막힌칸 뺀 게 탐색한칸과 다르면 못다다른 칸이 있다는 뜻
if w!=((m*n)-minuscount):
    print(-1)
else:
    print(q)