import pytest
import time

# Найти два числа в отсорт по возр массиве, кот. в сумме дают target, и вернуть их индексы
def two_sum (nums, target):
    left = 0
    right = len(nums)-1

    while left<right:
        sum = nums[left] + nums[right]

        if sum == target:
            return [left, right]
        elif sum < target: left+=1
        else: right -= 1

    return [left, right]

print(two_sum([3,8,9,11,16,18,19,21],25))

def test_two_sum():
    assert two_sum([3, 8, 9, 11, 16, 18, 19, 21], 25) == [2, 4]
    assert two_sum([1, 2, 3, 4, 5], 5) == [0, 3]

def test_two_sum_benchmark(benchmark):
    nums = [3, 8, 9, 11, 16, 18, 19, 21]
    target = 25

    def run():
        two_sum(nums, target)
    benchmark(run)
