def test_methode():
    n = list(raw_input())
    control = True
    while control:
        for i in range(len(n)-1):
            if n[i] <= n[i+1]:
                continue
            else:
                n[i] = str(int(n[i])-1)
                for j in range(i+1,len(n)):
                    n[j] = "9"
        if n == sorted(n):
            control = False

    if n[0] == "0":
        del n[0]

    return int("".join(n))

T = int(raw_input())
for k in xrange(1, T + 1):
    print "Case #{}: {}".format(k, test_methode())
