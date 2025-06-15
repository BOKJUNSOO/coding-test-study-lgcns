from collections import deque

N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

def bfs():
    max_val = -int(1e9)
    min_val = int(1e9)

    queue = deque()
    # (현재까지의 값, 현재 인덱스, +, -, *, / 남은 수)
    queue.append((numbers[0], 1, add, sub, mul, div))

    while queue:
        total, idx, a, s, m, d = queue.popleft()

        if idx == N:
            max_val = max(max_val, total)
            min_val = min(min_val, total)
            # 아직 계산을 해야하는 경로가 존재하므로로
            continue

        num = numbers[idx]

        if a > 0:
            queue.append((total + num, idx + 1, a - 1, s, m, d))
        if s > 0:
            queue.append((total - num, idx + 1, a, s - 1, m, d))
        if m > 0:
            queue.append((total * num, idx + 1, a, s, m - 1, d))
        if d > 0:
            if total < 0:
                queue.append((-(abs(total) // num), idx + 1, a, s, m, d - 1))
            else:
                queue.append((total // num, idx + 1, a, s, m, d - 1))

    return max_val, min_val

max_result, min_result = bfs()
print(max_result)
print(min_result)
