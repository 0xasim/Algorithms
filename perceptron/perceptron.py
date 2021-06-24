import numpy as np

class Perceptron:
  def __init__(self, eta=0.01, n_iter=50):
    self.eta = eta
    self.n_iter = n_iter
  
  def fit(self, X, y):
    self.w_ = numpy.random.rand(x.shape[1]+1)
    self.errors = []

if __name__ == "__main__":
  p = Perceptron()
