def is_palindrome(x: int) -> bool:
    # 常にマイナスは,「-」記号があるため False
    if x < 0:
        return False
    
    original = x
    reverse = 0

    while x != 0:
        reverse = reverse * 10 + x % 10
        x = x // 10 

    # if文は要らない
    # if original == reverse:
    #     return True
    # else:
    #     return False
    
    return original == reverse
    
if __name__ == '__main__':
    x = 121
    print(is_palindrome(x))