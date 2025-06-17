def fib(n:int):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n:int=3)->list[int]:    # return Fibonacci series less than n
    """Return a Fibonacci series less than n."""
    a, b = 0, 1
    results = []
    while a < n:
        results.append(a)
        a, b = b, a+b
    return results

# Now call the function we just defined:
fib(2000)
r = fib2()
print(r) # [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597 ]