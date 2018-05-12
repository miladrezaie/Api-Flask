from Model.BaseModel import BaseModel, EnumField
from peewee import IntegerField, PrimaryKeyField


class TimeCourse(BaseModel):
    id = PrimaryKeyField()
    days = IntegerField(30)
    time = IntegerField(30)
    classes = IntegerField(30)
    rotatory = EnumField(choices=['1', '2'])
    day_rotatory = EnumField(choices=['zoj', 'fard'])

    class Meta:
        db_table = "time_course"
