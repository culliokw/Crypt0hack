from math import sqrt

# Using custom function to check up to sqrt(n)
def is_prime(x):
    if(x>1):
        for i in range(2,int(sqrt(x)) + 1):
            if (x % i == 0):
                return False
        return True
    else:
        return False

exps = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
candidates = [x for x in range(851,1000) if is_prime(x)]
print(candidates)
final = list()

# run through the candidate primes starting at largest value in the base power list
# We then need to run up to that candidate number and check that the equality statement for the test variable assignment is 
# true for all successive powers since x+1 is equal to a value times the exponent modular our three digit prime p.
# If all True values for this equality for the exponent list, we have found our final tuple of integers p and x per the task.
for p in candidates:
    for x in range(1,p):
        test = [ (x*exps[y])%p == exps[y+1] for y in range(0,len(exps)-1)]
        if all(test):
            final=[p,x]
            
# voila
print("crypto{",final[0],",",final[1],"}",sep="")
