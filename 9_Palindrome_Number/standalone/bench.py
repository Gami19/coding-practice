import time
from typing import Callable, List


def benchmark_digits(
    func: Callable[[int], bool],
    values: List[int],
    label: str = "digits",
    repeat: int = 1,
) -> None:
    print("| digit | x | 実行時間(ms) |")
    print("| ----- | - | ------------ |")

    for x in values:
        start = time.perf_counter()
        for _ in range(repeat):
            func(x)
        elapsed = (time.perf_counter() - start) * 1000

        digits = len(str(abs(x))) if x != 0 else 1
        per_run = elapsed / repeat
        print(f"| {digits} | {x} | {per_run:.7f} ms |")