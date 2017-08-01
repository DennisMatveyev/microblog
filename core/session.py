import functools
import aiohttp.web
import aiohttp_session


class Session():
    def __init__(self, request):
        self.request = request
        self._session = None

    async def get_session(self):
        if self._session is None:
            self._session = await aiohttp_session.get_session(self.request)
        return self._session

    async def get(self, key):
        s = await self.get_session()
        return s[key] if key in s else None

    async def set(self, key, value):
        (await self.get_session())[key] = value

    async def remove(self, key):
        del (await self.get_session())[key]


def login_required(method):
    @functools.wraps(method)
    async def wrapper(request, *args, **kwargs):
        sess = Session(request)
        user = await sess.get('user')
        if not user:
            return aiohttp.web.HTTPMovedPermanently('/login')
        return await method(request, *args, **kwargs)
    return wrapper

