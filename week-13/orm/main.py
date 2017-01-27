from ikea.fields import PKColumn, IntegerColumn, TextColumn
from ikea.models import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    id = PKColumn()
    name = TextColumn(max_length=100)
    age = IntegerColumn(number=20)


class Student(User):
    email = TextColumn()
    shirt_size = IntegerColumn(number=1)


# Creating all tables from BaseModelMeta class
BaseModel.create_all_tables()

