"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*data):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    #print(f'<<< {[ el**2 for el in data ]}')
    return [ el**2 for el in data ]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def filter_numbers(data, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    def func_odd(num):
        if(num % 2 != 0):
            return True
        else:
            return False


    def func_even(num):
        if (num % 2 == 0):
            return True
        else:
            return False


    new_data=[]
    if filter_type == ODD:
        new_data = filter(func_odd,data)
    if filter_type == EVEN:
        new_data = filter(func_even, data)
    if filter_type == PRIME:
        new_data = filter(is_prime, data)
    return list(new_data)

#filter_numbers([4343, 3005, 6969, 2227, 3183, 785, 411, 2673, 7435, 3519, 9741, 7735, 8903, 8681, 9747, 5427, 2181, 4285, 3927, 3081, 4115, 1663, 4465, 841, 2499, 8741, 6395],ODD)