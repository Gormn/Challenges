import sys

def solve(a, b):
    q = (a+b)/2
    print q
    sys.stdout.flush()
    response = raw_input()
    if response == "CORRECT":
        return 
    elif response == "TOO_BIG":
        b = q
    else: 
        a = q
    solve(a,b)
            
T = input()
for x in xrange(T):
    a, b = map(int, raw_input().split())
    x = input()
    solve(a, b)


        