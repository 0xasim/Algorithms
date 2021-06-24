# https://stackoverflow.com/a/5063783
from functools import wraps

def withself(f):
  '''
  Add yourself to the arguments
  All function calls (especially recusive) will have to go through the wrapper
  '''
  @wraps(f)
  def _wrapper(*a, **kwa): return f(_wrapper, *a, **kwa) 
  return _wrapper

