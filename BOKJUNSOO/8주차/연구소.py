from itertools import combinations
from copy import deepcopy
row,col = map(int, input().split())
matrix_ = [[0] * col for _ in range(row)]

for r in range(row):
    matrix_[r] = list(map(int, input().split()))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
virus = []
room = []
answer = [] # 각 경우에따른 안전지대 counting
# check virus
for i in range(row):
    for j in range(col):
        if matrix_[i][j] == 0:
            room.append((i,j))
        if matrix_[i][j] == 2:
            virus.append((i,j))


# 벽을 세운 연구소를 인자로 넣으면 bfs 를 실행, 안전지대 리턴
def bfs(matrix_:list) -> int:
    # 백트랙킹을 위한 깊은복사
    queue = deepcopy(virus)
    count = 0
    while queue:
        v = queue.pop(0)
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if row <= nx or nx < 0 or ny >= col or ny < 0:
                continue
            # 벽인 경우
            if matrix_[nx][ny] == 1:
                continue
            # 2가 아닌경우 즉 아직 방문을 할 수 있는 방인 경우
            if matrix_[nx][ny] == 0:
                matrix_[nx][ny] =2
                queue.append((nx,ny))
    for i in range(row):
        for j in matrix_[i]:
            if j == 0:
                count += 1
    return count

for c in combinations(room,3):
    test_matrix_ = deepcopy(matrix_)
    for x, y in c:
        test_matrix_[x][y] =1
    count = bfs(test_matrix_)
    answer.append(count)
print(max(answer))