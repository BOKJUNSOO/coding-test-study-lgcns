#1개: 1
#2개: 2, 5
#3개: 3, 6, 6
#4개: 4, 4, 10, 4, 7, 7, 7

# 이런식으로 각각 최대금액(n): 최대값(최대금액(n)+최대금액(0),최대금액(n-1),최대금액(1),최대금액(n-2),최대금액(2),...) 순으로 진행해야


n = int(input())
kards = list(map(int,input().split(" ")))

# 카드 개수별 최대 금액이 담길 배열: 0장부터 시작
ee = [0] + kards


def tosso(n):
    # 위의 공식을 코드로 재현
    for i in range(1,n+1):
        for j in range(i):
            ee[i] = max(ee[i],ee[j]+ee[i-j])
    return max(ee)

print(tosso(n))            
