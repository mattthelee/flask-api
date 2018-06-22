from flaskApi import app, db

class Message(db.Model):
    """docstring for Message."""
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(64))

    def to_dict(self):
        data = {
            'id' : self.id,
            'body': self.body
        }
        return data

    def from_dict(self,data):
        for field in "body":
            if field in data:
                setattr(self, field, data[field])

    def __repr__(self):
        return '<{} : {}>'.format(self.body,self.body)
