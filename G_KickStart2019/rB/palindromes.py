# 
# 
# 1/2 not fast enough for large data set
# 
# 

import sys
import itertools

T = input()
ans = {}

for x in xrange(T):
    N, Q = map(int, raw_input().split())
    blocks=list(raw_input())
    tot=0
    for y in xrange(0, Q):
        L, R = map(int, raw_input().split())
        L = L-1
        subset = []
        
        for b in xrange(L, R):
            subset.append(blocks[b])

        cont1 = False
        cont2 = 0

        if len(subset) == 1:
            tot = tot+1
            continue
        elif len(subset) % 2 == 0:
            for ss in subset:
                if subset.count(ss) % 2 != 0 :
                    cont1 = True
                    break
            if cont1 == True:
                continue
            else:
                tot = tot+1
        elif len(subset) % 2 != 0:
            dex = {}
            sum = 0
            for ss in subset:
                if subset.count(ss) % 2 != 0:
                    dex.update({ss : 1})
                    if len(dex) > 1:
                        break
                else:
                    continue
            if len(dex) > 1:
                continue
            else:
                tot = tot+1
        else:
            tot = tot+1


    ans.update({x+1: tot})

for case, total in ans.iteritems():
    print "Case #{}: {}".format(case, total)
    sys.stdout.flush()