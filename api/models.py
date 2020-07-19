from mongoengine import Document, fields
import datetime

# Create your models here.
class House(Document):
    
    name = fields.StringField(max_length=32)
    origin = fields.StringField(max_length=16, default='INDIA')
    price = fields.StringField(max_length=10)
    sold = fields.DateTimeField(default=datetime.datetime.now)
    tags = fields.ListField(required=False, null=True)

