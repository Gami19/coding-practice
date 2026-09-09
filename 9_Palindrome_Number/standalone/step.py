import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from bench import benchmark_digits
from step3 import is_palindrome

# 桁数ごとのテスト値（回文 / 非回文）
cases = [
    7,           # 1桁
    121,         # 3桁（回文）
    12345,       # 5桁（非回文）
    1234321,     # 7桁（回文）
    123456789,   # 9桁（非回文）
    1234554321,  # 10桁（回文）
    12345678987654321,
]

benchmark_digits(is_palindrome, cases, repeat=10000)