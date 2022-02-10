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
        old_price TEXT NULL,
        track BOOLEAN NOT NULL
        );
        """
        await self.execute(sql, execute=True)
    
    async def add_user_product(self, id_users, url_product, name_product, now_price,track):
        sql = """
        INSERT INTO assistant_price_db (id_users, url_product, name_product, now_price, old_price, track) VALUES($1, $2, $3, $4, $5, $6)
        """
        await self.execute(sql, id_users, url_product, name_product, now_price, now_price, track, fetchrow = True)