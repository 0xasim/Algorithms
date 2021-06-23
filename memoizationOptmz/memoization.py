import sys
sys.path.append('..')
from fibonacci.fibonacci_sum import *
from extra.decorators import withself
from extra.utils import call
import functools

"""
An optimization technique that caches and retrieves function results instead of recomputing
Reduces time complexity but increases space requirements.
"""
sys.setrecursionlimit(10**6)

def memoize(func):
  cache = dict()
  @functools.wraps(func)
  def to_cache(*args):
    if args in cache:
      return cache[args]
    cache[args] = func(*args)  #No limit on cache size. Might grow big
    return cache[args]
  return to_cache

class memoizeC:
  def __init__(self, f):
    self.f = f
    self.cache = dict()
  def __call__(self, *args):
    if not args in self.cache:
      self.cache[args] = self.f(*args)
    return self.cache[args]

class fibonacciC:
  def fib(self, n):
    if n < 2:
      return n
    return self.fib(n-1) + self.fib(n-2)
    
if __name__ == "__main__":
  fib_rec_mymem = withself(memoize(fib_rec_self))
  #fib_rec_mymemC = lambda n: memoizeC(withself(fib_rec_self(n)))
  N = 35
  call(fib_rec_mymem, N)
  #call(fib_rec_mymemC, N)
  call(fib_rec_memo, N)
  call(fib_rec_tailcall, N)
  call(fib_rec_basic, N)
