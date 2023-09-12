def count_rotations(nums):
    if len(nums) == 0:
        return None
    return nums.index(min(nums))
test0 = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}
# A list of size 8 rotated 5 times.
test1 = {
    'input': {
        'nums': [4,5,6,7,8,1,2,3]
    },
    'output': 5
}
# A list that wasn't rotated at all.
test2 = {
    'input': {
        'nums': [1,2,3,4,5,6,7,8]
    },
    'output': 0
}
# A list that was rotated just once.
test3 = {  
    'input': {
        'nums': [8,1,2,3,4,5,6,7]
    },
    'output': 1
}
# A list that was rotated n-1 times, where n is the size of the list.
test4 = {
    'input': {
        'nums': [2,3,4,5,1]
    },
    'output': 4
}
# A list that was rotated n times, where n is the size of the list
test5 = {
    'input': {
        'nums': [1,2,3,4,5]
    },
    'output': 0
}
# An empty list.
test6 = {
    'input': {
        'nums': []
    },
    'output': None
}
# A list containing just one element.
test7 = {
    'input': {
        'nums': [1]
    },
    'output': 0
}
tests = [test0, test1, test2, test3, test3, test5, test6, test7]
from jovian.pythondsa import evaluate_test_cases
evaluate_test_cases(count_rotations, tests)
