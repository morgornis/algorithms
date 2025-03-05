# Развернуть часть массива за лин. время без доп. аллокаций
def reverse_array_part(arr, k):
    def reverse_arr(arr, left, right):
        while left<right:
            arr[left], arr[right] = arr[right], arr[left]
            left+=1
            right-=1
    
    n = len(arr)
    reverse_arr(arr, 0, n-1)
    reverse_arr(arr, 0, abs(k)-1)
    reverse_arr(arr, abs(k), n-1)

    return arr

print(reverse_array_part([1, 2, 3, 4, 5, 6, 7],3))

def test_reverse_array_part():
    assert reverse_array_part([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]

def test_reverse_array_part_benchmark(benchmark):
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    def run():
        reverse_array_part(arr, k)
    benchmark(run)
