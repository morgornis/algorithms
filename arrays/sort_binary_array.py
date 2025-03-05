# Сортировка массива из 0 и 1
def sort_binary_array(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            # Если arr[left] == 1 и arr[right] == 0, меняем их местами
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
    return arr

print(sort_binary_array([0,1,1,0,1,0,1,0]))

def test_sort_binary_array():
    assert sort_binary_array([0, 1, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1]

def test_sort_binary_array_benchmark(benchmark):
    arr = [0, 1, 1, 0, 1, 0, 1, 0]

    def run():
        sort_binary_array(arr)
    benchmark(run)
