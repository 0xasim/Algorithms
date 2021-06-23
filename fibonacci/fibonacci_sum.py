#!/usr/bin/env python3
# Return the sum of fibonacci sequence upto n
import sys
sys.path.append('..')
from extra.utils import call, callDec
from extra.decorators import withself

def fib_rec_basic(n):
  "Exponential? Naive recursion."
  if n < 2:
    return n
  return fib_rec_basic(n-1) + fib_rec_basic(n-2)

#@callDec
def fib_rec_tailcall(n):
  "Recursion with tailcall optimization."
  def calc_fib(n, a, b):
    if n == 0: return a
    return calc_fib(n-1, b, a+b)
  return calc_fib(n, 0 ,1)

import functools
@functools.cache
def fib_rec_memo(n: int):
  "O(log n). Same as naive recursion but with memoization optimization applied."
  if n < 2:
    return n
  return fib_rec_memo(n-1) + fib_rec_memo(n-2)

@withself
def fib_rec_self(self, n):
  "Exponential? Naive recursion."
  if n < 2:
    return n
  return self(n-1) + self(n-2)

if __name__ == "__main__":
  n = 35
  fib_rec_tailcall(n)
  call(fib_rec_memo, n)
  call(fib_rec_basic(n))
