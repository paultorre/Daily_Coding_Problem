import collections

def isAna(s1, s2):
    """ Returns whether two strings are anagrams of one another or not.

        Uses a Counter dictionary to determine the letter count of each word and compares for equality.
        This O(n) time (really O(n) + O(n) + O(n) for creation + creation + comparison, but asymptotically O(n)

        Args:
            s1: string 
            s2: string

        Returns:
            True: s1 IS an anagram of s2
            False: s1 IS NOT an anagram of s2

    """
    c1 = collections.Counter(s1)
    c2 = collections.Counter(s2)
    return c1 == c2

def anagram_indexes_brute(w, s):
    """ Returns indexes of s where a substring that is an anagram of w begins

    Args:
        w: word to search s for
        s: string

    Returns:
        List of indexes in s where an anagram of w begins
    """
    ans = []
    i = 0
    while i < len(s) - len(w) + 1:
        if isAna(w,s[i:i+len(w)]):
            ans.append(i)
        i += 1
    return ans

w = 'ab'
s = 'abxaba'
print(anagram_indexes_brute(w,s))

# Optimized Version !

def anagram_indexes_opt(w, s):
    ans = []
    w_arr = [0 for _ in range(26)]
    s_arr = [0 for _ in range(26)]

    for c in w:
        w_arr[ord(c)-97] += 1

    i = 0
    for _ in range(len(w)):
        s_arr[ord(s[i])-97] += 1
        i += 1
    if w_arr == s_arr:
        ans.append(0)
    
    while i < len(s):
        s_arr[ ord(s[i-len(w)])-97 ] -= 1
        s_arr[ ord(s[i])-97 ] += 1
        if s_arr == w_arr:
            ans.append(i - len(w) + 1)
        i += 1
    return ans
    

print(anagram_indexes_opt(w,s))
