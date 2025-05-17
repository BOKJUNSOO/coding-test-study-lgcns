# 빡구현
def solution(numbers, hand):
    answer = ''
    left = [3,0]
    right = [3,2]
    cent = [0,0]
    for i in numbers:
        if i==1 or i==4 or i==7:
            answer+='L'
            if i==1:
                left = [0,0]
            elif i==4:
                left = [1,0]
            else:
                left = [2,0]
        elif i==3 or i==6 or i==9:
            answer+='R'
            if i==3:
                right = [0,2]
            elif i==6:
                right = [1,2]
            else:
                right = [2,2]
        else:
            if i==2:
                cent = [0,1]
            elif i==5:
                cent = [1,1]
            elif i==8:
                cent = [2,1]
            elif i==0:
                cent = [3,1]
            guri = abs((left[0]-cent[0]))+abs((left[1]-cent[1]))
            guri2 = abs((right[0]-cent[0]))+abs((right[1]-cent[1]))
            if guri>guri2:
                answer+='R'
                right = cent
            elif guri<guri2:
                answer+='L'
                left = cent
            else:
                if hand=='right':
                    answer+='R'
                    right = cent
                else:
                    answer+='L'
                    left = cent
    return answer