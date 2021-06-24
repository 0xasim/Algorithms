import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import sys
sys.path.append('/Users/dude/fun/ml/')

class Perceptron:
  """ Use me to solve your linearly separable binary classification problem. """
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
    return np.dot(xi, self.w_[1:]) + self.w_[0]

  def predict(self, xi):
    return np.where(self.net_input(xi) >= 0.0, 1, -1)

if __name__ == "__main__":
  try:
    with open("iris.data", 'r') as df:
      data = pd.read_csv(df, header=None, encoding='utf-8')
  except FileNotFoundError:
    data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None, encoding='utf-8')
    data.to_csv("iris.data", header=False, index=False)

  # Preprocessing
  y = data.iloc[0:99, 4].values # 4th column contains labels
  y = np.where(y == "Iris-setosa", -1, 1) # replace names with -1 and 1
  X = data.iloc[0:99, [0, 2]].values  # Binary class selection

  # Data plotting
  print(data.head())
  plt.scatter(X[:50, 0], X[:50, 1], 
              color='red', marker='o', label='setosa')
  plt.scatter(X[50:100, 0], X[50:100, 1], 
              color='blue', marker='x', label='versicolor')
  plt.xlabel('sepal length [cm]')
  plt.ylabel('petal length [cm]')
  plt.legend(loc='upper left')
  #plt.show()

  # Learning or Model fitting
  ppn = Perceptron(eta=0.01, n_iter=20)
  errors = ppn.fit(X, y)

  # Loss curve
  print(f'Loss over iteration: {errors}')
  plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
  plt.xlabel('Epochs')
  plt.ylabel('Number of updates')
  #plt.show()

  def plot_decision_regions(X, y, classifier, resolution=0.02):
      # setup marker generator and color map
      markers = ('s', 'x', 'o', '^', 'v')
      colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
      cmap = ListedColormap(colors[:len(np.unique(y))])

      # plot the decision surface
      x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
      x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
      xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                             np.arange(x2_min, x2_max, resolution))
      Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
      Z = Z.reshape(xx1.shape)
      plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
      plt.xlim(xx1.min(), xx1.max())
      plt.ylim(xx2.min(), xx2.max())

      # plot class examples
      for idx, cl in enumerate(np.unique(y)):
          plt.scatter(x=X[y == cl, 0],
                      y=X[y == cl, 1],
                      alpha=0.8,
                      c=colors[idx],
                      marker=markers[idx],
                      label=cl,
                      edgecolor='black')

  plot_decision_regions(X, y, classifier=ppn)
  plt.xlabel('sepal length [cm]')
  plt.ylabel('petal length [cm]')
  plt.legend(loc='upper left')
  plt.show()
