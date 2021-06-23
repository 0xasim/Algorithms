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
    result = func(*args)
    cache[args] = result  # No limit on cache size. Might grow big
    return result
  return to_cache

@memoize
def fibonacci(n):
  if n < 2:
    return n
  return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
  N = 35
  print(timeit("fibonacci(N)", globals=globals(), number=1))
