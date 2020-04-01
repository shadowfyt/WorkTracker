from pyramid.view import view_config
from pyramid.response import Response
from pyramid.request import Request



@view_config(route_name='home', renderer='../templates/home/home.pt')
def home(request):
    return {'project': 'work_tracker'}


@view_config(route_name='expense', renderer='../templates/home/expense.pt')
def expense(request):
    return {'project': 'work_tracker'}
