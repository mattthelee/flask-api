from flaskApi import app, db

class Task(db.Model):
    """docstring for Task."""
    id = db.Column(db.Integer,primary_key=True)
    longDescription = db.Column(db.String(64))

    def to_dict(self):
        data = {
            'id' : self.id,
            'longDescription': self.longDescription
        }
        return data

    def from_dict(self,data):
        for field in "longDescription":
            if field in data:
                setattr(self, field, data[field])

    def __repr__(self):
        return '<{} : {}>'.format(self.body,self.longDescription)
