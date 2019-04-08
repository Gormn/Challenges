import sys

def primes(n):
    siev = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if siev[i]:
            siev[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if siev[i]]

T = input()
cases = {}

for x in xrange(T):
    N, L = map(int, raw_input().split())
    all_primes = primes(N) 
    input_nums=list(map(int,raw_input().split()))
    let_primes = []
    final_string = ''
    value_array = []

   
    for index in xrange(0, L): 
        if len(value_array) > 0:
            if input_nums[index] % value_array[index] == 0:
                value_array.append(input_nums[index] / value_array[index])
            elif input_nums[index] % value_array[index-1] == 0:
                first_num = value_array[index]
                second_num = value_array[index-1]
                value_array[index-1] = first_num
                value_array[index] = second_num
                value_array.append(input_nums[index] / value_array[index])

        else:
            for prime in all_primes:
                if input_nums[index] % prime == 0:
                    value_array.append(prime)
                    value_array.append(input_nums[index] / prime)
                    break
    
    let_primes = list(value_array)
    let_primes = list(dict.fromkeys(let_primes))
    let_primes.sort()

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
    keys = {}

    for r in xrange(0, 26):
        keys[let_primes[r]] = letters[r]

    for value in value_array:
        final_string = final_string + keys[value]
                

    cases.update({x+1: final_string})
    
for case, string in cases.iteritems():
    print "Case #{}: {}".format(case, string)
    sys.stdout.flush()
                

        
        

        
