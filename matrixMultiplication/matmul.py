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

def matmul_cache(A, B):
  assert A.shape[1] == B.shape[0]
  C = np.zeros([A.shape[0], B.shape[1]])
  
def matmul_strassen(A, B):
  assert A.shape[0] == A.shape[1] == B.shape[0] # Be a square
  print(np.split(A, 2, 2))

if __name__ == "__main__":
  A = np.array([[1, 2], [4, 5]])
  B = np.array([[5, 6], [9, 20]])

  call(matmul_naive, A, B)
  call(np.dot, A, B)
  call(matmul_strassen, A, B)
