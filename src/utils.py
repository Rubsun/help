import random

from src.materials import THREADS, NEEDLES, CANVAS
from src.user_data import user_data


def get_random_recommendation(category, option, user_id):
    if category == "Нитки":
        if 'last_firm' in user_data[user_id]:
            available_firms = [firm for firm in THREADS.keys() if firm != user_data[user_id]['last_firm']]
        else:
            available_firms = list(THREADS.keys())

        firm = random.choice(available_firms)
        shade = THREADS[firm][option]
        user_data[user_id]['last_firm'] = firm
        return f"Фирма {firm}, цвет {option}, оттенок {shade}."

    elif category == "Иголки":
        if 'last_firm' in user_data[user_id]:
            available_firms = [firm for firm in NEEDLES.keys() if firm != user_data[user_id]['last_firm']]
        else:
            available_firms = list(NEEDLES.keys())

        firm = random.choice(available_firms)
        size = NEEDLES[firm][option]
        user_data[user_id]['last_firm'] = firm
        return f"Фирма {firm}, толщина {option}, размер {size}."

    elif category == "Канва":
        if 'last_firm' in user_data[user_id]:
            available_firms = [firm for firm in CANVAS.keys() if firm != user_data[user_id]['last_firm']]
        else:
            available_firms = list(CANVAS.keys())

        firm = random.choice(available_firms)
        scale = CANVAS[firm][option]
        user_data[user_id]['last_firm'] = firm
        return f"Фирма {firm}, масштаб {option}: {scale}."
