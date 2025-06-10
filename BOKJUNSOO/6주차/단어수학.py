# 어떻게하면 최댓값을 출력할 수 있을까?
# 그리디인것이 체감됐지만, 어떻게 구현해야할까를 생각해보면
# 9, 8 .. 내림차순으로 철자마다 값을 딕셔너리 형태로 저장한다.

# 이때
# 모든 단어의 입력에 대해서
# 9를 지정하는 경우의 수를 고려해보면

# case1) 가장 긴 문자열의 가장 앞에 오는 단어를 9로 지정해준다.
# --> 주어진 단어가 10개 이하이므로, 
# 두번째로 긴 단어의 첫번째 오는 철자가 모두 9로 한다 해도
# 가장 긴 단어의 첫번째 오는 철자를 9로 할때와 값이 같다!

# case2) 가장 긴 문자열이 2개이상이라면, 가장 빈도수가 많은 철자를 9로 지정한다.
# --> 예를들어 
# adb
# adc
# bca 의 경우에서
# b보다는 a를 9로 지정하는것이 더 큰 값을 얻을 수 있다.
# 9는 이미 사용된 철자가 존재하므로, 8을 맵핑시킬 철자가 필요한데
# b를 이에 맵핑시키면 된다.
# 따라서 긴 단어부터 맨 앞에 오는 철자에 값을 맵핑시키고,
# 단어의 길이를 줄인후, 다른 단어들과 비교해가며 모든 문자열의 길이가 0이 될때까지 진행하면 된다.
# 단어의 철자들을 비교해가는 과정에서 이미 맵핑이 되어있다면 바로 문자열을 줄인다.

# 철자들을 모두 맵핑 시키고 난 후 (dictionary) 기존 문자에 값을 replace 하여 답을 출력한다.


N = int(input().strip())
words = []
for _ in range(N):
    words.append(input())

# 모든 알파벳의 가중치 초기화
weight = {}
for word in words:
    alpha = set(word)
    for i in alpha:
        weight[i] = 0

for w in words:
    L = len(w)
    for i, v in enumerate(w):
        power = L - 1 - i # 인덱스가 작을수록 (앞에 오는 문자일 수록 큰 값을 주어야함)
        weight[v] = weight.get(v) + (10 ** power)

# 가중치 내림차순으로 정렬
# 가중치가 같을 경우에 x[0] 알파벳 순서대로 정렬
chars_sorted = sorted(weight.items(), key=lambda x: (-x[1], x[0]))
mapper = {}
digit = 9

# 각 알파벳에 가중치를 9부터 순서대로 부여
for ch, _ in chars_sorted:
    mapper[ch] = digit
    digit -= 1
    if digit < 0:
        break

# 단어들을 치환해 합 계산
answer = 0
for word in words:
    target = ""
    for alpha in word:
        target += str(mapper[alpha])
    answer += int(target)
print(answer)
