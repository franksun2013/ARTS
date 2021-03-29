from typing import List

class Solution():

    @staticmethod
    def get_low(arr: List[int]) -> int:
        smallest = arr[0]
        smallest_index = 0
        for i in range(1, len(arr)):
            if smallest > arr[i]:
                smallest = arr[i]
                smallest_index = i
        return smallest_index

    def quick_sort(self, arr: List[int]) -> List:
        new_arr = []
        for i in range(len(arr)):
            smallest_index = self.get_low(arr)
            new_arr.append(arr.pop(smallest_index))
        return new_arr


a = [1, 2, 3, 4]
b = [5, 4, 3, 2]
c = [19, 23121,234,124543,89, 2310]
print(Solution().quick_sort(a))
print(Solution().quick_sort(b))
print(Solution().quick_sort(c))
