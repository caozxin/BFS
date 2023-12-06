from typing import (
    List,
)

class Solution:
    """
    @param arr: an array of non-negative integers
    @return: minimum number of elements
    """
    def min_elements(self, arr: List[int]) -> int:
        # write your code here

        if not arr:
            return
        input_arr = arr.copy()
        queue = [[]] # queue is the list of subsets. you cannot use set() here since there might be repeats
        index = 0

        while index < len(queue):
            subset = queue[index]
            index += 1
            for each_num in input_arr:
                if subset and subset[-1] >= each_num:
                    continue
            
                queue.append(subset + [each_num])
                curr_sum = sum(queue[-1])
                rest_sum = sum(input_arr) - curr_sum
                print(queue[-1], sum(queue[-1]), queue[:-1], rest_sum )
                if curr_sum > rest_sum:
                    print(len(queue[-1]))
                    return len(queue[-1])

