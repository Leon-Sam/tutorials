from fibo import fib
from fibo import fib as fibi
import fibo

fibo.fib(200)
fib(400)
fibi(300)


if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))