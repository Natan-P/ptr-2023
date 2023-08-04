def fib(i: int) -> int:
    if i < 0:
        raise ValueError("ne mors kalkulirat negativn fibonaci butl en, lp")
    if i <= 1:
        return 1
    return fib(i-1) + fib(i-2)
print(fib(int(input())))
