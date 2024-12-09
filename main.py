from src.masks import get_mask_account, get_mask_card_number

# импорт функций при помощи абсолютным путём

"""Запрос функций, для маскировки номера карты в числовом значении, маскируется '*'. """

# Вывод функции
if __name__ == "__main__":

    # Вызов функции
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
