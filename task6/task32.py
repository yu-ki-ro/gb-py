def find_indexes(arr, min_val, max_val):
    indexes = []
    for i in range(len(arr)):
        if min_val <= arr[i] <= max_val:
            indexes.append(i)
    return indexes


arr = [3, 8, 55, 34, 20, 86]
min_val = 4
max_val = 20
indexes = find_indexes(arr, min_val, max_val)
print(indexes)
