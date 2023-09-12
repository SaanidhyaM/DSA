nums = [1]
target = 0
num1 = nums.copy()
num1.sort()
def count_rotations(nums):
    if len(nums) == 0:
        return None
    return nums.index(min(nums))
def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1
def locate_num(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            else:
                return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums) - 1, condition)
def check_if_element_rotated(locate_num, count_rotations, nums):
    if locate_num == -1:
        return -1
    else:
        if (1<= (len(nums) - locate_num) <= count_rotations):
            return True
        else:
            return False
def correct_index(locate_num, count_rotations, check_if_element_rotated, nums):
    if locate_num == -1:
        return -1
    else:
        if check_if_element_rotated == True:
            return locate_num + count_rotations - len(nums)
        return locate_num + count_rotations
x = (check_if_element_rotated(locate_num(num1, target), count_rotations(nums), nums))
print(correct_index(locate_num(num1, target), count_rotations(nums), x, nums))