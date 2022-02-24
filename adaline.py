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

  def fit_bgd(self, X, y):
    '''Fit using batch gradient descent'''
    rgen = np.random.RandomState(self.random_state)
    self.w_ = rgen.normal(loc=0.0, scale=0.01,\
                         size=1 + X.shape[1])
    for _ in range(self.n_iter):
      '''Cost batch gradient & Learning rule'''
      output = self.activation(self.net_input(X))
      errors = (y - output) # 100 len
      self.w_[1:] += self.eta * X.T.dot(errors)
      self.w_[0] += self.eta * errors.sum()
      '''Cost function'''
      cost = (errors**2).sum() / 2.0
      self.cost_.append(cost)
    return self

  def fit_sgd(self, X, y):
    '''Fit using stochastic gradient descent'''
    self.rgen = np.random.RandomState(self.random_state)
    self.w_ = self.rgen.normal(loc=0.0, scale=0.01,\
                         size=1 + X.shape[1])
    for _ in range(self.n_iter):
      cost = list()
      for xi, yi in zip(X, y):
        error = yi - self.activation(self.net_input(xi))
        self.w_[1:] += self.eta * xi.dot(error)
        self.w_[0] += self.eta * error
        cost.append(0.5 * error**2)
      self.cost_.append(sum(cost) / len(y))
      X, y = self._shuffle(X, y)
    return self

  def net_input(self, X):
    return np.dot(X, self.w_[1:]) + self.w_[0]

  def predict(self, X):
    '''Threshold function'''
    return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)

  def _shuffle(self, X, y):
    '''Shuffling training data'''
    r = self.rgen.permutation(len(y))
    return X[r], y[r]

  accuracy = lambda self, X, y: sum(self.predict(X) == y)

if __name__ == '__main__':
  from perceptron import get_iris
  X, y = get_iris()
  ada_bgd = Adaline(eta=0.0001, n_iter=100).fit_bgd(X, y)
  print(ada_bgd.cost_)
  print(ada_bgd.accuracy(X, y))

  X_std = np.copy(X)
  ''' Featue scaling: Standardization '''
  for i in range(X.shape[1]):
    X_std[:,i] = (X[:,i] - X[:,i].mean()) / X[:,i].std()
  ada_std = Adaline(eta=0.001, n_iter=15).fit_bgd(X_std, y)
  print(ada_std.cost_)
  print(ada_std.accuracy(X_std, y))

  ada_sgd = Adaline(eta=0.001, n_iter=15).fit_sgd(X_std, y)
  print(ada_sgd.cost_)
  print(ada_sgd.accuracy(X_std, y))
