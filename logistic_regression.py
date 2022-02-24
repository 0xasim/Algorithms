import numpy as np
class logisticReg():
  def __init__(self, eta=0.01, n_iter=100, random_state=1):
    self.eta = eta
    self.n_iter = n_iter
    self.random_state = random_state

  def activation(self, z):
    """Compute logistic sigmoid activation"""
    return 1. / (1. + np.exp(-np.clip(z, -250, 250)))

  def net_input(self, X):
    return np.dot(X, self.w_[1:]) + self.w_[0]

  def fit(self, X, y):
    rgen = np.random.default_rng(self.random_state)
    self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
    self.cost_ = list()
    for _ in range(self.n_iter):
      phi_z = self.activation(self.net_input(X)) # interpretable as prob of what?
      grad = y - phi_z
      self.w_[1:] += self.eta * X.T.dot(grad)
      self.w_[0] += self.eta * grad.sum()
      cost = (-y.dot(np.log(phi_z)) - ((1 - y).dot(np.log(1 - phi_z))))
      self.cost_.append(cost.sum())

  def predict(self, xi):
    return np.where(self.activation(self.net_input(xi)) >= 0.5, 1, 0)

if __name__ == '__main__':
  from perceptron import get_iris
  X, y = get_iris()
  y = np.array([0 if yi == -1 else 1 for yi in y])
  logreg = logisticReg(eta=0.01, n_iter=1000)
  logreg.fit(X, y)
  print(logreg.cost_)

