n,k = map(int,input().split())

# 일의자리는 1~9 9개
# 십의자리는 10~99 90*2 = 180개
# 백의자리는 100~999 900*3 = 2700개...
# 이렇게 k에서 각 자리를 올라가며 빼주면서 더 이상 안빼지도록

answer = 0 # k가 어디서부터 시작하는지를 찾기
jari = 1 # 자리수 (9n * m에서 m)
tosso = 9 # 자리수 (9n * m에서 9n)


while k>(tosso*jari):
    k -= (tosso*jari) # 계속 빼주고
    answer += tosso # 자리 순번을 올려
    tosso *= 10
    jari +=1
    
answer = (answer + 1) + (k-1)//jari
# answer + 1은 10, 100, 1000... 이렇게 될 거고(2의 자리면 10)
# 아까 계속 뺀 k를 자리수로 나눠준 몫을 더하면 k번째에 해당하는 수가 무엇인지를 확인 가능 
# k가 아닌 k-1인 이유는 인덱스가 0부터 시작하기 때문

if answer>n:
    print (-1)
else:
    # 이렇게 구한 수를 이번에는 나머지의 인덱스화 하면 해당 수를 알 수 있어
    print(str(answer)[(k-1)%jari])
    
    
# n 20 k 23
# tosso 90 jari 2 sijak 9 k = 14
# 10 + 13//2 = 16 k가 속한 수는 16
# 16[13%2] = 6 진짜 k번째에 해당하는 수는 6