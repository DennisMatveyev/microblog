import aiopg.sa

from config import SQLALCHEMY_DATABASE_URI


class DB(object):
    obj = None

    def __new__(cls):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
        return cls.obj

    async def connect(self):
        self.pool = await aiopg.sa.create_engine(SQLALCHEMY_DATABASE_URI)

    async def execute(self, query):
        resp = []
        async with self.pool.acquire() as conn:
            async for row in conn.execute(query):
                resp.append(row)
        return resp


