def calculate(args):
  count = 0
  if args == []:
    return 0

  if isinstance(args, dict) == True:
    for k, v in args.items():
      count += calculate(k)
      count += calculate(v)

  elif isinstance(args, str) == True:
    count += len(args)

  elif isinstance(args, int | float) == True:
    count += args

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