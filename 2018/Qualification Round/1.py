def damage_one_swap_smaller(P,current_damage,current_d):
    for i in range(len(P)-1,0,-1):
        if i >= 2:
            if P[i] != P[i-1] and P[i-1] == "C":
                P[i],P[i-1] = P[i-1], P[i]
                for j in range(i-1,len(P)):
                    if P[j] == "C":
                        current_d[j] = current_d[j-1] * 2
                        current_damage[j] = current_damage[j-1]
                    else:
                        current_damage[j] = current_damage[j-1] + current_d[j-1]
                        current_d[j] = current_d[j-1]
                return current_damage, current_d, 0
            else:
                continue
        elif i == 1:
            if P[0] == P[1]:
                return current_damage, current_d, -1
            elif P[0] != P[1] and P[0] == "C":
                P[0],P[1] = P[1],P[0]
                current_d[0] = 1
                current_damage[0] = 1
                current_d[1] = 2
                current_damage[1] = 1
                for j in range(2,len(P)):
                    if P[j] == "C":
                        current_d[j] = current_d[j-1] * 2
                        current_damage[j] = current_damage[j-1]
                    else:
                        current_damage[j] = current_damage[j-1] + current_d[j-1]
                        current_d[j] = current_d[j-1]
                return current_damage, current_d, 0
def run_test():
    D,P = raw_input().split(" ")
    D = int(D)
    P = list(P)
    result = 0
    current_damage = {}
    current_d = {}
    c = 1
    d = 0
    i = 0
    for p in P:
        if p == "C":
            c = c * 2
        else:
            d = d + c
        current_damage[i] = d
        current_d[i] = c
        i = i + 1
    # print("current_damage0: "+str(current_damage))
    # print()
    # print("current_d0: "+str(current_d))
    # print("P0: "+str(P))
    while D < current_damage[len(P)-1]:
        current_damage, current_d, r = damage_one_swap_smaller(P,current_damage, current_d)
        result = result + 1
        # print("############$$$$$#######")
        # print("current_damage: "+str(current_damage))
        # print("current_d: "+str(current_d))
        # print("r: "+str(r))
        # print("result: "+str(result))
        # print("P: "+str(P))
        if r == -1:
            return -1
    return result

T = int(input()) + 1
for i in range(1, T):
    t = run_test()
    if t == -1:
        print("Case #{}: ".format(i)+"IMPOSSIBLE")
    else:
        print("Case #{}: {}".format(i, t))
