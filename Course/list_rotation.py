def rotate_list(lst, n):
    return lst[n:] + lst[:n]

original_list = [1, 2, 3, 4, 5, 6]
rotated_list = rotate_list(original_list, 2)
print(f"original list: {original_list}")
print(f"rotated list: {rotated_list}")