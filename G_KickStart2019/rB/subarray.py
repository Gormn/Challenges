# 
# WRong solution
# 
# 
# 

import sys
import itertools

T = input()
ans = {}

for x in xrange(T):
    N, S = map(int, raw_input().split())
    trink_id=map(int, raw_input().split())
    tot=0
    trink_count = {}
    
    for trink in trink_id:

        if not trink in trink_count:
            trink_count[trink] = 1
        else:
            trink_count[trink] +=1
    
    most = min(len(trink_count), N)
    
    trinkets = []

    for trink, count in trink_count.iteritems():
        trinkets.append(trink)
    
    # for b in xrange(S, most):
    #     for bb in xrange(b, N):
    #         for 
    
    trinkets.sort
    print trinkets

    for i in xrange(1, len(trinkets)):
        sum = trink_count[trinkets[i-1]] + trink_count[trinkets[i]]
        if (sum > tot):
            tot = sum
        
    
    ans.update({x+1: tot})

for case, total in ans.iteritems():
    print "Case #{}: {}".format(case, total)
    sys.stdout.flush()
