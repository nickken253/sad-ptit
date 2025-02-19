import mongoengine as me

class Book(me.Document):
    title = me.StringField(required=True, max_length=255)
    author = me.StringField(required=True, max_length=255)
    price = me.DecimalField(required=True, precision=2)
    stock = me.IntField(required=True)
    description = me.StringField()
    # created_at = me.DateTimeField(default=me.datetime.datetime.utcnow)

    def __str__(self):
        return self.title
