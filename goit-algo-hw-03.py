#Homework Module_3_hmw_1

from datetime import datetime # імпортуємо модуль datetime з бібліотеки datetime


def get_days_from_today(needdate):
    """перетворюємо рядок у дату, 
    присвоюємо сьогоднішню дату, 
    розраховуємо кількість днів від сьогоднішньої дати до потрібної дати
    та повертає кількість днів.
    Обробляємо помилки та вказуємо потрібний формат дати.
    """
    try:
        date = datetime.strptime(needdate, "%Y-%m-%d")
        today = datetime.today()
        days = (date - today).days
        return days
    except ValueError:
        return "Неправильний формат дати. Будь ласка введіть дату у форматі YYYY-MM-DD."
    except Exception as e:
        return f"Сталася невідома помилка: {e}. Спробуйте ще раз"

print(get_days_from_today("2022-10-05"))





#Homework Module_3_hmw_2 без коментарів та пустих списків якщо параметри некоректні
import random

def get_numbers_ticket(min, max, quantity):
    return [random.randint(1, 1000) for _ in range(6)]


print(get_numbers_ticket(1, 1000, 6))





#Homework Module_3_hmw_2 з коректними параметрами
import random

def get_numbers_ticket(min, max, quantity):
    """
    Перевірямо спочатку коректность параметрів
    Повертаємо порожній список, якщо параметри некоректні
    Генеруємо унікальні випадкові числа в заданому діапазоні
    Повертаємо відсортований список чисел
    """
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []  
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)

# Приклад використання:
print(get_numbers_ticket(1, 49, 6))  # Для лотереї з 6 чисел від 1 до 49
print(get_numbers_ticket(1, 36, 5))  # Для лотереї з 5 чисел від 1 до 36
print(get_numbers_ticket(1, 1000, 6))  # Для лотереї з 6 чисел від 1 до 1000

