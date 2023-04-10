def find_indexes(arr, min_val, max_val):
    """
    Функция возвращает список индексов элементов массива (списка),
    значения которых принадлежат заданному диапазону (между min_val и max_val)
    """
    indexes = []
    for i in range(len(arr)):
        if min_val <= arr[i] <= max_val:
            indexes.append(i)
    return indexes

# Пример использования:
arr = [1, 5, 10, 15, 20, 25]
min_val = 10
max_val = 20
indexes = find_indexes(arr, min_val, max_val)
print(indexes) # [2, 3, 4]
