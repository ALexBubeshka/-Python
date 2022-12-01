 Телеграмм бот Калькулятор 
==============
Всем привет. Рад Вам представить калкулятор по решению операций с рациональными в телеграмм боте. 
Программа написана с использованием графического интерфейса - EasyGUI.	

<a href="https://files.fm/f/yvyp2s8y9"><img src="https://files.fm/thumb_show.php?i=yvyp2s8y9"></a>

----------------------------------------------------------
1. Используем модуль Fraction. Создаем экземпляр класса используя строку представляющую собой число.
   Универсальность данного кода в возможности преобразования любого количества переменных из строки.
    >>> def rational_numbers():
    >>> 
    >>>     global ration_nums
    >>>     for i in range(len(nums)):
    >>>         if nums[i].isnumeric():
    >>>             if (i+1) < len(nums):
    >>>                 if nums[i+1] != el_2 and nums[i-1] != el_2:
    >>>                     ration_nums.append(Fraction(int(nums[i]), x))
    >>>             elif (i+1) == len(nums):
    >>>                 if nums[i-1] != el_2:
    >>>                     ration_nums.append(Fraction(int(nums[i]), x))
    >>>         elif nums[i] == el_2:
    >>>             ration_nums.append(Fraction(int(nums[i - 1]), int(nums[i + 1])))
    >>>         else:
    >>>             ration_nums.append(nums[i])
    >>>     result_output()

2. Далее производим вычисления с использованием возможностей модуля Fraction.

    >>> def result_output():
    >>> 
    >>>     while True:
    >>>         for i in range(len(ration_nums)):
    >>>             if ration_nums[i] == el_1:
    >>>                 result = ration_nums[i - 1] * ration_nums[i + 1]
    >>>                 del ration_nums[i + 1]
    >>>                 del ration_nums[i]
    >>>                 del ration_nums[i - 1]
    >>>                 ration_nums.insert(i - 1, result)
    >>>                 break
    >>>         if el_1 not in ration_nums:
    >>>             break
    >>> 
    >>>     while True:
    >>>         for i in range(len(ration_nums)):
    >>>             if ration_nums[i] == el_3:
    >>>                 result = ration_nums[i - 1] - ration_nums[i + 1]
    >>>                 del ration_nums[i + 1]
    >>>                 del ration_nums[i]
    >>>                 del ration_nums[i - 1]
    >>>                 ration_nums.insert(i - 1, result)
    >>>                 break
    >>>         if el_3 not in ration_nums:
    >>>             break
    >>> 
    >>>     while True:
    >>>         for i in range(len(ration_nums)):
    >>>             if ration_nums[i] == el_4:
    >>>                 result = ration_nums[i - 1] + ration_nums[i + 1]
    >>>                 del ration_nums[i + 1]
    >>>                 del ration_nums[i]
    >>>                 del ration_nums[i - 1]
    >>>                 ration_nums.insert(i - 1, result)
    >>>                 break
    >>>         if el_4 not in ration_nums:
    >>>             break


Над проектом работал
---------------------------------------
Бубешко Александр (https://github.com/ALexBubeshka)

