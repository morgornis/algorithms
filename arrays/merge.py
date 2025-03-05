# Слияние двух отсортированных массивов без дополнительных аллокаций
def merge(arr1, arr2):
    pointer1 = len(arr1) - len(arr2) - 1
    pointer2 = len(arr2) - 1
    pointer3 = len(arr1) - 1

    while pointer2 >= 0:
        if pointer1 >= 0 and arr1[pointer1] > arr2[pointer2]:
            arr1[pointer3] = arr1[pointer1]
            pointer1 -= 1
        else:
            arr1[pointer3] = arr2[pointer2]
            pointer2 -= 1
        pointer3 -= 1

    return arr1

print(merge([3,8,10,11],[1,7,9]))

def test_merge():
    arr1 = [3, 8, 10, 11, 0, 0, 0]
    arr2 = [1, 7, 9]
    assert merge(arr1, arr2) == [1, 3, 7, 8, 9, 10, 11]

def test_merge_benchmark(benchmark):
    arr1 = [3, 8, 10, 11, 0, 0, 0]
    arr2 = [1, 7, 9]

    def run():
        merge(arr1, arr2)
    benchmark(run)
