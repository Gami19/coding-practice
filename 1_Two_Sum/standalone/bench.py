import random
import time
from typing import Callable, List, Optional


def benchmark_sizes(
    func: Callable,
    sizes: List[int],
    target: int,
    seed: Optional[int] = None,
) -> None:
    if seed is not None:
        random.seed(seed)
    for n in sizes:
        sample_nums = [random.randint(1, 10000) for _ in range(n)]

        start = time.perf_counter()
        func(sample_nums, target=target)
        elapsed = (time.perf_counter() - start) * 1000

        print(f"N = {n:4d} | 実行時間: {elapsed:.4f} ms")
