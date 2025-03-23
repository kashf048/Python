from functools import lru_cache        # calculate everything instantly

@lru_cache
def fib(n: int) -> int:     # fresh calculation in each and every time
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    
for i in range(0, 100):
    print(f"{i}: {fib(i)}")