T = int(input())
for x in range(1, T + 1):
    N = int(input())
    L = input().split()
    for m in range(len(L)):
        L[m] = int(L[m]) 
    cost = []
    for i in range(1, len(L)):
        j = L.index(min(L[i-1 : len(L)])) + 1
        # print(L[j-1 : : -1])
        if(i == 1):
            L[i-1 : j] = L[j-1 : : -1]
        else:
            L[i-1 : j] = L[j-1 : i-2 : -1]
        # print("i={}, j={}, L={}".format(i, j, L))
        cost.append(j - i + 1)
    y = sum(cost)
    print("Case #{}: {}".format(x, y))

