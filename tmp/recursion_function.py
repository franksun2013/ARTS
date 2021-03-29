

from typing import List


def recursion_print(n: int):
    print(n)
    n -=1
    if n == 1:
        return "over"
    recursion_print(n)
    

recursion_print(10)


def recursion_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + recursion_sum(arr[1:])



print(recursion_sum([1, 2, 3, 4, 5]))
