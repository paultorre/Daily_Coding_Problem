def find_one(nums):
    tot = sum(nums)
    print(tot)
    for n in nums:
        tot -= (n*3)

    return tot

a = [6, 1, 3, 3, 3, 6, 6]
b = [13, 19, 13, 13]

print(find_one(a))
print(find_one(b))