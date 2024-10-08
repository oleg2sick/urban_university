def get_multiplied_digits(number):                                      #решение через рекурсию
    str_number = str(number)
    if len(str_number) == 1:
        return number
    else:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)
print(result)




def get_multiplied_digits(number):                                      #решение через цикл
    if number < 10:
        return number
    else:
        mult = 1
        for i in str(number):
            if int(i) == 0:
                continue
            mult *= int(i)
        return mult

result = get_multiplied_digits(40203)
print(result)