def reverse_number(x: int) -> int:
    sign = [1,-1][x < 0]
    rst = sign * int(str(abs(x))[::-1])
    return rst


assert reverse_number(-123) == -321
assert reverse_number(123) == 321
assert reverse_number(120) == 21
