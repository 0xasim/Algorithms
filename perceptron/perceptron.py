import numpy as np
import pandas as pd

class Perceptron:
  ''' Use me to solve your linearly separable binary classification problem'''
  def __init__(self, eta=0.01, n_iter=50):
    self.eta = eta
    self.n_iter = n_iter
  
  def fit(self, X, y):
    self.w_ = np.random.rand(X.shape[1]+1)
    self.errors_ = []

    for _ in range(self.n_iter):
      errors = 0
      for xi, yi in zip(X, y):
        update = self.eta * (yi - self.predict(xi))
        self.w_[1:] += update * xi
        self.w_[0] += update
        errors += int(update!=0.0)
      self.errors_.append(errors)
    return self.errors_

  def net_input(self, xi):
    return np.dot(self.w_[1:], xi) + self.w_[0]

  def predict(self, xi):
    return 1 if self.net_input(xi) > 0 else -1

if __name__ == "__main__":
  try:
    with open("iris.data", 'r') as df:
      data = pd.read_csv(df, header=None, encoding='utf-8')
  except FileNotFoundError:
    data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None, encoding='utf-8')
    data.to_csv("iris.data", header=False, index=False)

  y = data.iloc[0:99, 4].values # 4th column contains labels
  y = np.where(y == "Iris-setosa", -1, 1) # replace names with -1 and 1
  X = data.iloc[0:99, [0, 2]].values  # Binary class selection

  p = Perceptron(eta=0.01, n_iter=20)
  errors = p.fit(X, y)
  print(errors)
  print(p.predict(np.array([3.0, 0.8])))
