
import sys

T = input()
cases = {}
steps = {}

possibility= ''
possible = 'POSSIBLE'
impossible = 'IMPOSSIBLE'
route = []
validroute = []

def checkAgainst(gridly, r, c):
    print 'outside: ', gridly, r, c 
    for b, g in gridly:
        print " R: {} C: {} B {} G: {}".format(r, c, b, g)
        if r != b and c != g and r-c != b-g and r+c != b+g:
            if len(route) == 0:
                route.append(tuple((r, c)))
                route.append(tuple((b, g)))
            else: 
                route.append(tuple((b, g)))
            print 'delete: ', tuple((r, c))
            print gridly
            gridly.remove(tuple((r, c)))
            print gridly
            r = b
            c = g
            if len(gridly) == 1:
                possibility = possible
                validroute = list(route)
                break
            checkAgainst(gridly, r, c)
            break
        else:
            possibility = impossible
            if b == len(gridly):
                break


for x in xrange(T):
    R, C = map(int, raw_input().split())
    grid = []
    for r in xrange(1, R+1):
        for c in xrange(1, C+1):
            grid.append(tuple((r, c)))
            
    
    routegrid = list(grid)

    for r, c in grid:

        print r, routegrid
        checkAgainst(list(routegrid), r, c)
        print 'possibility: ', possibility
        if possibility == possible:
            break
        grid = []
        route = []
        validroute = []
        routegrid = list(grid)



    cases.update({x+1: possibility})
    steps.update({x+1: validroute})
    
for case, string in cases.iteritems():
    print "Case #{}: {}".format(case, string)
    if string == 'POSSIBLE':
        for r, c in steps[case]:
            print r,c 
    sys.stdout.flush()