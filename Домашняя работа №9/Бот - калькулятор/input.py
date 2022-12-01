from rational_calc import rational_numbers

nums = ''
ration_nums = []
x = 1
el_1 = '*'
el_2 = '/'
el_3 = '-'
el_4 = '+'
condition = None

def input_numbers(var1):
    global nums
    global condition
    nums += var1
    nums = nums.split(' ')
    for i in range(len(nums)):
        if nums[i] == el_1 or nums[i] == el_2 or nums[i] == el_3 or nums[i] == el_4:
            condition = True
        elif nums[i].isnumeric():
            condition = True
        else:
            print("Вводить можно лишь целые цифры и операции с ними!")
            input_numbers(var1)
    rational_numbers(nums, el_2, el_1,el_3,el_4)