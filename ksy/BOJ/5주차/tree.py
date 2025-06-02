n = int(input())

tree = {}

# 딕셔너리를 사용하면 연결된 그래프를 쉽게 확인
for i in range(n):
    a,b,c = input().split()
    tree[a] = [b,c]
    
#a 키의 0번째가 왼쪽 자식, 1번째가 오른쪽 자식
#전위: 부모(a)를 항상 먼저 표기
def chonui(a):
    if a != '.':
        print(a,end='')
        chonui(tree[a][0])
        chonui(tree[a][1])
#중위: 왼쪽 자식부터 먼저 불러와야 하므로 일단 재귀로 왼쪽 끝까지 가
#끝까지 가면 왼쪽 자식이 부모가 되므로 먼저 표시되고 그 다음 그의 부모가 표기, 마지막이 오른쪽 탐색
def chongui(a):
    if a != '.':
        chongui(tree[a][0])
        print(a,end='')
        chongui(tree[a][1])
#후위: 중위와 마찬가지지만 부모를 맨 나중에 표시해야 하므로 print문을 맨 뒤로
def huui(a):
    if a != '.':
        huui(tree[a][0])
        huui(tree[a][1])
        print(a,end='')

chonui('A')
print()
chongui('A')
print()
huui('A')
