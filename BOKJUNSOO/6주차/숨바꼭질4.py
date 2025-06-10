from collections import deque
n, k = map(int,input().split())

MAX = 100001
visited = [0] * MAX
queue = deque()
def bfs():
    queue.append(n)
    while queue:
        q = queue.popleft() # n
        if q == k:
            print(visited[q])
            move(q)
            break

        if 0 <= q-1 < MAX and not visited[q-1]:
            queue.append(q-1)
            visited[q-1] = visited[q] + 1
            path[q-1] = q
            
        if 0<= q+1 < MAX and not visited[q+1]:
            queue.append(q+1)
            visited[q+1] = visited[q] + 1
            path[q+1] = q
        
        if 0<=q*2<MAX and not visited[q*2]:
            queue.append(q*2)
            visited[q*2] = visited[q] + 1
            path[q*2] = q

# 이동한 경로를 기록해 놓을 수 있는 리스트
# 5, 17로 예시를들면 
# 5는 0 으로 초기화되고 변하지 않을것이다.
# 5 -> 4, 6, 10 을 갈 수 있으므로
# 4,6,10 는 5로 초기화 될 것이다.
# 나중에 path[4] 를 확인하면, 이는 5에서 온 노드라는것을 확인할 수 있다.
path = [0] * MAX

def move(now):
    # 답으로 낼 리스트
    data = []
    # 임시로 사용할 변수
    temp = now
    # visited[now] 는 0 부터 점차 증가 시킨 값이 기록 (n==k 까지)
    for _ in range(visited[now] + 1):
        data.append(temp)
        # 현재 노드 이전에 방문했던 노드를 temp에 저장
        temp = path[temp]
    data.reverse()
    print(*data)

bfs()