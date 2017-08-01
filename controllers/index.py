import datetime
from core.db import DB
from core.session import Session, login_required
from core.redirect import redirect
from forms.post import PostForm
from models.post import posts
from models.user import users
from config import POSTS_PER_PAGE
from sqlalchemy import select, func, desc
from aiohttp_jinja2 import template


@login_required
@template("index.html")
async def index(request):
    # Form for new posts
    session = Session(request)
    messages = []
    current_user = await session.get('user')
    # Get existing posts
    page = int(request.GET.get('page') or 1)

    current_page_query = select([posts, users.c.name])\
        .where(users.c.id == posts.c.user_id)\
        .order_by(desc(posts.c.timestamp))\
        .limit(POSTS_PER_PAGE)\
        .offset((page-1)*POSTS_PER_PAGE)

    posts_list = await DB().execute(current_page_query)

    if page == 1 and len(posts_list) < POSTS_PER_PAGE:
        total = len(posts_list)
    else:
        total = (await DB().execute(select([func.count()])
                                    .where(users.c.id == posts.c.user_id)))[0][0]

    return dict(
        title='Home',
        form=PostForm(),
        messages=messages,
        user=current_user,
        posts=posts_list,
        has_prev=True if page > 1 else False,
        has_next=True if total > page*POSTS_PER_PAGE else False,
        page=page,
        current_user=current_user)


@login_required
@template('index.html')
async def add_post(request):
    # Form for new posts
    post = await request.post()
    form = PostForm(post)
    session = Session(request)
    current_user = await session.get('user')
    if form.validate():
        await DB().execute(posts.insert().values(body=form.post.data,
                                                 timestamp=datetime.datetime.utcnow(),
                                                 user_id=current_user['id']))
        return redirect('/')
    else:
        return redirect('/')


