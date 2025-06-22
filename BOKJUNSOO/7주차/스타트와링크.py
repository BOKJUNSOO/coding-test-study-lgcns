from itertools import combinations
N= int(input())

matrix_ =[]
combinations_ = []
answer = []
# 입력
for _ in range(N):
    list_ = list(map(int, input().split()))
    matrix_.append(list_)

# 팀을 나누는 모든 경우의 수
stack = { _ for _ in range(N)}
for combination in combinations(range(N),int(N/2)):
    combination1 = stack - set(combination)
    combinations_.append([combination,tuple(combination1)])


# 어떤 팀의 인원이 정해지면 능력치의 합을 구하는 함수
def summation(v:tuple) -> int:
    int_ = 0
    for c in combinations(v,2):
        row_ = c[0]
        col_ = c[1]
        sum_ = matrix_[row_][col_] + matrix_[col_][row_]
        int_ += sum_
    return int_

# matrix 를 확인하면서 모든 능력치 계산 후 리스트에 저장
for list_ in combinations_:
    start_team = list_[0]
    link_team = list_[1]
    
    answer_ = abs(summation(start_team) - summation(link_team))
    answer.append(answer_)

print(min(answer))
