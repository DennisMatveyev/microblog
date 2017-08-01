from controllers import *


urls = [
    ('GET', '/', index),
    ('POST', '/', add_post),

    ('GET', '/login', login_page),
    ('POST', '/login', login),
    ('GET',  '/log_out', log_out),

    ('GET', '/register', register_page),
    ('POST', '/register', register),

]
