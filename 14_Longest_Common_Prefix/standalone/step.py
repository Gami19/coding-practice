import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from bench import run_test_cases
from step2 import Solution

solution = Solution()

cases = [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
    (["interspecies", "interstellar", "interstate"], "inters"),
    (["a"], "a"),
    (["", "b"], ""),
    (["ab", "a"], "a"),
]
run_test_cases(solution.longest_common_prefix, cases)