
def test_methode():
    S, K = raw_input().split(" ")
    S = list(S)
    K = int(K)
    result = 0
    for i in range(len(S)-K+1):
        if S[i] == "+":
            continue
        else:
            for j in range(i , i+K):
                if S[j] == "+":
                    S[j] = "-"
                else:
                    S[j] = "+"
            result = result + 1
    if "-" not in S:
        return result
    else:
        return "IMPOSSIBLE"

T = int(raw_input())
for i in xrange(1, T + 1):
    if test_methode == "no":
        print "Case #{}: IMPOSSIBLE".format(i)
    else:
        print "Case #{}: {}".format(i, test_methode())
