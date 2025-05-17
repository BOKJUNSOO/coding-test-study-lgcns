n = int(input())

tosso = [[]] * n

for i in range(n):
    tosso[i] = list(map(int,input().split()))

#i가 첫번째면 다음건 두,세번째거만
#i가 두번째면 다음건 첫,세번째거만
#i가 세번째면 다음건 첫,두번째거만
for i in range(1,n):
    tosso[i][0] = min(tosso[i-1][1],tosso[i-1][2])+tosso[i][0]
    tosso[i][1] = min(tosso[i-1][0],tosso[i-1][2])+tosso[i][1]
    tosso[i][2] = min(tosso[i-1][0],tosso[i-1][1])+tosso[i][2]
    
print(min(tosso[n-1]))