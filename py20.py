def remove_duplicates(arr):
    
    unique_elements = set(arr)
   
    result = list(unique_elements)
    return result

arr = [1, 2, 3, 3, 4, 5, 5]
result = remove_duplicates(arr)
print("Array after removing duplicates:", result)
