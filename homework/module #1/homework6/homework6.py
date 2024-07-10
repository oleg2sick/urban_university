my_dict = {'test': 123, 'example': 456}             #создал словарь

print(my_dict)

print(my_dict['test'])                              #вывел значение по существующему ключу

print(my_dict.get('dont_exist', 'not found'))       #вывел значение по отсутствующему ключу

my_dict.update({'add_first': 111,
                'add_second': 222})                 #добавил две произвольные пары в словарь

grabbed = my_dict.pop('test')                       #удалил одну пару из словаря по ключу и вывел её на экран

print(grabbed)
print(my_dict)



my_set = {1, 1, 1, 2, 2, 3, 'test', 'test', 1.5, 1.5}   #создал множество

print(my_set)

my_set.add(4)                                           #добавил два произвольных элемента в множество
my_set.add(5)

my_set.discard(1)                                       #удалил элемент из множества

print(my_set)