"""here we are modelating the tables and atributes for the DB"""
from api import db


# we define the class that is gonna be used in the DB
class User(db.Model):
    """class representing a User that gonna request the apps"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    apps = db.relationship('Lumos', back_populates='user', lazy='dynamic')
    

    def serialize(self):
        """Method that translates the data into a JSON / Dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
        }


class App(db.Model):
    """class for the applications of the appstore"""

    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String, nullable=False)
    app_icon = db.Column(db.String, nullable=False)
    users = db.relationship('Lumos', back_populates='app', lazy='dynamic')
    

    def serialize(self):
        """same function for JSON formating"""
        return {
            "id": self.id, 
            "app_name": self.app_name, 
            "app_icon": self.app_icon
        }


class Lumos(db.Model):
    """the many to many relationship table"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    app_id = db.Column(db.Integer, db.ForeignKey('app.id')) 
    permission_level = db.Column(db.Integer, nullable=False)
    activation_date = db.Column(db.DateTime, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    account_status = db.Column(db.String, nullable=False)

    user = db.relationship('User', back_populates='apps')
    app = db.relationship('App', back_populates='users')

    def serialize(self):
        """Method that translates the data into a JSON / Dictionary."""
        return {
            "user_id": self.user_id,
            "app_id": self.app_id,
            "permission_level": self.permission_level,
            "activation_date": self.activation_date,
            "expiration_date": self.expiration_date,
            "account_status": self.account_status
        }

