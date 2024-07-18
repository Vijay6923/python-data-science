def transpose_matrix(matrix):
    transposed=[[matrix[j][i] for j in range(len(matrix))] for i in range (len(matrix[0]))]
    return transposed




# Initialize the matrix
matrix = []
print("Please enter the elements of the 3x3 matrix row by row:")
# Read the 3x3 matrix from user input
for i in range(3):
    row = list(map(int, input().split()))
    while len(row) != 3:
        print("Each row must have exactly 3 elements. Please try again.")
        row = list(map(int, input().split()))
    matrix.append(row)

# # Calculate the sum of all elements in the matrix
# total_sum = 0
# for row in matrix:
#     total_sum += sum(row)

# # Print the result
# print("The sum of all elements in the matrix is:", total_sum)
    
transposed=transpose_matrix(matrix)
print("original matrix: ")
for row in matrix:
    print(row)
print("transposed matrix: ")
for row in transposed:
    print(row)