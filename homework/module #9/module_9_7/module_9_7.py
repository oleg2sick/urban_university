def is_prime(func):
    def wrapper(*args, **kwargs):
        middle_num = func(*args, **kwargs)
        for i in range(2, int(middle_num / 2 + 1)):
            if middle_num % i == 0:
                return 'Составное'
        return 'Простое'

    return wrapper


@is_prime
def sum_three(a, b, c):
    sum_result = a + b + c
    return sum_result


result = sum_three(2, 3, 6)
print(result)
