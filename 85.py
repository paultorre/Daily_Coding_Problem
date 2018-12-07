# This was a tricky problem that relied on a flash of insight.  In this case, I was more or less thinking heuristaclly
# about solving this problem.  I thought a lot about bitwise operations and eventually realized
# that somehow I should be adding the two numbers together, and that one of them should be 0 and one should
# be the desired number to return.  I then thought about how I could achieve this with the third variable b.
# The resulting formula produced the desired result. 
#
#
# Time - O(1)
# Space - O(1)

def go(x,y,b):
    return (x * b) + (y * (b^1))

print(go(100,2,0))




#  To help with visualization.
#
# x 100101
#
# y 100111
#
# b 000000        --> y
#
# b 000001       --> x
