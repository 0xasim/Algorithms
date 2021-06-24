import numpy as np

class Perceptron:
  def __init__(self, eta=0.01, n_iter=50):
    self.eta = eta
    self.n_iter = n_iter
  
  def fit(self, X, y):
    self.w_ = np.random.rand(X.shape[1]+1)
    self.errors_ = []

    for _ in range(n_iter):
      errors = 0
      for xi, yi in zip(X, y):
        update = (yi - self.predict(xi))*eta
        w_ = w_ + update

  def net_input(self, xi):
    return np.dot(self.w_[1:], xi) + self.w_[0]

  def predict(self, xi):
    return 1 if self.net_input(xi) > 0 else -1
if __name__ == "__main__":
  p = Perceptron()
