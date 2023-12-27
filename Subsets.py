from typing import (
    List,
)
from collections import deque
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    """
    def subsets_dfs(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        res = []
        def dfs(i, cur):
            if i == n: # when all index went over, we return --> base case
                cur.sort()
                res.append(cur)
                return

            dfs(i + 1, cur + [nums[i]]) # this is for a binary choice to include the number in the subset at each level.
            dfs(i + 1, cur) # this is for a binary choice to NOT include the number in the subset at each level.

        dfs(0, [])

        return res
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        queue = [[]]
        index = 0

        while index < len(queue):
            subset = queue[index]
            index += 1
            for num in nums:
                if subset and subset[-1] >= num:
                    continue
                queue.append(subset + [num])

        return queue


    def subsets_fromJZSF(self, nums):
        results = []

        if not nums:
            return results

        nums.sort()

        # BFS
        queue = deque()
        queue.append([])

        while queue:
            subset = queue.popleft()
            results.append(subset)

            for i in range(len(nums)):
                if not subset or subset[-1] < nums[i]:
                    nextSubset = list(subset)
                    nextSubset.append(nums[i])
                    queue.append(nextSubset)

        return results
