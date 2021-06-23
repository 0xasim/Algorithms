from decorators import *

@bind
def rec(self, i):
  print(i,end=",")
  if i>0: self(self, i-1)

rec(10)
