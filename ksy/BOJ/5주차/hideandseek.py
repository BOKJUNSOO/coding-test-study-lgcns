from collections import deque

n, m = map(int, input().split())
tosso = [-1] * 100001
tosso[n] = 0

def solution():
    ee = deque()
    ee.append(n)
    
    while(ee):
        t = ee.popleft()
        if t==m:
           print(tosso[t])
           break
        
        for i in ([t-1,t+1,t*2]):
            if 0<=i<=100000 and tosso[i] == -1:
                tosso[i] = tosso[t]+1
                ee.append(i)
solution()