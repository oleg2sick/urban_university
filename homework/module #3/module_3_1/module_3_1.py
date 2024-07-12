calls = 0

def count_calls():                                              #создаём фукнцию-счетчик
    global calls
    calls += 1

def string_info(string):
    count_calls()                                               #добавляем функцию счетчик
    result = len(string), string.lower(), string.upper()        #кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре
    return result

def is_contains(string, list_to_search):
    count_calls()
    new_list = [i.lower() for i in list_to_search]              #функция принимает строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь
    if string.lower() in new_list:
        return True
    else:
        return False

print(string_info('claim'))
print(string_info('data data data'))
print(is_contains('test', ['testing', 'testt', 'TESt']))
print(is_contains('ASDFf', ['asfd', 'asdf']))
print(calls)
