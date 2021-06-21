# Return the sum of fibonacci sequence upto n

def fib_rec_basic(n):
  "Exponential? Naive recursion."
  if n < 2:
    return n
  return fib_rec_basic(n-1) + fib_rec_basic(n-2)

def fib_rec_tailcall(n):
  "Recursion with tailcall optimization."
  def calc_fib(n, a, b):
    if n == 0: return a
    return calc_fib(n-1, b, a+b)
  return calc_fib(n, 0 ,1)

from functools import lru_cache
from memoization import cached
#@cached(thread_safe=False)
@lru_cache()
def fib_rec_memo(n):
  "O(log n). Same as naive recursion but with memoization optimization applied."
  if n < 2:
    return n
  return fib_rec_basic(n-1) + fib_rec_basic(n-2)
  

def timeMe(f, n):
  import time
  s = time.time()
  result = f(n)
  e = time.time()
  print(f"Function: {f.__name__}\n\tOutput: {result}\n\tExecution time: {e-s}")
  

if __name__ == "__main__":
  import time
  n = 30
  timeMe(fib_rec_tailcall, n)
  timeMe(fib_rec_memo, n)
  timeMe(fib_rec_basic, n)
