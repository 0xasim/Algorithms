import numpy as np
class LogisticRegressionGD():
  def __init__(self, eta=0.01, n_iter=100, random_state=1):
    self.eta = eta
    self.n_iter = n_iter
    self.random_state = random_state

  def fit(self, X, y):
    rgen = np.random.default_rng(self.random_state)
    self.w_ = rgen.normal(loc=0.0, scale=0.01, size=X.shape[1])
    self.b_ = np.float_(0.)
    self.losses_ = []
    for _ in range(self.n_iter):
      phi_z = self.activation(self.net_input(X)) # Interpretable as Class 1 PROB.
      grad = y - phi_z
      self.w_ += self.eta * 2.0 * X.T.dot(grad) / X.shape[0]
      self.b_ += self.eta * 2.0 * grad.mean()
      loss = (-y.dot(np.log(phi_z)) - ((1 - y).dot(np.log(1 - phi_z))) / X.shape[0])
      self.losses_.append(loss)
    return self

  # maps {-inf,+inf} => {0,1}
  def activation(self, z):
    """Compute logistic sigmoid activation"""
    return 1. / (1. + np.exp(-np.clip(z, -250, 250)))

  def net_input(self, X):
    return np.dot(X, self.w_) + self.b_

  def predict(self, xi):
    return np.where(self.activation(self.net_input(xi)) >= 0.5, 1, 0)

if __name__ == '__main__':
  from sklearn import datasets, model_selection, preprocessing
  from plot import plot_decision_regions
  iris = datasets.load_iris()
  X = iris.data[:, [2, 3]]
  y = iris.target
  X_train, X_test, y_train, y_test = model_selection.train_test_split(
          X, y, test_size=0.3, random_state=1, stratify=y)
  sc = preprocessing.StandardScaler().fit(X_train)
  X_train_std, X_test_std = sc.transform(X_train), sc.transform(X_test)

  X_train_01_subset = X_train_std[(y_train == 0) | (y_train == 1)]
  y_train_01_subset = y_train[(y_train == 0) | (y_train == 1)]

  lrgd = LogisticRegressionGD(eta=0.3, n_iter=1000, random_state=1)
  lrgd.fit(X_train_01_subset,
           y_train_01_subset)

  plt = plot_decision_regions(X=X_train_01_subset, 
                        y=y_train_01_subset,
                        classifier=lrgd)

  plt.xlabel('Petal length [standardized]')
  plt.ylabel('Petal width [standardized]')
  plt.legend(loc='upper left')

  plt.tight_layout()
  plt.show()
