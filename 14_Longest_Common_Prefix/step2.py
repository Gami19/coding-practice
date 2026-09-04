"""
1. found the shortest lenght of stirng element in str array
    str = ["flow" "flower" "flying"]
    shortest_leght is flow. so, the common prefix take up to 4 words like f,l,o,w
2. vertical search
    flow
    flower
    flying
    
"""

from typing import List

class Solution:
    def __init__(self) -> None:
        pass

    def longest_common_prefix(self, strs: List[str]) -> str:
        min_lenght = len(strs[0])

        for words in strs:
            if min_lenght > len(words):
                min_lenght = len(words)

        i = 0
        while i < min_lenght:
            for word in strs:
                if word[i] != strs[0][i]:
                    return word[:i]
            i += 1
        return strs[0][:i]