# The solution in python

import sys


T = input()
dict = {}

for x in xrange(T):
    N, P = map(int, raw_input().split())
    stud=list(map(int,raw_input().split()))
    stud.sort()
    sum = 0
    for i in xrange(0, P):
        sum += stud[i]
    tot = stud[P-1] * P - sum
    
    for s in xrange(P, N):
        sum -= stud[s-P]
        sum += stud[s]
        index = s-P+1
        train = stud[s] * P - sum

        if (train < tot):
            tot = train

    dict.update({x+1: tot})

for case, total in dict.iteritems():
    print "Case #{}: {}".format(case, total)
    sys.stdout.flush()