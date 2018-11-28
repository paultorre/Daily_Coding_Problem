'''Given an array of Integers, return the length of the longest increasing subsequence'''
def longest_inc_subsequence(arr):
    memo = {}

    def dp(i):
        if i in memo:
            return memo[i]
        if i == 0:
            memo[0] = 1
            return 1
        ans = max([dp(j) if arr[j] <= arr[i] else 0 for j in range(len(arr[:i]))]) + 1
        memo[i] = ans 
        return memo[i]
    dp(len(arr)-1)
    
    return max(memo.values())

arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(longest_inc_subsequence(arr))