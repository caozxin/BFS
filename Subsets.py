from typing import (
    List,
)

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        res = []
        def dfs(i, cur):
            if i == n: # when all index went over, we return 
                cur.sort()
                res.append(cur)
                return

            dfs(i + 1, cur + [nums[i]]) # this is for a binary choice to include the number in the subset at each level.
            dfs(i + 1, cur) # this is for a binary choice to NOT include the number in the subset at each level.

        dfs(0, [])

        return res
