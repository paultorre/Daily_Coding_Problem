def reverse_words(s):
    """ Trivial algorithm
        
        Args:
            s: sentence string delimited by space

        Returns:
            String with words in sentence appearing in reverse order
    """
    w = s.split(' ')
    return ' '.join(w[::-1])

def inplace(s):
    """ Reverses all the words in a string in-place.  Very hacky and unclear. Gist is that it finds the end
        of the fist word, bubbles all the letters to the end of the string, update the 'end'
        index, and repeat until the end is the beginnning.  Now the words appear in reverse order.

        Args:
            s: sentence string delimited by space

        Returns:
            String with words in sentence appearing in reverse order
    """
    arr = [c for c in s]
    
    end = len(arr) - 1
    while end > 0:
        i = 0
        while arr[i] != ' ':
            i += 1
        i -= 1
        while i >= 0:
            i2 = i
            while i2 < end:
                arr[i2],arr[i2+1] = arr[i2+1],arr[i2]
                i2 += 1
            end -= 1
            i -= 1
        i2 = 0
        while i2 < end:
            arr[i2],arr[i2+1] = arr[i2+1],arr[i2]
            i2 += 1
        end -= 1
            
    return ''.join(arr)

s = 'Hi my name is paul'
print(inplace(s))
print(reverse_words(s))