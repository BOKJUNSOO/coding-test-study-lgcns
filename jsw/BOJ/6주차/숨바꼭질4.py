from collections import deque
N, K = map(int ,input().split())
dot_list = [0] * 100001
visited = [0] * 100001
q = deque()
q.append(N)

def path(current):
    arr = []
    temp = current
    for _ in range(dot_list[current] + 1):
        arr.append(temp)
        temp = visited[temp]
    print(' '.join(map(str, arr[::-1])))
while q:
    current = q.popleft()
    if current == K:
        print(dot_list[current])
        path(current)
        break
    for i in (current-1, current+1, current*2):
        if 0<= i <= 100000 and dot_list[i] == 0:
            dot_list[i] = dot_list[current] + 1
            q.append(i)
            # 현재 노드에서 이전 노드에서 온 값을 넣어줌
            visited[i] = current