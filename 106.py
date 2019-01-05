# Brute Force
# Assuming you have to land on the last spot.
# O(n) - Time
# O(1) - Space

def can_make_hops(arr):
    i = 0
    while arr[i] != 0:
        i += arr[i]

    return i == len(arr) - 1
a = [2, 0, 1, 0]
b = [1, 1, 0, 1]
print(can_make_hops(a),can_make_hops(b))