from core import DB, redirect, Session, flash
from forms import LoginForm
from models.user import users
from aiohttp_jinja2 import template


@template('login.html')
async def login_page(request):
    return dict(title='Sign In', messages=[], form=LoginForm())


async def log_out(request):
    session = Session(request)
    await session.remove('user')
    return redirect('/login')


@template('login.html')
async def login(request):
    post_request = await request.post()
    form = LoginForm(post_request)

    if form.validate():
        # See if we have such user in the database
        resp = await DB().execute(users.select().where(users.c.login == post_request['login']))
        user = resp[0] if len(resp) else None

        if user is None:
            flash(request, 'No such user! "{}" Please register!'.format(post_request['login']))
            return redirect('/register')
        elif user.password == post_request['password']:
            session = Session(request)
            await session.set('user', dict(user))
            return redirect('/')
        else:
            messages = ['Invalid password!']
            return dict(title='Sign In', messages=messages, form=form)

    return dict(title='Sign In', messages=['Validation failed!'], form=form)

