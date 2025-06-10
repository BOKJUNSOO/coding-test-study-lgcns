from collections import deque

n, m = map(int, input().split())
tosso = [-1] * 100001
tosso[n] = 0

def solution():
    ee = deque()
    # 큐에 필살기-지금까지 거쳐온 길 저장하는 배열 추가!
    ee.append([n,[n]])
    
    while(ee):
        t, r = ee.popleft()
        if t==m:
           print(tosso[t])
           # 배열을 출력하기만 하면 끝!
           print(' '.join(map(str,r)))
           break
        
        for i in ([t-1,t+1,t*2]):
            if 0<=i<=100000 and tosso[i] == -1:
                tosso[i] = tosso[t]+1
                # 큐에 해당 길도 추가
                ee.append([i,r+[i]])
solution()
