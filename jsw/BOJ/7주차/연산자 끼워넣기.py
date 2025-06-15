N = int(input())
num_list = list(map(int,input().split()))
calc_list = list(map(int,input().split()))

minn = 10**9
maxx = -10**9

def backtracking(depth, temp, plus, minus,multiply, divide):
    global minn, maxx
    if depth == N:
        minn = min(temp, minn)
        maxx = max(temp, maxx)
    if plus > 0:
        backtracking(depth+1, temp + num_list[depth],plus-1, minus, multiply, divide)
    
    if minus > 0:
        backtracking(depth+1, temp - num_list[depth],plus, minus-1, multiply, divide)
    
    if multiply > 0:
        backtracking(depth+1, temp * num_list[depth],plus, minus, multiply-1, divide)
    
    if divide > 0:
        backtracking(depth+1, int(temp / num_list[depth]),plus, minus, multiply, divide-1)
backtracking(1,num_list[0],calc_list[0],calc_list[1],calc_list[2],calc_list[3])
print(maxx)
print(minn)
