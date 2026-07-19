from flask import Blueprint

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from app.models.user import User

from app.utils.response import (
    success_response
)

user_bp = Blueprint(
    "user",
    __name__,
    url_prefix="/api/user"
)


@user_bp.route(
    "/me",
    methods=["GET"]
)
@jwt_required()
def current_user():

    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    return success_response(
        "Current user fetched",
        {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    )