#Return the sum of fibonacci sequence upto n

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

import time
t = time.time()
fib_rec_tailcall(40)
f = time.time()
print(f"Time was {f-t}")

s = time.time()
print(fib_rec_basic(40))
e = time.time()
print(f"Time was {e-s}")

