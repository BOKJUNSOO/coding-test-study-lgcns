# n까지 몇 개의 수가 있는지를 계산하는 함수
def calc(n):
    length = 0
    digit = 1
    start = 1
    while start <= n:
        end = min(n, start * 10 - 1)
        length += (end - start + 1) * digit
        start *= 10
        digit += 1
    return length

def solution(n, k):
    # k가 n까지의 자리수를 초과하면 에라
    if calc(n) < k:
        return -1

    # 이분 탐색 개시
    low, high = 1, n
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        # k가 가운데까지의 사리수를 초과하면 그 위이므로 최소값 높이기
        if calc(mid) < k:
            low = mid + 1
        # 그 반대면 거기에 있으므로 최대값 낮추기 - answer는 가운데 값으로
        else:
            answer = mid
            high = mid - 1

    # answer 안에 k번째가 있으므로 answer까지의 자리수를 구하기
    tosso = calc(answer - 1)
    # 마찬가지로 전체 번째에서 answer까지의 자리수를 빼면 answer 안의 인덱스를 알 수 있어
    # -1 해주는 것도 잊지 말기
    index = k - tosso - 1
    return str(answer)[index]

n, k = map(int, input().split())
print(solution(n, k))
