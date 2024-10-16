first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (
                len(first_list_value) - len(second_list_value)
                for first_list_value, second_list_value
                in zip(first, second)
                if len(first_list_value) != len(second_list_value)
)

second_result = (
                len(first[i]) == len(second[i])
                for i in range(len(first))
)

print(list(first_result))
print(list(second_result))


