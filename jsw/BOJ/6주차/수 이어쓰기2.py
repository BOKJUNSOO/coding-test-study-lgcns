#단순 구현 문제?
N, K = map(int, input().split())
#1의 자리와 숫자 개수 초기화
digits, count, start_num = 1, 9, 1
while K > digits * count:
    K -= (digits * count)
    digits += 1
    count *= 10
    start_num *= 10
num = str(start_num + (K-1) // digits)
if int(num) > N:
    print(-1)
else:
    num_idx = (K-1) % digits
    print(num[num_idx])