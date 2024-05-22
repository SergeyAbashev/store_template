from app.database.models import User, Category, Item, Basket
from app.database.models import async_session

from sqlalchemy import select, update, delete


async def set_user(tg_id):
    """
    Запрос из бд ID пользователя, если нет, добавляем.
    """
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        
        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def set_item(data):
    """
    Добавляем в бд информацию о продукте. 
    """
    async with async_session() as session:
        session.add(Item(**data))
        await session.commit()


async def set_basket(tg_id, item_id):
    """
    Добавление в бд ин формации о заказе.
    """
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        session.add(Basket(user=user.id, item=item_id))
        await session.commit()


async def get_basket(tg_id):
    """
    Получение из бд заказа.
    """
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        basket = await session.scalars(select(Basket).where(Basket.user == user.id))
        return basket


async def get_users():
    """
    Получение из бд пользователя.
    """
    async with async_session() as session:
        users = await session.scalars(select(User))
        return users


async def get_categories():
    """
    ПОлучение из бд категорий.
    """
    async with async_session() as session:
        categories = await session.scalars(select(Category))
        return categories


async def get_items_by_category(category_id: int):
    """
    ПОлучение из бд товаров выбранной категории.
    """
    async with async_session() as session:
        items = await session.scalars(select(Item).where(Item.category == category_id))
        return items


async def get_item_by_id(item_id: int):
    """
    Получение товара из бд по ID.
    """
    async with async_session() as session:
        item = await session.scalar(select(Item).where(Item.id == item_id))
        return item


async def delete_basket(tg_id, item_id):
    """
    Удаление заказа из бд.
    """
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        await session.execute(delete(Basket).where(Basket.user == user.id, Basket.item == item_id))
        await session.commit()
