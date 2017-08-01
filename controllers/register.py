from forms import RegisterForm
from core import DB, redirect, get_flashed
from models.user import users
from aiohttp_jinja2 import template


@template("register.html")
async def register_page(request):
    form = RegisterForm()
    return dict(
        title='Register',
        form=form,
        messages=get_flashed(request)
    )


@template("register.html")
async def register(request):
    post = await request.post()
    form = RegisterForm(post)
    messages = []
    if form.validate():
        # See if we have such user in the database
        resp = await DB().execute(users.select().where(users.c.login == post['login']))
        # If no such user create it in db
        if len(resp) == 0:
            # Register new user
            await DB().execute(users.insert().values(login=form.login.data,
                                                     name=form.name.data,
                                                     email=form.email.data,
                                                     password=form.password.data))
        else:
            # User exists
            messages.append('User {} already exists!'.format(form.login.data))
            return redirect('login')

        # Redirect to login page
        messages.append('Thank you for registration! You can log in now.')
        return redirect('login')

    messages.append('Invalid registration data!')
    return dict(
        title='Register',
        form=form,
        messages=messages
    )
