import math
T = int(input())

for x in range(1, T + 1):
    y, current_K = 0, 0
    # print(x)
    # [N, B] = int(input().split())
    N, K = map(int, input().split())
    # print("N is {} \nK is {}".format(N, K))
    S = input()
    # S = S.upper()
    for i in range(math.floor(len(S)/2)):
        # print(i)
        if S[i] != S[N-i-1]:
            current_K += 1
    # print(current_K)
    if current_K < K:
        y = K - current_K
    print("Case #{}: {}".format(x, y))
    