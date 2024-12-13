from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


def create_inline_keyboard(options: list, row_width: int = 3) -> InlineKeyboardMarkup:
    keyboard_buttons = [
        [InlineKeyboardButton(text=options[i + j], callback_data=options[i + j])
         for j in range(min(row_width, len(options) - i))]
        for i in range(0, len(options), row_width)
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)


colors_keyboard = create_inline_keyboard([
    "Красный", "Оранжевый", "Желтый", "Зеленый", "Голубой",
    "Синий", "Фиолетовый", "Розовый", "Черный", "Белый",
    "Бежевый", "Коричневый"
])

thickness_keyboard = create_inline_keyboard(["Тонкие", "Средние", "Толстые"])
scale_keyboard = create_inline_keyboard(["Мелкая", "Средняя", "Крупная"])

main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, keyboard=[
    [KeyboardButton(text='Нитки')],
    [KeyboardButton(text='Иголки')],
    [KeyboardButton(text='Канва')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Очистить корзину')],
])

additional_options_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить', callback_data='add')],
    [InlineKeyboardButton(text='Подобрать другой', callback_data='retry')],
])
