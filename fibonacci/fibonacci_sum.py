def fib_rec_basic(n):
  "Return the nth Fibonacci number."
  if n < 2:
    return n
  return fib_rec_basic(n-1) + fib_rec_basic(n-2)

def fib_rec_tailcall(n):
  def calc_fib(n, a, b):
    if n == 0: return a
    return calc_fib(n-1, b, a+b)
  return calc_fib(n, 0 ,1)


print(fib_rec_basic(20))
print(fib_rec_tailcall(20))
