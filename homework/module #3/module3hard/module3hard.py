def calculate(args):
  count = 0                                       #создаем счетчик

  if isinstance(args, str) == True:               #увеличиваем счет на длину строки, если нашлась строка
    count += len(args)

  elif isinstance(args, int | float) == True:     #увеличиваем счет на число, если нашли число
    count += args

  elif isinstance(args, dict) == True:            #достаем key и value из словаря, если нашли словарь
    for k, v in args.items():
      count += calculate(k)                       #при помощи рекурсии обрабатываем содержимое словарей, списков, кортежей и множеств и прибавляем к счетчику, если были найдены числа или строки
      count += calculate(v)

  elif isinstance(args, list | tuple | set) == True:
    for i in args:
      count += calculate(i)

  return count


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate(data_structure))