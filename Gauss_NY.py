
import numpy as np

def transAugmentedMatrix(A, b):
    # You can use other types variables.
    # TODO:
    augmentedMatrix = np.hstack((A,b))
    return augmentedMatrix

def gaussJordan(augMat):
    # TODO:
    rowNum = len(augMat)                               # return the number of rows.
    rowNum_0 = len(augMat[0])
    x = np.zeros((rowNum, 1))                          # solution vector x has 4x1 dimension.

    # Gauss elimination step.
    for j in range(min(rowNum_0, rowNum)):             # each column on the main diag
        if (augMat[j][j]==0):
            colNum = [augMat[k][j] for k in range(j,rowNum)]
            pivot = colNum.index(max(colNum))          # find a non-zero pivot and swap rows
            temp = augMat[j]
            augMat[j] = augMat[pivot]
            augMat[pivot] = temp
        
        for i in range(j+1,rowNum):
            c = augMat[i][j]/augMat[j][j]              # the ratio of lower element by the pivot 
            augMat[i] = [augMat[i][k]-c*augMat[j][k] for k in range(rowNum_0)]
    
      #  else:
      #      print ('Detected 0 pivot, skip this loop')

    # Jordan elimination step.
    #for j in reversed(range(rowNum)):
     #   pivot = augMat[rowNum_, colNum]
     #   if pivot != 0:
            # TODO:
            # Code here.

      #      colNum -= 1

    # TODO:
    # Split the augmentedMatrix and store in vector x.

    return x

def inverseMatrix(A):
    # You can use other types variables.
    # TODO:
    inverseMatrix = np.matrix()
    return inverseMatrix

def systemSolver(A, b):
    # TODO: A*b
    x = np.array()
    return x

def main():
    '''
    Do not modify function arguments. You should use all the functions.

    A is coefficient matrix.
    x is variable x vector.
    b is constant vector.

    I recommend using numpy to define A, x, b.
    Compare the results of Gauss Jordan method and x = inv(A)*b.
    This material is copyrighted by louis.
    '''
    # You can other types variables.
    A = np.array([[2, 1, 1, -2],
                  [3, -2, 1, -6],
                  [1, 1, -1, -1],
                  [-5, -1, 2, -8]])  # 계수
    x = np.zeros(4)
    b = np.array([[1, -2, -1, 3]]).T

    augMat=transAugmentedMatrix(A, b)
    x = gaussJordan(augMat)
    print (x)

if __name__ == '__main__':
    main()
