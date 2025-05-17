n, k = map(int, input().split())

tosso = [[0,0]] # 항목은 0부터 시작
ee = [[0]*(k+1)] # 가로줄은 무게, 세로줄은 각 항목(무게도 0부터 시작)

for i in range(n):
    tosso.append(list(map(int,input().split())))
    ee.append([0]*(k+1))

# ee 테이블을 칸별로 돌면서...
for i in range(1,n+1):
    for j in range(1,k+1):
        # 현재 항목의 무게와 가치
        muge = tosso[i][0]
        kachi = tosso[i][1]
        
        # j(가로줄-무게)가 현재 들고있는 항목의 무게보다 작으면 이전값을 그대로(못넣으니까)
        if j<muge:
            ee[i][j] = ee[i-1][j]
        # 같거나 크면 이전값과 현재가치+이전항목 중 현재무게 뺀 것의 값중 최대값
        # (최대 무게에서 지금 들고있는 무게를 제한 것중 최대값을 구하면 되니까)
        else:
            ee[i][j] = max(kachi+ee[i-1][j-muge],ee[i-1][j])
            
print(ee[n][k])