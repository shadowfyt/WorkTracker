from typing import Optional

from sqlalchemy.orm import subqueryload
from sqlalchemy.orm import Session

from work_tracker.data.db_session import DbSession
from work_tracker.data.models.expense import Expense
from work_tracker.data.models.users import User
import dateutil.parser
from datetime import datetime

def load_starter_data():
    print('Loading starter data...')
    session = DbSession.create_session()
    if session.query(Expense).count() > 0:
        session.close()
        print('data already loaded')
        return
    session.expire_on_commit = False

    user = get_default_user(session)
    get_default_expense(user)
    
    session.commit()
    session.close()

def get_default_user(session: Session):

    user = session.query(User).filter(User.email == 'Doan_ryan@hotmail.com').first()
    if user:
        return user

    session.expire_on_commit = False
    user = User()
    user.email = 'Doan_ryan@hotmail.com'
    user.name = 'ryan'
    user.created_date = datetime.now()

    session.add(user)
    return user


def get_default_expense(user):
    user = user
    expense = Expense()
    expense.created_date = datetime.now()
    expense.store_name = 'shop'
    expense.cost = 50
    expense.des = 'hammer'
    user_id = user.id
    user.expenses.append(expense)


def get_user_by_id(user_id:int, include_expenses=True) ->Optional[User]:
    session = DbSession.create_session()
    try:
        if not include_expenses:
            return session.query(User).filter(User.id == user_id).first()
        
        else:
            return session.query(User).options(subqueryload(User.expenses)).filter(User.id == user_id).first()

    finally:
        session.close()

def get_expense_by_id(expense_id: int) -> Optional:
    session = DbSession.create_session()
    try:
        return session.query(Expense).filter(Expense.id == expense_id).first()

    finally:
        session.close()


def add_new_expense(user, des, cost, store):
    session = DbSession.create_session()

    session.expire_on_commit = False

    user = user
    expense = Expense()
    expense.created_date = datetime.now()
    expense.des = des
    expense.cost = cost
    expense.store_name = store
    expense.user_id = user.id
    user.expenses.append(expense)

    session.add(expense)
    session.commit()
    session.close()