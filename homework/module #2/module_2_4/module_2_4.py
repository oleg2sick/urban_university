numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers.pop(0)          #удаляем единичку, потому что единица не простое и не составное число

primes = []             #список под простые числа
not_primes = []         #список под составные числа

for i in numbers:                       #цикл для перебора списка чисел
    flag = True                         #флаг для добавления составных чисел в соответствующий список
    for j in range(2, i // 2 + 1):      #цикл для перебора делителей простого числа
        if i % j == 0:
            not_primes.append(i)
            flag = False
            break                       #прерывание цикла, если нашёлся делитель
    if flag == True:
        primes.append(i)

print(primes)
print(not_primes)