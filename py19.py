def intersection(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1.intersection(set2))


arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

a = intersection(arr1, arr2)
print("Intersection of arr1 and arr2:", a)



