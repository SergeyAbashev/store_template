from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_categories, get_items_by_category


# Inline кнопки главного меню.
main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Корзина', callback_data='mybasket'),
     InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])


# Inline кнопка для возващения на главное меню.
to_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='На главную', callback_data='to_main')]
])


async def delete_from_basket(order_id):
    """
    Кнопка удаления из корзины.
    """
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Удалить из корзины', callback_data=f'delete_{order_id}'))
    return keyboard.adjust(2).as_markup()


async def basket(order_id):
    """
    Кнопки корзины.
    """
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Оформить заказ', callback_data=f'order_{order_id}'))
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def categories():
    """
    Кнопки с категориями товаров.
    """
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name,
                                          callback_data=f'category_{category.id}'))
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def items(category_id: int):
    """
    Кнопки товаров.
    """
    items = await get_items_by_category(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in items:
        keyboard.add(InlineKeyboardButton(text=item.name,
                                          callback_data=f"item_{item.id}"))
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()
