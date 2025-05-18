from collections import deque
import sys
sys.setrecursionlimit(10000)

n = int(input())
# tosso는 역간 관계-각 인덱스가 역번호-
tosso = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
# 순환선인 역변호 찾기
sunhwan = []
# 순환선 찾았는지 여부
isexist = False

# 투다츠와 마찬가지로 순환선 찾기는 DFS
# 다만 여긴 연결관계가 정의되어 있어 굳이 상하좌우 안찾아도돼
def solution(i,sijak,count,temp):
    
    global isexist
    
    for j in tosso[i]:
        if visited[j]==0:
            visited[j] = 1
            solution(j,sijak,count+1,temp+[j])
            #초기화
            visited[j] = 0
            
        if visited[j]==1 and j==sijak and count>2:
            for k in temp:
                sunhwan.append(k)
            isexist = True
            
# 거리 찾기는 BFS 사용
def solution2():
    ee = deque()
    # 각 역별 거리를 담는 배열: -1로 초기화
    ddogae = [-1 for i in range(n+1)]
    
    # 순환선 역들은 전부 거리 0으로
    # 큐는 순환선만 넣어 초기화
    for i in sunhwan:
        ee.append((i,0))
        ddogae[i] = 0
    
    while ee:
        print(ee)
        print(ddogae)
        print()
        a, kori = ee.popleft()
        
        # 연결된 역 찾기
        for i in tosso[a]:
            # 거리가 초기화되있으면(즉 순환선이 아니면) 큐에 거리+1해서 넣어
            if ddogae[i] == -1:
                ddogae[i] = kori+1
                ee.append((i,kori+1))
    return ddogae
    

# 각 인덱스에 해당되는 항목들이 해당 역번호와 연결된 역들
for i in range(n):
    a,b = map(int, input().split())
    tosso[a].append(b)
    tosso[b].append(a)

for i in range(1,n+1):
    # 순환선은 하나밖에 없으므로 하나라도 찾았으면 다음거 찾지마
    if isexist == True:
        break
    visited[i]=1
    solution(i,i,1,[i])
    #초기화
    visited[i]=0

dachs = solution2()
temp = ""
for i in range(1,len(dachs)):
    temp+=str(dachs[i])+" "
print(temp)