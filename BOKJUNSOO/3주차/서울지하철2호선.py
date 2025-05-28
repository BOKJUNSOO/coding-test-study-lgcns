# re commit
# 순환선 : 한역에서 출발해 계속 가서 언젠간 돌아올때
# 지선 : 순환선에 속하는 한 역에서 시작하는 트리 형태의 노선
# 순환선 사이의 거리 : 역 A와 순환선사이의 거리 = A와 순환선에 속하는 역사이의 거리중 최솟값
    # 예를들어 
    # 양천구청역과 순환선 사이의 거리는 2임 순환선에 존재하는 어떤역(신도림역)이 양천구천역과 사이의 거리가 2이기 때문
    # 대림역과 순환선 사이의 거리는 0임 왜냐하면 대림역 자체도 순환선에 속하는 역이므로 이둘 사이의 거리는 0
    # 따라서 순환선에 해당하는 역들은 모두 거리가 0임

    # 순환선을 구하는 방법
    # 시작역에서 연결된 역을 계속해서 탐색하다가 다시 시작역으로 돌아왔다면 그것은 순환역에 해당
    # 예외처리를 하나 하자면 2개이상의 역을 지나야함 (점 3개가 평면, 즉 순환하는 고리? 를 만들 수 있음)
    # DFS를 진행하다가 처음 

    # 순환선을 찾고 남은 역이 지선이 되는데
    # 최소 거리를 구해야함
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

cycle_nodes = set()

def dfs(start):
    stack = [(start, 0, [])]  # (현재노드, 이전노드, 현재까지 경로)
    visited = [False] * (N + 1)

    while stack:
        current, parent, path = stack.pop()
        if visited[current]:
            # 이미 방문한 노드인데, 현재 경로에 있다면 사이클 발견
            if current in path:
                idx = path.index(current)
                cycle_nodes.update(path[idx:])
                return True
            continue
        
        visited[current] = True
        path = path + [current]  # 현재 경로에 현재노드 추가

        for neighbor in graph[current]:
            if neighbor == parent:
                continue
            stack.append((neighbor, current, path))
    return False

# 외부 방문 배열: 사이클 찾기 위해 모든 노드 검사
visited_global = [False] * (N + 1)
for i in range(1, N + 1):
    if not visited_global[i]:
        if dfs(i):
            break
        # dfs 내부에서 사용한 visited는 별도라서, 사이클 찾기 실패 시 다음 노드로 넘어감

# BFS로 순환선까지 거리 계산
distance = [-1] * (N + 1)
queue = deque()

# 순환선 노드는 거리 0으로 초기화 후 큐에 넣음
for node in cycle_nodes:
    distance[node] = 0
    queue.append(node)

while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
        if distance[neighbor] == -1:
            distance[neighbor] = distance[current] + 1
            queue.append(neighbor)

print(' '.join(map(str, distance[1:])))
