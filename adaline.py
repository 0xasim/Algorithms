import numpy as np
class Adaline():
  def __init__(self, eta, n_iter):
    self.eta = eta
    self.n_iter = n_iter
    self.cost_ = list()

  def activation(self, X):
    '''Compute linear activation'''
    return X

  def fit(self, X, y):
    self.w_ = np.random.random(X.shape[1] + 1)
    for _ in range(self.n_iter):
      output = self.activation(self.net_input(X))
      errors = (y - output) # 100 len
      self.w_[1:] += self.eta * X.T.dot(errors)
      self.w_[0] += self.eta * errors.sum()
      cost = (errors**2).sum() / 2.0
      self.cost_.append(cost)
    return self

  def net_input(self, X):
    return np.dot(X, self.w_[1:]) + self.w_[0]

  def predict(self, X):
    return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)

if __name__ == '__main__':
  from perceptron import get_iris
  X, y = get_iris()
  adl = Adaline(0.0003, 100).fit(X, y)
  print(adl.cost_)

