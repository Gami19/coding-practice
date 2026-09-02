import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from bench import benchmark_sizes
from step1 import twoSum

benchmark_sizes(twoSum, [100, 500, 1000, 2000], target=6)
