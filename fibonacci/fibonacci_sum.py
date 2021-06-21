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

def timeMe(f, n):
  import time
  s = time.time()
  f(n)
  e = time.time()
  print(f"Time was {e-s}")
  

if __name__ == "__main__":
  import time
  timeMe(fib_rec_tailcall, 40)
  timeMe(fib_rec_basic, 40)
