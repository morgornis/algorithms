# Задача флага Нидерладндов: отсорт. массив из 0,1,2 за линейное время
def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

print(sort_colors([2, 0, 2, 1, 1, 0]))

def test_sort_colors():
    assert sort_colors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]

def test_sort_colors_benchmark(benchmark):
    nums = [2, 0, 2, 1, 1, 0]

    def run():
        sort_colors(nums)
    benchmark(run)
