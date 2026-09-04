from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def longest_common_prefix(self,strs: List[str]) -> str:
        common_prefix = ""

        sorted_strs = sorted(strs)
        first_word = sorted_strs[0]
        last_word = sorted_strs[-1]
        for i in range( min(len(first_word),len(last_word)) ):
            if first_word[i] != last_word[i]:
                return common_prefix
            common_prefix += first_word[i]
        return common_prefix