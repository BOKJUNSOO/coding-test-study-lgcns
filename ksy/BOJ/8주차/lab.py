from collections import deque
from copy import deepcopy
from itertools import combinations

n,m = map(int,input().split())
lab = []

for i in range(n):
    temp = list(map(int,input().split()))
    lab.append(temp)

#bfs 탐색
def solution(lab,n,m):
    virus = deque([])
    for i in range(n):
        for j in range(m):
            if mylab[i][j]==2:
                virus.append([i,j])

    count=0
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]

    while virus:
        cur = virus.popleft()
        for i in range(4):
            y=cur[0]+dy[i]
            x=cur[1]+dx[i]
            if 0<=y<n and 0<=x<m:
                if mylab[y][x]==0:
                    mylab[y][x]=2
                    virus.append([y,x])
    for i in range(n):
        for j in range(m):
            if mylab[i][j]==0:
                count+=1
    return count
    
temp = 0
tosso = []
for i in range(n):
    for j in range(m):
        if lab[i][j]==0:
            tosso.append([i,j])

# 조합 사용: 벽을 3개 세울 수 있으니까 칸들 중 3개만 뽑기            
combi = list(combinations(tosso,3))
for i in combi:
    # 깊은복사로 중복 방지
    mylab = deepcopy(lab)
    # 벽 세우고 bfs 실행
    for j in i:
        mylab[j[0]][j[1]] = 1
    a = solution(mylab,n,m)
    # 최대값구하기
    if a>temp:
        temp = a
print(temp)