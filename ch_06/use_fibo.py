import fibo as fb
from fibo import fib
import sys

# sys.path.append('c:\')



# def fib(i):
#     print("Bonjour",i)

def main():
    # fibo.fib(1000)
    # fb.fib(1000)
    print(sys.argv)
    fib(1000)
    print("fb.r",fb.r)

if __name__ == "__main__":
    main()

