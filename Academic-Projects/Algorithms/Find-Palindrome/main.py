# Determine if a tuple can be made into a palindrome by removing exactly one element
import math 


def slice_palindrome(palin, length):
    length_half = length // 2
    if length % 2 == 0:
        palin_front = palin[0:length_half]
        palin_back = palin[length_half:]
    else:
        palin_front = palin[0:length_half + 1]
        palin_back = palin[length_half + 1:]
    return palin_front, palin_back


def remove_element(palin, index):
    return palin[:index] + palin[index + 1:]


def is_palindrome(palin):
    return (palin == palin[::-1])


def remove_palindrome_element(palin):
    return remove_element(palin, len(palin) // 2)

    
def check_palindrome(palin, length):
    palin_front, palin_back = slice_palindrome(palin, length)
    length_half = length // 2
    for index, (char_front, char_back) in enumerate(zip(palin_front, reversed(palin_back))):
        if (char_front != char_back):
            palin_front_removed = remove_element(palin_front, index) + palin_back
            palin_back_removed = palin_front + remove_element(palin_back, (length_half - index) - 1)
            if (is_palindrome(palin_front_removed)):
                return palin_front_removed
            elif (is_palindrome(palin_back_removed)):
                return palin_back_removed
            else:
                return None
    return None


def find_palindrome(pattern):
    if type(pattern) is tuple:
        length = len(pattern)
        if length <= 2:
            return None
        elif (is_palindrome(pattern)):
            return remove_palindrome_element(pattern)
        else:
            answer = check_palindrome(pattern, length)
            return answer
    else:
        return None
