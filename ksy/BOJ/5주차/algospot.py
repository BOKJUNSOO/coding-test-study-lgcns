from collections import deque

n, m = map(int, input().split())

tosso = [[0] * n for i in range(m)]
visited = [[-1] * n for i in range(m)]
visited[0][0]=0

for i in range(m):
    tosso[i] = list(map(int,str(input())))


karo = [0,0,1,-1]
sero = [1,-1,0,0]

dachs = set([])


def solution():
    
    ee = deque()
    ee.append([0,0,0])
    
    while ee:
        
        x,y,z = ee.popleft()
        
        
        for i in range(4):
            dx = x+karo[i]
            dy = y+sero[i]
            
            
            if 0<=dx<n and 0<=dy<m and visited[dy][dx] == -1:
                if tosso[dy][dx] == 1:
                    visited[dy][dx] = visited[y][x]+1
                    ee.append([dx,dy,z+1])
                else:
                    visited[dy][dx] = visited[y][x]
                    ee.appendleft([dx,dy,z])
    
solution()
print(visited[m-1][n-1])
