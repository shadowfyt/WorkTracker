from pyramid.view import view_config
from pyramid.response import Response
from pyramid.request import Request
from pyramid.httpexceptions import HTTPFound

from work_tracker.data import repository



@view_config(route_name='home', renderer='../templates/home/default.pt')
def home(request: Request):
    user_id = 1
    user = repository.get_user_by_id(user_id)
    return {
        'user': user
    }


@view_config(route_name='expense', renderer='../templates/home/expense.pt', request_method="GET")
def expense_get(request: Request):

    user_id = 1
    user = repository.get_user_by_id(user_id)

    return {
        'user': user,
        'error': None
    }

@view_config(route_name='expense', renderer='../templates/home/expense.pt', request_method='POST')
def expense_post(request: Request):

    user_id = 1
    user = repository.get_user_by_id(user_id)

    store = request.POST.get('store')
    cost = int(request.POST.get('cost'))
    des = request.POST.get('des')
    if cost < 0:
        error = 'aint nothing free'
        return {
            'user': user,
            'error': None,
            'store': store,
            'des': des,
            'cost': cost,

        }
    repository.add_new_expense(user, des, cost, store)
    return HTTPFound(location='/expense')
