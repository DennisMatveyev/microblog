import asyncio
import aiohttp.web

from aiohttp_session import setup as session_setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage

from core import templates_setup, DB, messages_setup

from urls import urls
from config import STATIC_PATH, secret_key


def prepare_resources(ioloop):
    ioloop.run_until_complete(asyncio.wait([DB().connect()]))


def main():
    ioloop = asyncio.get_event_loop()
    prepare_resources(ioloop)

    app = aiohttp.web.Application(loop=ioloop)

    session_setup(app, EncryptedCookieStorage(secret_key))
    templates_setup(app)
    messages_setup(app)

    app.router.add_static('/static', STATIC_PATH)
    for method, url, handler in urls:
        app.router.add_route(method.upper(), url, handler)

    aiohttp.web.run_app(app)


if __name__ == '__main__':
    main()
