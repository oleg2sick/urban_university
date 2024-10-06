def custom_write(file_name, strings):
    file_name = file_name
    strings = strings

    file = open(file_name, 'a', encoding='utf-8')

    counter = 0
    strings_positions = {}

    for string in strings:
        strings_positions[counter + 1, file.tell()] = strings[counter]
        file.write(string + '\n')
        counter += 1

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
