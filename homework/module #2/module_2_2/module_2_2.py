first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')

if first == second and first == third:
    print(3)
elif first == second and first != third:
    print(2)
elif first == third and first != second:
    print(2)
elif second == third and first != second:
    print(2)
else:
    print(0)