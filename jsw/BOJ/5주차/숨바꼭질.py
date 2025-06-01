#수빈 점 N, 동생 점 K
from collections import deque
N ,K = map(int, input().split())
day_count = 0
day_list = [0]*(100000+1)
q = deque()
q.append(N)
while q:
    dot = q.popleft()
    if dot == K:
        break
    dot_list = [dot+1, dot-1, dot*2]
    for i in dot_list:
        if 0 <= i <= 100000 and not day_list[i]:
            day_list[i] = day_list[dot] +1
            q.append(i)
print(day_list[K])