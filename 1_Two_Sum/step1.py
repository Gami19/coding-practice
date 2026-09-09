from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    """
        ブルートフォース方式：Double Loop
        targetと各要素の差分が0になるものを選ぶ
        ループ j では、スタートをiの次を選ぶことで、重複確認を回避
    """
    n = len(nums)
    # 求める配列
    result = []

    for i in range(n):
        # 差分を定義
        expect = target - nums[i]
        for j in range(i+1,n):
            # 差分が存在する
            if expect == nums[j]:
                result.append(i)
                result.append(j)
    
    return result


if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    print(twoSum(nums,target))