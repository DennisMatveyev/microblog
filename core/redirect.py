import aiohttp.web


def redirect(url):
    return aiohttp.web.HTTPMovedPermanently(url)