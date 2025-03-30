# Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.

# Вимоги до завдання:
#
# Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. Цей декоратор відповідає за повернення користувачеві
# повідомлень типу "Enter user name", "Give me name and phone please" тощо.
# Декоратор input_error повинен обробляти винятки, що виникають у функціях — handler — і це винятки KeyError, ValueError, IndexError.
# Коли відбувається виняток декоратор повинен повертати відповідь користувачеві. Виконання програми при цьому не припиняється.

def input_error(func):                        # Decorator for errors
    def inner(*args, **kwargs):
        try:
            return func(*args,**kwargs)
        except ValueError:
            return "Enter the arguments for the command"
        except IndexError:
            return "Enter user name"
        except KeyError:
            return "There is no such name"
    return inner

@input_error
def input_parcer(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_command(args,contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"

@input_error
def change_username(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed"

@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts[name]

def get_all(contacts):
    return [f"{key} : {value}" for key ,value in contacts.items()]

def main():
    contacts = {}
    print("Welcome to assistant bot")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = input_parcer(user_input)


        if command in ["exit", "close"]:
            print("Good bye")
            break
        elif command == "hello":
            print("How can i help you")
        elif command == "add":
            print(add_command(args, contacts))
        elif command == "change":
            print(change_username(args,contacts))
        elif command == "phone":
            print(get_phone(args,contacts))
        elif command == "all":
            print(*get_all(contacts))
        else:
             print("Invalid command or empty input")

if __name__ == "__main__":
    main()
