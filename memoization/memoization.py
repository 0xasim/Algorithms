import functools
from timeit import timeit

"""
An optimization technique that caches and retrieves function results instead of recomputing
Reduces time complexity but increases space requirements.
"""

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


@memoizeC
def fibonacci(n):
  if n < 2:
    return n
  return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
  N = 35
  print(timeit("fibonacci(N)", globals=globals(), number=1))
