# Необхідно створити функцію generator_numbers, яка буде аналізувати текст, ідентифікувати всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор. Дійсні числа у тексті записані без помилок, чітко відокремлені пробілами з обох боків. Також потрібно реалізувати функцію sum_profit, яка буде використовувати generator_numbers для підсумовування цих чисел і обчислення загального прибутку.
#
# Вимоги до завдання:
#
# Функція generator_numbers(text: str) повинна приймати рядок як аргумент і повертати генератор, що ітерує по всіх дійсних числах у тексті.
# Дійсні числа у тексті вважаються записаними без помилок і чітко відокремлені пробілами з обох боків.
# Функція sum_profit(text: str, func: Callable) має використовувати генератор generator_numbers для обчислення загальної суми чисел
# у вхідному рядку та приймати його як аргумент при виклику.
#
# Рекомендації для виконання:
#
# Використовуйте регулярні вирази для ідентифікації дійсних чисел у тексті, з урахуванням, що числа чітко відокремлені пробілами.
# Застосуйте конструкцію yield у функції generator_numbers для створення генератора.
# Переконайтеся, що sum_profit коректно обробляє дані від generator_numbers і підсумовує всі числа.

from decimal import Decimal
import re
def generator_numbers(text):
    pattern = re.compile(r"\s\d+.\d+\s")
    for item in pattern.findall(text):
        yield Decimal(item.strip())

def sum_profit(text, generator_numbers):
    return sum([i for i in generator_numbers(text)])

text = "20.23 Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.34.21"
total_income = sum_profit(text, generator_numbers)
print(f"Total revenue = {total_income}")














