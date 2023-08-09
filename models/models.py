"""here we are modelating the tables and atributes for the DB"""
from api import db


# we define the class that is gonna be used in the DB
class User(db.Model):
    """class representing a User that gonna request the apps"""

    id: db.Column(db.Interger, primary_key=True)
    name: db.Column(db.String)
    email: db.Column(db.String)
    password: db.Column(db.String)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
