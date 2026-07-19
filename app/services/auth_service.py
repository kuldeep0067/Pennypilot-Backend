from werkzeug.security import generate_password_hash

from app.extensions.database import db

from app.models.user import User

from app.utils.validators import is_valid_email

from werkzeug.security import (
        check_password_hash
    )

from flask_jwt_extended import (
      create_access_token
    )


def register_user(data):

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name:
        return False, "Name is required"

    if not email:
        return False, "Email is required"

    if not password:
        return False, "Password is required"

    if not is_valid_email(email):
        return False, "Invalid email"

    existing_user = User.query.filter_by(
        email=email
    ).first()

    if existing_user:
        return False, "Email already exists"

    hashed_password = generate_password_hash(
        password
    )

    user = User(
        name=name,
        email=email,
        password=hashed_password
    )

    db.session.add(user)

    db.session.commit()

    return True, "User registered successfully"

def login_user(data):

    email = data.get("email")

    password = data.get("password")

    if not email:

        return False, "Email is required", None

    if not password:

        return False, "Password is required", None

    user = User.query.filter_by(
        email=email
    ).first()

    if not user:

        return False, "Invalid credentials", None

    if not check_password_hash(
        user.password,
        password
    ):

        return False, "Invalid credentials", None

    access_token = create_access_token(
        identity=str(user.id)
    )

    return (
        True,
        "Login successful",
        access_token
    )