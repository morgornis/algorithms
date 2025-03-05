# Слияние двух отсортированных массивов
def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    
    # Если в каком-то из массивов остались элементы, добавляем их в конец слияния
    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])
    
    return merged_array

print(merge_sorted_arrays([3,8,10,11],[1,7,9]))

def test_merge_sorted_arrays():
    assert merge_sorted_arrays([3, 8, 10, 11], [1, 7, 9]) == [1, 3, 7, 8, 9, 10, 11]


def test_merge_sorted_arrays_benchmark(benchmark):
    arr1 = [3, 8, 10, 11]
    arr2 = [1, 7, 9]

    def run():
        merge_sorted_arrays(arr1, arr2)
    benchmark(run)
