import time
from typing import Callable, List, Tuple

Case = Tuple[List[str], str]


def run_test_cases(
    func: Callable[[List[str]], str],
    cases: List[Case],
    # 標本平均
    repeat: int = 10000,
) -> None:
    print("| input | expected | got | status |")
    print("| ----- | -------- | --- | ------ |")

    # --- 正しさの確認（1回だけ）+ 全体時間 ---
    total_start = time.perf_counter()
    for strs, expected in cases:
        result = func(strs)
        status = "OK" if result == expected else "NG"
        print(f"| {strs} | {expected!r} | {result!r} | {status} |")
    total_elapsed = (time.perf_counter() - total_start) * 1000

    # --- アルゴリズムだけ（print なし、repeat 回）---
    algo_start = time.perf_counter()
    for _ in range(repeat):
        for strs, _ in cases:
            func(strs)
    algo_elapsed = (time.perf_counter() - algo_start) * 1000
    algo_per_run = algo_elapsed / (repeat * len(cases))

    print()
    print(f"1. アルゴリズムのみ: {algo_elapsed:.4f} ms  "
          f"（{len(cases)} cases × {repeat} = {len(cases) * repeat} calls, "
          f"1回あたり {algo_per_run:.6f} ms）")
    print(f"2. 全体（検証+表示）: {total_elapsed:.4f} ms  "
          f"（{len(cases)} cases）")