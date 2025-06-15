from itertools import combinations

n = int(input())

tosso = []

for i in range(n):
    tosso.append(list(map(int,input().split())))
    

def solution():
    
    # 1번부터 N번까지
    saram = [i for i in range(n)]
    
    # 차이 최소값 초기화
    result = 99999999999
    
    # 조합을 사용하여 사람들을 두 팀으로 나누는 모든 경우 계산
    for i in combinations(saram, n//2):
        start = list(i)
        link = list(set(saram) - set(start))
        
        # 각 팀의 점수 계산
        start_jumsu = 0
        link_jumsu = 0
        for i in start:
            for j in start:
                if i!=j:
                    start_jumsu += tosso[i][j]
        for i in link:
            for j in link:
                if i!=j:
                    link_jumsu += tosso[i][j]
        
        # 차이 계산해서 최소값 출력            
        chai = abs(start_jumsu - link_jumsu)
        result = min(result,chai)
        
        # 0은 따로 빼기-더 이상 계산할게 없어
        if result == 0:
            break
    
    return result
    
print(solution())