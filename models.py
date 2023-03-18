from mongoengine import Document, StringField, IntField, ListField
class Employee(Document):
    emp_id = IntField()
    name = StringField(max_lenght =100)
    age = IntField()
    teams = ListField()

class User(Document):
    username = StringField()
    password = StringField()
    
    
    
