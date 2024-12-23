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
        date = datetime.strptime(needdate, "%Y-%m-%d").date()
        today = datetime.today().date()
        days = (date - today).days
        return days
    except ValueError:
        return "Неправильний формат дати. Будь ласка введіть дату у форматі YYYY-MM-DD."
    except Exception as e:
        return f"Сталася невідома помилка: {e}. Спробуйте ще раз"

print(get_days_from_today("2024-12-23"))


