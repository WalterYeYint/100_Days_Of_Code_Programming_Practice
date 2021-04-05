import itertools
T = int(input())
for x in range(1, T + 1):
    idx = 0
    temp = []
    
    def Recursion(idx):
        if idx != len(space_idx)-1:
            for i in K:
                Recursion(idx + 1)
        else:
            for i in M[idx]:
                temp.append(i)

    C = []
    K = ['C', 'J']
    X, Y, S = input().split()
    X, Y = int(X), int(Y)
    # print(type(X))
    # print(type(Y))
    # print(type(S))
    space_idx = [pos for pos, char in enumerate(S) if char == "?"]
    M = [K for i in range(len(space_idx))]
    print(M)

    # combi = itertools.permutations(['C','J'], 2)
    # for c in list(combi):
    #     print(c)

    for i in K:
        for j in K:
            for k in K:
                print(i, j, k)

    # while idx != len(space_idx):
    #     idx += 1
    #     for i in range(len(space_idx)):
    #         L = S
    #         for j in range(len(space_idx)):
    #             L = L.replace("?", M[j][i], 1)
    #             print("j={}, M = {}, L={}".format(j, M[j][i], L))
    #         C.append(L)
    #         print(C)



