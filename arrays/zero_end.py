# Нули в конец
def zero_end(arr):
    left = 0
    right = 0

    while right < len(arr):
        if arr[right] == 0:
            right += 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right += 1
    
    return arr

print(zero_end([0, 0, 1, 0, 3, 12]))

def test_zero_end():
    assert zero_end([0, 0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0, 0]

def test_zero_end_benchmark(benchmark):
    arr = [0, 0, 1, 0, 3, 12]

    def run():
        zero_end(arr)
    benchmark(run)
