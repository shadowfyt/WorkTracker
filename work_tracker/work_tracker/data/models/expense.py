import datetime
import sqlalchemy
from sqlalchemy import orm
from work_tracker.data.modelbase import SqlAlchemyBase

class Expense(SqlAlchemyBase):
    __tablename__="expenses"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    store_name = sqlalchemy.Column(sqlalchemy.String, index=True)
    cost = sqlalchemy.Column(sqlalchemy.Float, default=0, index=True)
    des = sqlalchemy.Column(sqlalchemy.String, index=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    user = orm.relation('User', back_populates='expenses')

