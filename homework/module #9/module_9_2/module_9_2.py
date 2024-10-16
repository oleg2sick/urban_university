first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [
                len(first_string_value) for first_string_value in first_strings
                if len(first_string_value) >= 5
]

second_result = [
                 (first_string_value, second_string_value)
                 for first_string_value in first_strings
                 for second_string_value in second_strings
                 if len(first_string_value) == len(second_string_value)
]

third_strings = first_strings + second_strings

third_result = {
                third_string_value: len(third_string_value)
                for third_string_value in third_strings
                if len(third_string_value) % 2 == 0
}

print(first_result)
print(second_result)
print(third_result)