def vector(start):
    matrix=[
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['*','0','#']
    ]
    for i in range(len(matrix)):
        for j in range(3):
            if start in matrix[i][j]:
                v = (i,j)
    return v

def distance(v,w):
    dis = abs(v[0] - w[0]) + abs(v[1] - w[1])
    return dis

def solution(numbers,hand):
    answer = ""
    left_h="*"
    right_h="#"
    left_col=[1,4,7]
    right_col=[3,6,9]
    for _ in numbers:
        if _ in left_col:
            answer+="L"
            left_h=str(_)
            continue
        if _ in right_col:
            answer+="R"
            right_h=str(_)
            continue
        # 누를 번호가 2,5,8,0이라면
        else:
            v = vector(left_h)
            w = vector(right_h)
            k = vector(str(_))
            if distance(v,k) < distance(w,k):
                answer+="L"
                left_h=str(_)
                continue
            if distance(v,k) > distance(w,k):
                answer+="R"
                right_h=str(_)
                continue
            else:
                if hand =="right":
                    answer+="R"
                    right_h=str(_)
                    continue
                else:
                    answer+="L"
                    left_h=str(_)
                    continue
    return answer