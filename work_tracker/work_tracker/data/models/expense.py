import datetime
import sqlalchemy
from sqlalchemy import orm
from billtracker.data.modelbase import SqlAlchemyBase

class Expense(SqlAlchemyBase):
    __tablename__="expenses"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    store_name = sqlalchemy.Column(sqlalchemy.String, index=True)
    cost = sqlalchemy.Column(sqlalchemy.Float, default=0, index=True)
    desc = sqlalchemy.Column(sqlalchemy.String, index=True)