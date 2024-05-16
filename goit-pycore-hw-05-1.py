

def caching_fibonacci():
    cache = {}                                     # create empty dictionary

    def fib(n):                                    # inner function block (fib = fibonacci)
        if n in cache:                                  # check if the number is already in the cache
            return cache[n]
        if n <= 1:                                      # if n <= 1   Fibonacci number = n
            result = n
        else:
            result = fib(n - 1) + fib(n - 2)            # recursive formula for fibonacci number
        cache[n] = result
        return result
    
    return fib

fib = caching_fibonacci()

print(fib(1))
print(fib(5))
print(fib(10))

