# DFS는 효율성 통과 못해요

karo = [0,0,1,-1]
sero = [1,-1,0,0]

# 탐색시간이 담길 변수
ee = []
import copy

# 인자는 맵, 현재위치(n/m), 방문체크, 시간카운트
def tosso(maps,n,m,visited,count):
    
    # DFS는 재귀함수라 먼저 돌은 visited에 영향을 받을 수 있어 깊은복사 사용 
    dachs = copy.deepcopy(visited)
    
    # DFS탐색 개시
    for i in range(4):
        dn = n+karo[i]
        dm = m+sero[i]
        
        if 0<=dn<len(maps) and 0<=dm<len(maps[0]):
            
            if maps[dn][dm] == 1 and dachs[dn][dm]==0:
                # 만약 도착지에 다다랐다면 탐색시간 배열에 넣고 리턴
                if dn==len(maps)-1 and dm==len(maps[0])-1:
                    ee.append(count+1)
                    return
                # 아니면 방문위치에 1 찍고 다음위치에서 재귀
                else:
                    dachs[dn][dm] = 1
                    tosso(maps,dn,dm,dachs,count+1)
        
    
    return -1


def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    
    #for i in range(n):
    #    print(maps[i])
    
    # 방문했음을 담는 배열
    # 방문했을 경우 해당 위치에 1 표시
    visited = [[0 for i in range(m)] for j in range(n)]
    visited[0][0] = 1
    
    tosso(maps,0,0,visited,1)
    
    # 위치까지 못갔을 경우(완료시간 배열에 아무것도 없으면)
    if len(ee)==0:
        answer = -1
    else:
        answer = min(ee)
    
    return answer