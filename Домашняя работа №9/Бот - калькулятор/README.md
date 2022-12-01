 Калькулятор
==============
Всем привет. Рад Вам представить наш калкулятор по решению операций с рациональными и комплексными числами.
Программа написана с использованием графического интерфейса - EasyGUI.	

<a href="https://files.fm/f/75huqfmky"><img src="https://files.fm/thumb_show.php?i=75huqfmky"></a>

Установка EasyGUI:
-------------
1.Запустить программу “командная строка” (cmd.exe)

2.Ввести команду - pip install easygui

    >>> pip install easygui

Блок операций с рациональными числами
---------------------------------------
<a href="https://files.fm/f/faettr48q"><img src="https://files.fm/thumb_show.php?i=faettr48q"></a>

Данный блок работает при использоваании следующих функций:
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

Блок операций с комплексными числами
---------------------------------------
<a href="https://files.fm/f/emr3vch72"><img src="https://files.fm/thumb_show.php?i=emr3vch72"></a>

Над проектом работали
---------------------------------------
Бубешко Александр (https://github.com/ALexBubeshka)
Руткевич Вадим (https://github.com/vad1m24)
