# 단순히 string을 이어붙히고 인덱스로 답을 내면 시간초과 발생

# N, K = map(int, input().split())
# check=""
# for _ in range(N):
#     check += str(_ + 1)
#     if len(check) > K+1:
#         print(check[K-1])
#         break
# if K > len(check):
#     print(-1)
# ----
# 규칙을 찾아야함
# 1) 반복되는 수열이 있는가? -> 없는것 같음
# 2) 특정 자릿수에서 탐색을 하면 되는가 ?
# -> 예를들어 3000번째 자릿수를 찾는다하면
# - 1자리수는 9개 (1~9)
# - 2자리수는 90개 (10~99) 99 - 10 + 1 = 90
# - 3자리수는 900개 (100 ~ 999) 999 - 100 + 1 = 900

# 근데 각각의 자릿수는 `n자릿수에서` n을 곱해야 하므로
# 9 + 90 * 2 + 900 * 3 = 9 + 180 + 2700 = 2889
# 따라서 구하고자하는 3000번째 자리수는 4자리수에서 찾아내야함 (3000 - 2889 = 111) 111번 째 자리수
# 1000, 1001 ... 방식으로 111번째를 찾으면 될것 같음

# 그러므로 K가 탐색할 위치를 적절히 찾고 해당 n자릿수에서 n번째 숫자를 찾아내면 될것 같음

# N, K = map(int, input().split())

# n = 1 # 자릿수를 표시할 변수
# count = 9 # n 자릿수에 해당하는 숫자의 갯수
# target_sum = 0 # 자릿수 * 해당 자릿수 숫자의 갯수의 합

# # 몇번째 자릿수를 탐색해야 하는지 찾는 루프
# while True:
#     target = count * n
#     if K <= target_sum + target:
#         check = K-target_sum # 확인해볼 나머지 자릿수
#         break
#     target_sum += target
#     n += 1
#     count = count * 10

# answer = (10**(n-1)) + (check -1) // n
# if answer > N or check <= 0:
#     print(-1)
# else:
#     print(str(answer)[(check - 1) % n])

N, K = map(int, input().split())

def count_digits(upto):
    length = 0
    digit = 1
    start = 1
    while True:
        end = min(upto, 10**digit - 1)
        if end < start:
            break
        length += (end - start + 1) * digit
        if end == upto:
            break
        start = 10**digit
        digit += 1
    return length

# 1부터 N까지 숫자를 이어 붙인 문자열의 길이보다 K가 크면 -1
if count_digits(N) < K:
    print(-1)
    exit()

# 이분탐색: K번째 숫자가 속한 실제 숫자 찾기
low, high = 1, N
while low < high:
    mid = (low + high) // 2
    if count_digits(mid) >= K:
        high = mid
    else:
        low = mid + 1

# low가 K번째 숫자가 포함된 숫자
# 이 숫자까지 이어 붙였을 때 자리수 총합
if low > 1:
    prev_length = count_digits(low - 1)
else:
    prev_length = 0
offset = K - prev_length - 1  # low 숫자 내에서 몇 번째 자리인지 (0부터 시작)

result = str(low)[offset]
print(result)

