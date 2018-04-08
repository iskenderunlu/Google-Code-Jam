

def run_test():
    n = int(raw_input())
    L = list(raw_input().split(" "))
    done = False
    while not done:
        done = True
        for i in range(n-2):
            if L[i] > L[i+2]:
                done = False
                L[i],L[i+2]=L[i+2],L[i]

    for i in range(n-1):
        if L[i] <= L[i+1] and i < n-2:
            continue
        elif L[i] <= L[i+1] and i == n-2:
            return 0
        elif L[i]>L[i+1]:
            return i

T = int(input()) + 1
for i in range(1, T):
    t = run_test()
    if t == 0:
        print("Case #{}: ".format(i)+"OK")
    else:
        print("Case #{}: {}".format(i, t))
