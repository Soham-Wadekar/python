# 10. Write a program to perform matrix multiplication of two given matrices.

def multiply_matrix(mat1,mat2):

    final_result = []

    if len(mat1[0]) != len(mat2):
        print("Matrices are not compatible for multiplication.")
        return None
    
    for i in range(len(mat1)):
        row_result = []

        for j in range(len(mat2[0])):
            elem_sum = sum(mat1[i][k]*mat2[k][j] for k in range(len(mat2)))
            row_result.append(elem_sum)

        final_result.append(row_result)
    
    return final_result

def display_matrix(mat):
    for row in mat:
        print(row)

matrixA = [[1,2,3],
           [2,3,4],
           [3,4,5]]

matrixB = [[1,2,3],
           [2,3,1],
           [3,1,2]]

matrixC = multiply_matrix(matrixA,matrixB)

print("Matrix A:")
display_matrix(matrixA)
print("==="*4)
print("Matrix B:")
display_matrix(matrixB)
print("==="*4)
print("Matrix C:")
display_matrix(matrixC)