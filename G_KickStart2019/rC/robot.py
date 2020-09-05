import sys

T = input()
ans = {}

for x in range(T):
    N, R, C, SR, SC = map(int, raw_input().split())
    inst=list(raw_input())
    pos = [SR, SC]
    seen = []
    seen.append([pos[0], pos[1]])

    for i in inst:
        if i == 'N':
            pos[0] -= 1
            if pos in seen:
                while pos in seen:
                    pos[0] -= 1
            seen.append([pos[0], pos[1]])
        elif i == 'S':
            pos[0] +=1
            if pos in seen:
                while pos in seen:
                    pos[0] +=1
            seen.append([pos[0], pos[1]])
        elif i == 'E':
            pos[1] += 1
            if pos in seen:
                while pos in seen:
                    pos[1] += 1
            seen.append([pos[0], pos[1]])
        elif i == 'W':
            pos[1] -= 1
            if pos in seen:
                while pos in seen:
                    pos[1] -= 1
            seen.append([pos[0], pos[1]])

    ans.update({x+1: [pos[0], pos[1]]})

for case, pos in ans.iteritems():
    print "Case #{}: {} {}".format(case, pos[0], pos[1])
    sys.stdout.flush()