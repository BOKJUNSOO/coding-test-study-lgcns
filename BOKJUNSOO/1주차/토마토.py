from collections import deque

col, row = map(int, input().split())
matrix_ = [list(map(int, input().split())) for _ in range(row)]

# 1을 찾아두기 
vector = deque() # bfs -> queue 를 사용해야겠다!
for v in range(row):
    for w in range(col):
        if matrix_[v][w] == 1:
            vector.append((v, w))

# 익히기
# queue 에서 모든 vector가 빠지면 count // flag 필요
# queue 에서 하나가 빠질때 4방향을 탐색하고 queue에 추가
def find(w: tuple):
    """
    튜플이 하나 주어지면 4방향을 확인

    행렬에 값을 할당하는 하고 (토마토를 익게 하고)
    큐에 값을 할당하는 함수 (해당 일자에 익힌 위치를 추가하는 함수)
    """
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = w
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 움직인 방향이 matrix 밖이라면 countinue
        if not (0 <= nx < row and 0 <= ny < col): 
            continue
        # 이미 익었거나 토마토가 없다면 countinue
        if matrix_[nx][ny] == -1 or matrix_[nx][ny] == 1:
            continue
        # 익힐 토마토를 발견했다면
        if matrix_[nx][ny] == 0:
            matrix_[nx][ny] = 1
            vector.append((nx, ny))

# 첫째날 익어있는 건 0일로 시작해야함
days = -1
while vector:
    # 현재 큐 크기만큼(하루치) 꺼내서 find() 호출
    for _ in range(len(vector)):
        pos = vector.popleft()
        find(pos)
    days += 1

# 최종 matrix_ 확인
for line in matrix_:
    # 못익힌게 있다면
    if 0 in line:
        print(-1)
        break
else:
    print(days)
