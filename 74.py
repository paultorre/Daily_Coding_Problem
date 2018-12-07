from collections import defaultdict
from math import gcd

#   Brute force solution. 
#   Really bad but will get the answer.
#
#   Time - O(n^2)
#   Space - O(n^2)
def brute_force_bad(n,x):
    memo = defaultdict(int)
    for i in range(1,n+1):
        for j in range(1,n+1):
            memo[i*j] += 1
    return memo[x]

#   Should be some sort of math-y shortcut, but can;t figure it out. GCD and Pascal's
#   Triangle or something.
#
#
#
def num_appearances(n,x):
    return gcd(n,x) - 2 if x > n else gcd(n,x)

ans = brute_force_bad(6,2)
print(ans)
