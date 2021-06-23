from functools import wraps

def rec_self(f):
  @wraps(f)
  def _f(*a, **kwa): return f(_f, *a, **kwa)
  return _f
