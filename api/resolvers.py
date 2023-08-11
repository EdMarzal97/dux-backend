from datetime import datetime
from models.models import User, App, Lumos
from api import db


def resolve_users(obj, info):
    return User.query.all()

def resolve_user(obj, info, user_id):
    return User.query.get(user_id)

def resolve_create_user(obj, info, username, email, password):
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def resolve_update_user(obj, info, user_id, input):
    user = User.query.get(user_id)
    if user:
        for key, value in input.items():
            setattr(user, key, value)
        db.session.commit()
        return user
    return None

def resolve_delete_user(obj, info, user_id, input):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False
        
def resolve_apps(obj, info):
    return App.query.all()

def resolve_app(obj, info, app_id):
    return App.query.get(app_id)

def resolve_create_app(obj, info, app_name, app_icon):
    new_app = App(app_name=app_name, app_icon=app_icon)
    db.session.add(new_app)
    db.session.commit()
    return new_app

def resolve_update_app(obj, info, app_id, input):
    app = App.query.get(app_id)
    if app:
        for key, value in input.items():
            setattr(app, key, value)
        db.session.commit()
        return app
    return None

def resolve_delete_app(obj, info, app_id):
    app = App.query.get(app_id)
    if app:
        db.session.delete(app)
        db.session.commit()
        return True
    return False

def resolve_lumos(obj, info, lumos_id):
    return Lumos.query.get(lumos_id)

#possible resolvers for get Lumos information throught app or user
#def resolve_lumos_for_user(obj, info, user_id):
 #   return User.query.get(user_id).app_lumos

#def resolve_lumos_for_app(obj, info, app_id):
 #   return App.query.get(app_id).user_lumos

def resolve_create_lumos(obj, info, user_id, app_id, permission_level):
    new_lumos = Lumos(
        user_id=user_id,
        app_id=app_id,
        permission_level=permission_level,
        activation_date=datetime,
        expiration_date=datetime,
        account_status='active'
    )
    db.session.add(new_lumos)
    db.session.commit()
    return new_lumos

def resolve_update_Lumos(obj, info, lumos_id, input):
    lumos = Lumos.query.get(lumos_id)
    if lumos:
        for key, value in input.items():
            setattr(lumos, key, value)
        db.session.commit()
        return lumos
    return None

def resolve_delete_Lumos(obj, info, lumos_id):
    lumos = Lumos.query.get(lumos_id)
    if lumos:
        db.session.delete(lumos)
        db.session.commit()
        return True
    return False