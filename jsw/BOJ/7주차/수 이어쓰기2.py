def binary(n):
    if n == 0:
        return 0
    total_len = 0
    digits = 1
    count = 9
    start = 1
    while start * 10 <= n:
        total_len += digits * count
        digits += 1
        start *= 10
        count *= 10
    total_len += digits * (n- start)
    return total_len


N, K = map(int, input().split())

if binary(N) < K:
    print(-1)
else:
    left, right = 1, N
    ans_num = 0
    while left <= right:
        mid = (left + right) // 2
        length = binary(mid)
        if length >= K:
            ans_num = mid
            right = mid -1
        else:
            left = mid + 1

len_before = binary(ans_num-1)

idx = K - len_before -1
print(str(ans_num)[idx])