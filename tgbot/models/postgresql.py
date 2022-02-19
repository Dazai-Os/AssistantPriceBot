from typing import Union

import asyncpg
from asyncpg.connection import Connection
from asyncpg.pool import Pool
from tgbot.config import load_config

class Database:

    def __init__(self):
        self.pool: Union[Pool, None] =  None

    async def create(self):
        config = load_config(".env")
        self.pool = await asyncpg.create_pool(
            user=config.db.user,
            password=config.db.password,
            host=config.db.host,
            database=config.db.database,
        )

    async def execute (self, command, *args, 
                       fetch: bool = False,
                       fetchval: bool = False,
                       fetchrow: bool = False,
                       execute: bool = False
                       ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result
    
    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Assistant_Price_DB(
        id_number SERIAL PRIMARY KEY,
        id_users BIGINT NOT NULL,
        url_product TEXT NULL,
        name_product TEXT NULL,
        now_price TEXT NULL,
        old_price TEXT NULL
        );
        """
        await self.execute(sql, execute=True)

    async def add_user_product_db(self, id_users, url_product, name_product, now_price):
        check_dublicate = await self.get_url_price()


        result = True

        for i in check_dublicate:
            if (i[0] == id_users) and (i[1] == url_product) and (i[2] == name_product):
                result = False
            
        if result:
                sql = """
                INSERT INTO assistant_price_db (id_users, url_product, name_product, now_price, old_price) VALUES($1, $2, $3, $4, $5)
                """
                await self.execute(sql, id_users, url_product, name_product, now_price, now_price, execute = True)
                return True
        else:
            return False

            

    async def view_product(self, id_users):
        sql = """
        SELECT url_product, name_product, now_price, old_price
        FROM assistant_price_db
        WHERE id_users = """ + str(id_users)
        return await self.execute(sql, fetch = True)

    async def get_url_price(self):
        sql = """ 
        SELECT id_users, url_product, name_product, now_price, id_number
        FROM assistant_price_db
        """
        return await self.execute(sql, fetch = True)

    async def update_price(self, new_price, old_price, id_number):
        sql = f"UPDATE assistant_price_db SET now_price = '{new_price}', old_price = '{old_price}' WHERE id_number = {id_number}"
        await self.execute(sql, execute = True)