def divide(first, second):
    if second == 0 or isinstance(first, int | float) == False or isinstance(second, int | float) == False:
        return 'Ошибка'
    else:
        return first / second
