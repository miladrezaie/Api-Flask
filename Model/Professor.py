from Model.BaseModel import BaseModel, EnumField
from peewee import TextField, CharField, PrimaryKeyField


class Professor(BaseModel):
    id = PrimaryKeyField()
    firstname = CharField(45)
    lastname = CharField(45)
    father = CharField(45)
    sex = EnumField(choices=["male", "female"])
    national_code = CharField(unique=True)
    birthday = CharField(45)
    location_brith = CharField(45)
    phone = CharField(45)
    mobile = CharField(45)
    password = TextField()
    address = TextField()
    img = CharField(45)

    class Meta:
        db_table = "professor"
