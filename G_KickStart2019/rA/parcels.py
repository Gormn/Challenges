# Unfinished

import sys


T = input()
cases = {}

for x in xrange(T):
    R, C = map(int, raw_input().split())
    yes = {}
    no = {}
    dex = 0
    for s in xrange(R):
        row = list(map(int,raw_input()))
        print row
        for t in xrange(len(row)):
            dex += 1
            print row[t]
            if row[t] == 1:
                yes.update({dex : [s,t]})
            else: 
                no.update({dex : [s,t]})
    # for key, values in yes:
        # distance =
    print yes
    print no

for case, total in yes.iteritems():
    print "Case #{}: {}".format(case, total)
    sys.stdout.flush()



