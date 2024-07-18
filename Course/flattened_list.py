def flatten_list (nested_list):
    flat_list=[item for sublist in nested_list for item in sublist]
    return flat_list



nested_list=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
flattened=flatten_list(nested_list)
print("original nested list: ")
print(nested_list)
print("flattened list: ")
print(flattened)