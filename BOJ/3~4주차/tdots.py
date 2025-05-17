import copy

n, m = map(int, input().split())

tosso = []
ee = "No"

for i in range(n):
    tosso.append(list(input()))
    
#싸이클 찾는거니까 DFS
karo = [0,0,1,-1]
sero = [1,-1,0,0]

#이번 DFS에는 visited대신 시작 좌표값과 카운트값을 넣어주는데...이유는 후술
def solution(a,b,sijaka,sijakb,count):
    
    # 전역변수가 함수 안에서 영향받으려면 global 선언해줘야
    global ee
    
    # 마찬가지로 깊은복사 사용하여 재귀끼리 영향 안받도록
    # 이방법 사용하면 시간초과 걸려 다른방법 사용
    # dachs = copy.deepcopy(visited)
    
    
    for i in range(4):
        
        da = a+karo[i]
        db = b+sero[i]
        
        hyonjae = tosso[a][b]
        
        #for k in visited:
        #    print(k)
        #print(count)
        
        
        if 0<=da<len(tosso) and 0<=db<len(tosso[0]):
            # 색갈 같은것도 체크해야
            if visited[da][db]==0 and hyonjae==tosso[da][db]:
                visited[da][db]=1
                # 다음좌표로 DFS 진행
                solution(da,db,sijaka,sijakb,count+1)
            # 중요-다음 좌표가 방문했으면서 시작 좌표라면 돌았다는 뜻이므로 Yes
            # 문제에서 싸이클은 4보다 크다 했으므로 카운트도 체크
            if visited[da][db]==1 and da==sijaka and db==sijakb and count>=4:
                ee = "Yes"
                return
                
# 브레이크변수                
ddogae = 0        
# 각 칸별로 싸이클찾기
for i in range(n):
    for j in range(m):
        # visited 배열 만들기
        visited = []
        for k in range(n):
            temp = []
            for l in range(m):
                temp.append(0)
            visited.append(temp)
        visited[i][j] = 1
        
        #dfs실행
        solution(i,j,i,j,1)
        if ee == "Yes":
            ddogae = 1
            break
    if ddogae==1:
        break
print(ee)