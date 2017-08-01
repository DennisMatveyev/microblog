import aiohttp_jinja2
import jinja2
from config import TEMPLATE_PATH


def templates_setup(httpserver):
    aiohttp_jinja2.setup(httpserver, loader=jinja2.FileSystemLoader(TEMPLATE_PATH))



