# Калькулятор рациональных чисел
# пример 5 / 4 * 6 / 7 + 3 / 2 - 9
from out import result_output
from input import *
from fractions import Fraction


ration_nums = []
x = 1

def rational_numbers(nums, el_2, el_1, el_3, el_4):
    global ration_nums
    for i in range(len(nums)):
        if nums[i].isnumeric():
            if (i + 1) < len(nums):
                if nums[i + 1] != el_2 and nums[i - 1] != el_2:
                    ration_nums.append(Fraction(int(nums[i]), x))
            elif (i + 1) == len(nums):
                if nums[i - 1] != el_2:
                    ration_nums.append(Fraction(int(nums[i]), x))
        elif nums[i] == el_2:
            ration_nums.append(Fraction(int(nums[i - 1]), int(nums[i + 1])))
        else:
            ration_nums.append(nums[i])
    result_output(ration_nums, el_1, el_3, el_4)
