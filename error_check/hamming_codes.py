'''
An implementation of the error correction hamming codes from this 3B1B video
https://www.youtube.com/watch?v=X8jsijhllIA
'''
odd_cols = lambda block, n_set: int(sum([sum([b[n] for b in block]) for n in n_set])%2)
odd_rows = lambda block, n_set: int(sum([sum(block[n]) for n in n_set])%2)

import math
def parity_check(block):
  npar_bits = int(math.log(len(block)**2, 2))
  print(npar_bits)
  indexes = [(2,3), (1,3)] # PB index 1 and 4 use (1,3) cols or rows
  # par is 2x2 int matrix
  par = [odd_rows(block, s) for s in indexes], [odd_cols(block, s) for s in indexes]
  # bpar is 1x2 binary vector
  bpar = [bin(int(''.join(map(str, p)), 2)) for p in par]
  return [int(bpar[i], 2) for i in range(len(bpar))]

def fix_error(block, errI):
  block[errI[0]][errI[1]] = int(not block[errI[0]][errI[1]])
  return block

if __name__ == "__main__":
  import numpy as np
  # parity_bits indexes are (1,2),(4,8)
  block = np.array([[1, 1, 0, 0],
                    [0, 1, 0, 0],
                    [1, 1, 0, 1],
                    [1, 0, 1, 1]])
  print(block)
  print(errI := parity_check(block))
  if any(errI):
    print('fixing')
    print(fix_error(block, errI))
  else: print('No err')


