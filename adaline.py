import numpy as np
class Adaline():
  def __init__(self, eta, n_iter, random_state=1):
    self.eta = eta
    self.n_iter = n_iter
    self.cost_ = list()
    self.random_state = random_state

  def activation(self, X):
    '''Linear activation function'''
    return X

  def fit(self, X, y):
    rgen = np.random.RandomState(self.random_state)
    self.w_ = rgen.normal(loc=0.0, scale=0.01,\
                         size=1 + X.shape[1])
    for _ in range(self.n_iter):
      '''Batch gradient & Learning rule'''
      output = self.activation(self.net_input(X))
      errors = (y - output) # 100 len
      self.w_[1:] += self.eta * X.T.dot(errors)
      self.w_[0] += self.eta * errors.sum()
      '''Cost function'''
      cost = (errors**2).sum() / 2.0
      self.cost_.append(cost)
    return self

  def net_input(self, X):
    return np.dot(X, self.w_[1:]) + self.w_[0]

  def predict(self, X):
    '''Threshold function'''
    return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)

  accuracy = lambda self, X, y: sum(self.predict(X) == y)

if __name__ == '__main__':
  from perceptron import get_iris
  X, y = get_iris()
  adl = Adaline(eta=0.0001, n_iter=100).fit(X, y)
  print(adl.cost_)
  print(adl.accuracy(X, y))

  X_std = np.copy(X)
  ''' Featue scaling: standardization '''
  for i in range(X.shape[1]):
    X_std[:,i] = (X[:,i] - X[:,i].mean()) / X[:,i].std()
  adl_std = Adaline(eta=0.001, n_iter=15).fit(X_std, y)
  print(adl_std.cost_)
  print(adl_std.accuracy(X_std, y))
