import numpy as np
import sys
sys.path.append('..')
from extra.utils import call

def matmul_naive(A, B):
  assert A.shape[1] == B.shape[0]
  C = np.zeros([A.shape[0], B.shape[1]])
  for i in range(A.shape[0]):
    for j in range(B.shape[1]):
      total = 0
      for k in range(A.shape[1]):
        total += A[i][k] * B[k][j]
      C[i][j] = total
  return C

if __name__ == "__main__":
  A = np.array([[1, 2], [3, 4]])
  B = np.array([[5, 6], [7, 8]])
  print(matmul_naive(A, B))
  print(np.dot(A, B))
