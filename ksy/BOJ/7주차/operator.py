from itertools import permutations

n = int(input())

su = list(map(int,input().split()))

# 0번은 더셈, 1번은 뺄셈, 2번은 곱셈, 3번은 나누셈
yonsanja = list(map(int,input().split()))



def solution(su,yonsanja):
    #10억
    choidae = -1000000000
    choiso = 1000000000
    
    #무작정 풀기: 일단 연산자 리스트에 저장
    tosso = []
    for i in range(yonsanja[0]):
        tosso.append('+')
    for i in range(yonsanja[1]):
        tosso.append('-')
    for i in range(yonsanja[2]):
        tosso.append('*')
    for i in range(yonsanja[3]):
        tosso.append('/')
    
    #이 연산자 리스트를 순열화해서 최대/최소 계산
    for i in permutations(tosso,len(tosso)):
        ee = su[0]
        index = 1
        for j in i:
            if j=='+':
                ee+=su[index]
            elif j=='-':
                ee-=su[index]
            elif j=='*':
                ee*=su[index]
            elif j=='/':
                #C++14식 나누기 적용
                if ee<0 and su[index]>0:
                    ee = -ee
                    ee = ee//su[index]
                    ee = -ee
                else:
                    ee = ee//su[index]
            index+=1
        choiso = min(ee,choiso)
        choidae = max(ee,choidae)
    return choidae, choiso

result = solution(su,yonsanja)
print(result[0])
print(result[1])