from aiogram import types, F
from aiogram.types import CallbackQuery

from src.handlers.user_handlers.callback.router import router
from src.keyboards import colors_keyboard, thickness_keyboard, scale_keyboard, additional_options_kb, main_menu
from src.logger import logger
from src.materials import THREADS, NEEDLES, CANVAS
from src.user_data import user_data
from src.utils import get_random_recommendation


@router.message(F.text.in_({'Нитки', 'Иголки', 'Канва'}))
async def select_category(message: types.Message):
    category = message.text
    user_data[message.from_user.id]['selected'] = category
    logger.log_info(f"User {message.from_user.id} selected category: {category}")

    if category == "Нитки":
        await message.answer("Какой цвет ниток вы хотите?", reply_markup=colors_keyboard)
    elif category == "Иголки":
        await message.answer("Какую толщину иголок вы хотите?", reply_markup=thickness_keyboard)
    elif category == "Канва":
        await message.answer("Какой масштаб канвы вы хотите?", reply_markup=scale_keyboard)


@router.callback_query(lambda call: call.data in THREADS["Гамма"].keys() or
                                    call.data in NEEDLES["DMC"].keys() or
                                    call.data in CANVAS["Anchor"].keys())
async def recommend_item(callback: CallbackQuery):
    category = user_data[callback.from_user.id]['selected']
    option = callback.data
    user_data[callback.from_user.id]['last_option'] = option
    logger.log_info(f"User {callback.from_user.id} chose option: {option} in category: {category}")

    recommendation = get_random_recommendation(category, option, callback.from_user.id)
    user_data[callback.from_user.id]["last_recommendation"] = recommendation
    await callback.message.answer(text=f"{recommendation}\nДобавить в список или подобрать другой?",
                                  reply_markup=additional_options_kb)


@router.callback_query(F.data == 'add')
async def add_item(callback: CallbackQuery):
    user_id = callback.from_user.id
    recommendation = user_data[user_id]["last_recommendation"]
    user_data[user_id]["list"].append(recommendation)
    logger.log_info(f"User {user_id} added item to list: {recommendation}")

    await callback.message.answer(text="Материал добавлен в список. Хотите выбрать что-то еще?", reply_markup=main_menu)


@router.callback_query(F.data == 'retry')
async def retry(callback: CallbackQuery):
    user_id = callback.from_user.id
    category = user_data.get(user_id, {}).get("selected")
    logger.log_info(f"User {user_id} retried recommendation.")

    if not category:
        logger.log_warning(f"User {user_id} tried to retry without selecting a category.")
        await callback.message.answer("Вы не выбрали категорию. Пожалуйста, начните с главного меню.")
        return

    option = user_data[user_id].get("last_option")
    if not option:
        logger.log_warning(f"User {user_id} has no last option for retry.")

        await callback.message.answer("Не удалось определить последний выбор. Попробуйте снова.")
        return

    # Генерация нового рекомендации
    recommendation = get_random_recommendation(category, option, user_id)
    user_data[user_id]["last_recommendation"] = recommendation
    logger.log_info(f"New recommendation for user {user_id}: {recommendation}")

    # Отправляем ответ пользователю
    await callback.message.answer(
        f"{recommendation}\nДобавить в список или подобрать другой?",
        reply_markup=additional_options_kb
    )