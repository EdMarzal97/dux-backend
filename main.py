"""main file for start the app"""
from api import app, db
from models import models
from ariadne import make_executable_schema, load_schema_from_path, ObjectType
from api.resolvers import resolve_users, resolve_user, resolve_create_user, resolve_update_user, resolve_delete_user, resolve_apps, resolve_app, resolve_create_app, resolve_update_app, resolve_delete_app, resolve_lumos, resolve_create_lumos, resolve_update_Lumos, resolve_delete_Lumos


app.app_context().push()
# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    app.run(debug=True)
