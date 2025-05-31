# 가장 빠른 거리 찾는 문제이므로 BFS

from collections import deque
a,b = map(int, input().split())
MAX = 10 ** 5
graph = [0] * (MAX+1)

queue = deque()
def bfs(a,b):
    if a == b:
        print(0)
        return
    queue.append(a)
    while queue:
        a = queue.popleft()
        if a == b:
            print(graph[a])
            return
        
        # 아직 방문하지 않은 노드이고 (0이 아니고 ) 갈 수 있는 방향이라면
        if 0<= a+1 <= MAX and not graph[a+1]:
            queue.append(a + 1)
            graph[a+1] = graph[a] + 1

        if 0<= a-1 <= MAX and not graph[a-1]:   
            queue.append(a - 1)
            graph[a-1] = graph[a] + 1

        if 0<= a*2 <= MAX and not graph[a*2]:
            queue.append(a*2)
            graph[a*2] = graph[a] + 1
bfs(a,b)