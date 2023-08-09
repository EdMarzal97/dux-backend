"""here we are modelating the tables and atributes for the DB"""
from api import db


# we define the class that is gonna be used in the DB
class User(db.Model):
    """class representing a User that gonna request the apps"""

    id: db.Column(db.Interger, primary_key=True)
    name: db.Column(db.String, nullable=False)
    email: db.Column(db.String, nullable=False)
    password: db.Column(db.String, nullable=False)

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

    id: db.Column(db.Interger, primary_Key=True)
    app_name: db.Column(db.Strin, nullable=False)
    app_icon: db.Column(db.string, nullable=False)

    def serialize(self):
        """same function for JSON formating"""
        return {
            "id": self.id, 
            "app_name": self.app_name, 
            "app_icon": self.app_icon
        }


user_app = db.Table(
    "user_app",
    db.Column("user_id", db.Integer, db.ForeingKey(User.id), primary_key=True),
    db.Column("app_id", db.Integer, db.ForeingKey(App.id), primary_key=True),
    db.Column("permission_level", db.String, nullable=False),
    db.Column("activation_date", db.DateTime, nullable=False),
    db.Column("finish_date", db.DateTime, nullable=False),
    db.Column("account_status", db.String, nullable=False),
)
