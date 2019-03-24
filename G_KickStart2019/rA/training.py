# Passed 1/2 Failed 2/2

import sys

T = input()
dict = {}

for x in xrange(T):
    N, P = map(int, raw_input().split())
    stud=list(map(int,raw_input().split()))
    minTop = N-1-(N-P)
    stud.sort()
    tot=sum(stud) * sum(stud)
    for s in xrange(minTop, N):
        train = 0
        index = s-P+1
        for t in xrange(s-P+1, s):
            dif = stud[s] - stud[t]
            train += dif
        if (train < tot):
            tot = train

    dict.update({x+1: tot})

for case, total in dict.iteritems():
    print "Case #{}: {}".format(case, total)
    sys.stdout.flush()