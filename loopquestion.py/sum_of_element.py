matrix = [[0, 0, 1, 1, 1],[0, 0, 0, 0, 1],[0, 1, 1, 1, 1],[0, 0, 0, 0, 1],[1, 1, 1, 1, 1]]

max_ones = 0
max_row = -1

for i in range(len(matrix)):
    count_ones = 0
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            count_ones += 1
    if count_ones > max_ones:
        max_ones = count_ones
        max_row = i

print("Row with maximum number of 1s:", max_row + 1)







