# 정통 BFS 문제인데 이미 토마토에서 다 설명해서 주석은 안쓸게요~
# 옛날에 풀었던 문제라 탐색부분에 배열 안써서 조금 복잡해요
def solution(maps):
    answer = 1
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[0 for i in range(m)] for j in range(n)]
    
    queue = list()
    queue.append([(0,0)])
    visited[0][0] = 1
    while queue:
        tosso = queue[0]
        queue = queue[1:]
        temp = []
        while tosso:
            a,b = tosso[0]
            tosso = tosso[1:]
            if a+1<n and maps[a+1][b] !=0 and visited[a+1][b] == 0:
                visited[a+1][b] = 1
                temp.append((a+1,b))
            if a-1>=0 and maps[a-1][b] !=0 and visited[a-1][b] == 0:
                visited[a-1][b] = 1
                temp.append((a-1,b))
            if b+1<m and maps[a][b+1] !=0 and visited[a][b+1] == 0:
                visited[a][b+1] = 1
                temp.append((a,b+1))
            if b-1>=0 and maps[a][b-1] !=0 and visited[a][b-1] == 0:
                visited[a][b-1] = 1
                temp.append((a,b-1))
        if temp:
            queue.append(temp)
        answer+=1
        if visited[n-1][m-1]==1:
            break
    if visited[n-1][m-1]==0:
        answer = -1
    
    return answer