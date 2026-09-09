from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    diff_to_index = {}
    for i, num in enumerate(nums):
        complete = target - num
        if complete in diff_to_index:
            return [i,diff_to_index[complete]]
        else:
            diff_to_index[num] = i
    
    # not found solution
    return []
    
