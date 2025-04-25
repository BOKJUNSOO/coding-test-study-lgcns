def solution(numbers, hand):
    answer = ''
    idx_list = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]
    left_row, left_col = 3,0
    right_row, right_col = 3,2
    for i in numbers:
        if str(i) == '1' or str(i) == '4' or str(i) == '7':
            for r_idx in range(len(idx_list)):
                if str(i) in idx_list[r_idx]:
                    c_idx = idx_list[r_idx].index(str(i))
                    break
            left_row, left_col = r_idx, c_idx
            answer += 'L'
        elif str(i) == '3' or str(i) == '6' or str(i) == '9':
            for r_idx in range(len(idx_list)):
                if str(i) in idx_list[r_idx]:
                    c_idx = idx_list[r_idx].index(str(i))
                    break
            right_row, right_col = r_idx, c_idx
            answer += 'R'
        elif str(i) == '2' or str(i) == '5' or str(i) == '8' or str(i) =='0':
            for r_idx in range(len(idx_list)):
                if str(i) in idx_list[r_idx]:
                    c_idx = idx_list[r_idx].index(str(i))
                    break
            num_row, num_col = r_idx, c_idx
            sum_right = abs(right_row - num_row) + abs(right_col - num_col)
            sum_left = abs(left_row - num_row) + abs(left_col - num_col)
            if sum_right > sum_left:
                left_row, left_col = num_row, num_col
                answer += 'L'
            elif sum_right < sum_left:
                right_row, right_col = num_row, num_col
                answer += 'R'
            elif sum_right == sum_left:
                answer += hand[0].upper()
                if hand == 'right':
                    right_row, right_col = num_row, num_col
                elif hand == 'left':
                    left_row, left_col = num_row, num_col
    return answer

# 회고록
# 너무 노가다로 한건가 싶네요..ㅠㅠㅠㅠ
# 2차원 배열의 각 행에 대한 열 값의 idx값을 얻고싶으면 
# idx_list[r_idx].index(str(i))
# 위와같이 해야된 다는 것을 알았습니다!!(지피티한테 물어봤습니다 사실...)
