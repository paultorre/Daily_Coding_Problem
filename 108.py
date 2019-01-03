def is_shift(a, b):
    """ Returns if b can be found by shifting letters in a

        Args: 
            a: string
            b: string

        Returns:
            True: b CAN be shifted to get a
            False: b CANNOT be shifted to get a
    """
    i = b.index(a[0])
    a_i = 0
    while a_i < len(a):
        if a[a_i] != b[i]:
            return False
        if i == len(b)-1:
            i = 0
            a_i += 1
        else:
            i += 1
            a_i += 1

    return True

a = 'abc'
b = 'acb'
print(is_shift(a,b))