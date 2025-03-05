# Развернуть массив за лин. время без аллокации памяти
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

print(reverse_array([3,8,6,9,9,8,6]))

def test_reverse_array():
    assert reverse_array([3, 8, 6, 9, 9, 8, 6]) == [6, 8, 9, 9, 6, 8, 3]

def test_reverse_array_benchmark(benchmark):
    arr = [3, 8, 6, 9, 9, 8, 6]

    def run():
        reverse_array(arr)
    benchmark(run)
