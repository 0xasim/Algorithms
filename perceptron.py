import numpy as np
class Perceptron():
  def __init__(self, eta: int, size: int, i=10):
    """
    Parameters
    """
    self.eta = eta
    self.iter = i
    """
    Attributes
    """
    self.w_ = np.random.random(size + 1)
    self.errors_ = list()

  def fit(self, features, labels):
    for _ in range(self.iter):
      errors = 0
      for xi, t in zip(features, labels):
        update = self.eta * (t - self.predict(xi))
        self.w_[0] += update
        self.w_[1:] += update * xi
        errors += int(update != 0.0)
      self.errors_.append(errors)
    print(self.errors_)

  def net_input(self, x: np.array):
    return np.matmul(x, self.w_[1:]) + self.w_[0]

  def predict(self, x):
    return np.where(self.net_input(x) >= 0, 1, -1)

def manual_get_iris():
  try:
    with open('iris.data', 'r') as f:
      data = f.read().split('\n')
  except FileNotFoundError:
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    data = requests.get(url).text
    with open('iris.data', 'w') as f:
      f.write(data)
    data = data.split('\n')
  data = [d.split(',') for d in data if d][:100]
  features, labels = [d[:-1] for d in data], [d[-1] for d in data]
  features = np.array([[float(v) for v in sample] for sample in features])
  labels = [1 if l == labels[0] else -1 for l in labels]
  return (features, labels)

import pandas as pd
def get_iris():
  try: pdata = pd.read_csv('iris.data', header=None)
  except FileNotFoundError:
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    pdata = pd.read_csv(url, header=None, encoding='utf-8')
    with open('iris.data', 'w') as f:
      f.write(pdata.to_csv(header=None, index=False))
  targets = pdata.iloc[:100, 4].values
  targets = np.where(targets == 'Iris-setosa', -1, 1)
  features = pdata.iloc[:100, :4].values
  return (features, targets)

if __name__ == '__main__':
  features, labels = get_iris()
  assert len(features) == len(labels)
  ppn = Perceptron(eta=0.1, size=features[0].shape[0], i=20)
  ppn.fit(features, labels)

