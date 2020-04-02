import datetime
import sqlalchemy
from typing import List
from sqlalchemy import orm
from work_tracker.data.modelbase import SqlAlchemyBase
from work_tracker.data.models.expense import Expense

class User(SqlAlchemyBase):
    __tablename__="users"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True )
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True, index=True)

    expenses = orm.relation("Expense", order_by=Expense.created_date.desc(), back_populates='user')

    @property
    def total_expense(self)-> List[Expense]:
        return sum[self.expenses.cost]
