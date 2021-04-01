
from typing import List


class Solution():

    def binary_search(self, arr:List, item: int):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = arr[mid]
            if guess == item:
                return mid
            if guess > item:
                high = mid -1
            else:
                low += mid
        return None
            

my_arr = [i  for i in range(100) if i % 2 !=0]
print(my_arr)
result = Solution().binary_search(my_arr, 5)
print(result)
result = Solution().binary_search(my_arr, 100)
print(result)
