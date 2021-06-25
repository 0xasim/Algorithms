import time
from functools import wraps
def timeMe(f, *args):
  _t0 = time.time()
  retval = f(*args)
  _t1 = time.time() 
  return (_t1 - _t0, retval)
  
def call(func, *args):
  _t, retval = timeMe(func, *args)
  print(f"Function: {func.__name__}\n\tInput:\n{args}\n\tOutput:\n{retval}\n\tExecution time: {_t}\n")
  return retval

def callDec(func):
  "Bad idea when applied to recursive functions"
  @wraps(func)
  def _f(*args):
    _t, retval = timeMe(func, *args)
    print(f"Function: {func.__name__}\n\tInput:\n{args}\n\tOutput:\n{retval}\n\tExecution time: {_t}\n")
    return retval
  return _f
