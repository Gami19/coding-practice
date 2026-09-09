def is_palindrome(x: int) -> bool:
    # 文字列に変換
    # 配列のスライス（reverse）と比較x
    return str(x) == str(x)[::-1]
