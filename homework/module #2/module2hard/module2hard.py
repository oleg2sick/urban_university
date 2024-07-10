some_num = input('Число на первом камне (от 3 до 20): ')            #задаем число, для которого нужно подобрать пароль
first_rock_num = int(some_num)                                      #фиксируем это число, преобразуя тип

save_list = []                                                      #создаём список, который будем заполннять подходящими парами чисел
grow_num = 1                                                        #первое число в списке всегда будет единицой, с него будет начинаться подбор
decr_num = first_rock_num                                           #последнее число приравниваем к числу из начала кода, чтобы ограничить им range цикла

while grow_num < decr_num:                                          #создаём цикл, в котором будем осуществлять перебор пар чисел, пока первое подбираемое число не приравняется ко второму (дальше подбирать нет смысла по условию)
    for i in range(grow_num, decr_num):                             #создаём цикл для перебора чисел от единицы до числа из начала кода (не включительно)
        if first_rock_num % (grow_num + i) == 0 and grow_num != i:
            save_list.append(grow_num)
            save_list.append(i)
    grow_num += 1
    decr_num -= 1

result = [str(i) for i in save_list]                                #преобразуем тип данных в списке int -> str для join'a
print(''.join(result))                                              #выводим без пробелов целой строкой