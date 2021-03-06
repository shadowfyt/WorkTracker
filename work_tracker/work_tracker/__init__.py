import os

from pyramid.config import Configurator

from work_tracker.data.db_session import DbSession
from work_tracker.data.repository import load_starter_data



def main(_, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_chameleon')
        config.include('.routes')
        config.scan()

    init_db()
    return config.make_wsgi_app()


def init_db():
    db_file = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'db',
        'work_tracker.sqlite'
    )
    DbSession.global_init(db_file)
    load_starter_data()