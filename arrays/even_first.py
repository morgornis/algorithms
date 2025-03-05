# Передвинуть четные числа вперед в неотсорт. масиве
def even_first(arr):
    even_index = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[even_index], arr[i] = arr[i], arr[even_index]
            even_index += 1
            
    return arr

print(even_first([3, 2, 4, 1, 11, 8, 9]))

def test_even_first():
    assert even_first([3, 2, 4, 1, 11, 8, 9]) == [2, 4, 8, 1, 11, 3, 9]

def test_even_first_benchmark(benchmark):
    arr = [3, 2, 4, 1, 11, 8, 9]

    def run():
        even_first(arr)
    benchmark(run)
