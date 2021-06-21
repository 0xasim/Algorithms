def fib(n):
  "Return the nth Fibonacci number."
  if n < 2:
    return n
  return fib(n-1) + fib(n-2)

print(fib(4))
