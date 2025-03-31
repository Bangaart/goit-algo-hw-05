# Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти читати лог-файл, переданий як аргумент командного рядка,
# і виводити статистику за рівнями логування наприклад, INFO, ERROR, DEBUG. Також користувач може вказати рівень логування як другий
# аргумент командного рядка, щоб отримати всі записи цього рівня.

# Файли логів – це файли, що містять записи про події, які відбулися в операційній системі, програмному забезпеченні або інших системах.
# Вони допомагають відстежувати та аналізувати поведінку системи, виявляти та діагностувати проблеми.

# Вимоги до завдання:
#
# Скрипт повинен приймати шлях до файлу логів як аргумент командного рядка.
# Скрипт повинен приймати не обов('язковий аргумент командного рядка, після аргументу шляху до файлу логів. Він відповідає за виведення всіх '
#                                 'записи певного рівня логування. І приймає значення відповідно до рівня логування файлу. Наприклад аргумент '
#                                 'error виведе всі записи рівня ERROR з файлу логів.)
# Скрипт має зчитувати і аналізувати лог-файл, підраховуючи кількість записів для кожного рівня логування (INFO, ERROR, DEBUG, WARNING).
# Реалізуйте функцію parse_log_line(line: str) -> dict для парсингу рядків логу.
# Реалізуйте функцію load_logs(file_path: str) -> list для завантаження логів з файлу.
# Реалізуйте функцію filter_logs_by_level(logs: list, level: str) -> list для фільтрації логів за рівнем.
# Реалізуйте функцію count_logs_by_level(logs: list) -> dict для підрахунку записів за рівнем логування.
# Результати мають бути представлені у вигляді таблиці з кількістю записів для кожного рівня. Для цього реалізуйте
# функцію display_log_counts(counts: dict), яка форматує та виводить результати. Вона приймає результати виконання функції count_logs_by_level.

import sys

from collections import defaultdict


def parse_log_line(line: str) -> dict:
    log_dict = {}
    for index, item in enumerate(["date", "time", "level", "message"]):
        log_dict[item] = line.split(maxsplit=3)[index].strip()
    return log_dict

def load_logs(path: str) -> list:
    try:
        list_logs = [parse_log_line(i) for i in open(path, encoding='utf-8')]
    except (FileNotFoundError, FileExistsError):
        print("File doesn't exist ")
    except UnicodeDecodeError:
        print("File has no UTF-8 encoding")
    except IndexError:
        print("File is empty")
    else:
        return list_logs

def filter_logs_by_level(logs: list , level:str) -> list:
    filtered_list =[]
    for item in logs:
        if item["level"] == level.upper():
            filtered_list.append(item)
    return filtered_list

def count_logs_by_level(logs : list) -> dict:
    level_dict = defaultdict(int)
    for i in logs:
        level_dict[i["level"]] += 1
    return level_dict

def display_log_counts(counts: dict):
    print("Logs level | Quantity\n-----------|---------")
    for key, value in counts.items():
        print(f"{key:<10} | {value:^10}")

if __name__ == "__main__":
    path = sys.argv[1]
    level = sys.argv[2].lower() if len(sys.argv) > 2 else None

    logs = load_logs(path)
    count_logs = count_logs_by_level(logs)

    if level:
        display_log_counts(count_logs)
        print(f"Details for '{level.upper()}' level:")
        for item in filter_logs_by_level(logs, level):
            print(f"{item["date"]} {item["time"]} - {item["message"]}")
    else:
        display_log_counts(count_logs)




