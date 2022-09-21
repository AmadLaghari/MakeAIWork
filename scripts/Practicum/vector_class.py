
matrix_A = [[1,2,3],[4,5,6],[7,8,9]]
matrix_B = [[1,2,3,0],[4,5,6,7],[7,8,9,9]]
result = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

(print(matrix_A.__add__(matrix_B)))

class Matrix:

  def __init__(self, matrix_A, matrix_B, result):
    self.matrix_A = matrix_A
    self.matrix_B = matrix_B
    self.result = result


    
  def multiplier(self):
    if len(self.matrix_A[0]) == len(self.matrix_B):
      for rowIndex in range(len(self.matrix_A)):
        for columnIndex in range(len(self.matrix_B[0])):
          for termIndex in range(len(self.matrix_A[0])):
            self.result[rowIndex][columnIndex] += self.matrix_A[rowIndex][termIndex] * self.matrix_B[termIndex][columnIndex]


    else:
      print('Dat kan niet')
  for row in result:
    print(row)
