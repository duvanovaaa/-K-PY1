  # TODO написать функцию генерации случайных паролей
from random import sample

def get_random_password(lenght=8) -> str:
    letters_upper = "a/b/c/d/e/f/g/h/i/l/k/l/n/o/p/q/r/s/t/u/v/w/x/y/z"
    letters_lower = letters_upper.upper()
    nums = [str(i) for i in range(0, 10)]
    symbols = letters_upper.split('/') + letters_lower.split('/') + nums
    password = ''.join(sample(symbols, lenght))
    return password

print(get_random_password())
