from peewee import *
db = SqliteDatabase('mydatabase.db')
class User (Model):
   name=TextField()
   age=IntegerField()
   class Meta:
      database=db
      db_table='User'

User.create_table()
rec1=User(name="Rajesh", age=21)
rec1.save()