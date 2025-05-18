# 1,2,3은 고정값
tosso = [1,2,4]
# [1,2,4,7,13,...] 5까지 가지수 세어보면
# 간단한 dp: in=i(n-1)+i(n-2)+i(n-3)

# 미리 만들어놓기-그때그때 만들면 시간초과    
for i in range(3,1000001):
        # 이것도 미리 나눠놓지 않으면 메모리초과
        tosso.append((tosso[i-3]+tosso[i-2]+tosso[i-1])%1000000009)

for n in range(int(input())):
    k = int(input())
    print(tosso[k-1])