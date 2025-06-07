n = int(input())

dano = []

for i in range(n):
    dano.append(input())

jari = {}

# 각 알파벳별로 어떤 자리에 몇 번씩 들어가는 딕셔너리 만들어주기
# AAA AAA 인 경우 A는 백/십/일의자리에 2번씩 등장하므로 222 이런식
for i in range(n):
    for j in range(len(dano[i])):
        if dano[i][j] in jari:
            jari[dano[i][j]] += 10 ** (len(dano[i])-j-1)
        else:
            jari[dano[i][j]] = 10 ** (len(dano[i])-j-1)

myotbon = []

for i in jari.values():
    myotbon.append(i)

# 위에서 구한 자리수를 리스트에 넣은 후 내림차순 정렬하고    
myotbon.sort(reverse = True)

answer = 0
sijak = 9

# 9부터 시작해서 제일 큰 것부터 곱해주고 더하면 끝!
for i in myotbon:
    answer += sijak * i
    sijak -= 1
    
print(answer)
    