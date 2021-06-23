import sys
sys.path.append('..')
from fibonacci.fibonacci_sum import *
from extra.decorators import rec_self
from extra.utils import call

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

@rec_self #@memoize
def f1(self, n):
  if n < 2:
    return n
  return self(n-1) + self(n-2)

f2 = rec_self(memoize(f1.__wrapped__))


class fibonacciC:
  def fib(self, n):
    if n < 2:
      return n
    return self.fib(n-1) + self.fib(n-2)
    
if __name__ == "__main__":
  N = 35
  call(fib_rec_memo.__wrapped__, N)
  call(f1, N)
  call(f2, N)
  call(fib_rec_basic, N)
