# https://stackoverflow.com/a/5063783
from functools import wraps

def withself(f):
  @wraps(f)
  def _f(*a, **kwa): return f(_f, *a, **kwa)
  return _f

def bind(f):
  "Pass the reference to the function `f` as first argument"
  return f.__get__(f, type(f))
