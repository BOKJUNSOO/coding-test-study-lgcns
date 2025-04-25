import sys
input = sys.stdin.readline
memo = [1,2,4,7]
for _ in range(int(input())):
    n = int(input())
    for i in range(len(memo),n):
        memo.append(memo[-1]+memo[-2]+memo[-3] % 1000000009)
    print(memo[-1])

# 회고록
# DP는 왜이리 점화식 세우는 것이 어려운지....
# 접근도 못하다가 velog에서 푼 것을 봤는데 허망했습니다...
# 근데 시간초과로 못풀었습니다...