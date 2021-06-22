import time

def timeMe(f, n):
  _t0 = time.time()
  retval = f(n)
  _t1 = time.time() 
  return (_t1 - _t0, retval)
  
def call(f, n):
  _t, retval = timeMe(f, n)
  print(f"Function: {f.__name__}\n\tOutput: {retval}\n\tExecution time: {_t}")

