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
  def blockshaped(arr, nrows, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size
    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    h, w = arr.shape
    assert h % nrows == 0, f"{h} rows is not evenly divisible by {nrows}"
    assert w % nrows == 0, f"{w} rows is not evenly divisible by {ncols}"
    return (arr.reshape(int(h/nrows), nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))
	
  return blockshaped(A, 1, 1)
  #return np.split(A, [[1,1],[1, 1]], 1)

if __name__ == "__main__":
  A = np.array([[1, 2], [4, 5]])
  B = np.array([[5, 6], [9, 20]])
  C = np.array([[1,2,3],[4,5,6]])

  call(matmul_naive, A, B)
  call(np.dot, A, B)
  call(matmul_strassen, A, B)
