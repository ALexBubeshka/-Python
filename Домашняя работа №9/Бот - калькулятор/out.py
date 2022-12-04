from rational_calc import *

def result_output(ration_nums, el_1, el_3, el_4):
    while True:
        for i in range(len(ration_nums)):
            if ration_nums[i] == el_1:
                result = ration_nums[i - 1] * ration_nums[i + 1]
                del ration_nums[i + 1]
                del ration_nums[i]
                del ration_nums[i - 1]
                ration_nums.insert(i - 1, result)
                break
        if el_1 not in ration_nums:
            break

    while True:
        for i in range(len(ration_nums)):
            if ration_nums[i] == el_3:
                result = ration_nums[i - 1] - ration_nums[i + 1]
                del ration_nums[i + 1]
                del ration_nums[i]
                del ration_nums[i - 1]
                ration_nums.insert(i - 1, result)
                break
        if el_3 not in ration_nums:
            break

    while True:
        for i in range(len(ration_nums)):
            if ration_nums[i] == el_4:
                result = ration_nums[i - 1] + ration_nums[i + 1]
                del ration_nums[i + 1]
                del ration_nums[i]
                del ration_nums[i - 1]
                ration_nums.insert(i - 1, result)
                break
        if el_4 not in ration_nums:
            break
    print(sum(ration_nums))
    return sum(ration_nums)