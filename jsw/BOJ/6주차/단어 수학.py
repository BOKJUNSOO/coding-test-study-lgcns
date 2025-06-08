N = int(input())
N_dict = {}
alpha_list= []
num = 9
ans = 0
for _ in range(N):
    alpha = input()
    alpha_list.append(alpha)
    for i in range(len(alpha)):
        if alpha[i] not in N_dict:
            N_dict[alpha[i]] = 10**(len(alpha) - (i +1))
        else:
            N_dict[alpha[i]] += 10**(len(alpha) - (i + 1))
num_list = list(N_dict.values())
num_list.sort(reverse=True)
for i in num_list:
    ans += num * i
    num -= 1
print(ans)
