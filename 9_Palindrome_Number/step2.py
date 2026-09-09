def is_palindrome(x: int) -> bool:
    # 「-」がつく負の数、末尾が 0 は回文にならない
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reverse_half = 0

    while x > reverse_half:
        reverse_half = reverse_half * 10 + x % 10
        x //= 10
    
    # 奇数の場合は、中央の桁（reverse_halfの場合は末尾）を切り捨てて比較
    return (x == reverse_half) or (x == reverse_half // 10)

if __name__ == '__main__':
    x = 1234321
    print(is_palindrome(x))