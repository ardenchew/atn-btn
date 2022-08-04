from ariadne import convert_kwargs_to_snake_case
from models.user import User
from app import db

@convert_kwargs_to_snake_case
def user_resolver(obj, info, id):
    user = User.query.get(id)
    return {
        "id": user.id,
        "email": user.email,
    }

@convert_kwargs_to_snake_case
def createUser_resolver(obj, info, email):
    new_user = User(email)
    db.session.add(new_user)
    db.session.commit()

    return {
        "id": new_user.id,
    }
