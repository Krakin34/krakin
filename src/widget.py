from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(data: str) -> str:
    """Функция кодировки счета/карты"""
    parts = data.split()
    name = "".join(parts[:-1])
    number_str = parts[-1]
    if number_str.isdigit():
        number = int(number_str)  # Новая переменная number (int)
    else:
        return "Ошибка: Номер некорректный."

    number = int(number)
    masked_number_card = get_mask_card_number(number)
    masked_number_account = get_mask_account(number)

    if len(str(number)) == 16:
        return f"{name} {masked_number_card}"
    elif len(str(number)) == 20:
        return f"{name} {masked_number_account}"
    else:
        return "Ошибка: Номер некорректный."


def get_date(date_time: str) -> str:
    """Функция для преобразования даты и времени в формат ДД.ММ.ГГГГ"""
    return f"{date_time[8:10]}.{date_time[5:7]}.{date_time[:4]}"
