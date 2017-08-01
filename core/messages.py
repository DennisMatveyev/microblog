from .session import Session


def flash(request,message):
    if 'NEW_FLASHED' in request:
        request['NEW_FLASHED'].append(message)
    else:
        request['NEW_FLASHED'] = [message]


def get_flashed(request):
    return request['FLASHED']


async def messages_middleware(app, handler):

    async def middleware_handler(request):
        if str(request.rel_url).startswith('/static'):
            return await handler(request)

        # Initialize messages
        messages = await Session(request).get('messages')
        if messages is not None:
            await Session(request).remove('messages')
        else:
            messages = []
        request['FLASHED'] = messages

        # Call request handler itself
        response = await handler(request)

        # Store messages
        if 'NEW_FLASHED' in request:
            await Session(request).set('messages', request['NEW_FLASHED'])

        return response

    return middleware_handler


def messages_setup(app):
    app.middlewares.append(messages_middleware)
