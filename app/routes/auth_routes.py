from flask import Blueprint

from flask import request

from app.services.auth_service import (
    register_user
)

from app.utils.response import (
    success_response,
    error_response
)

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)


@auth_bp.route(
    "/register",
    methods=["POST"]
)
def register():

    data = request.get_json()

    success, message = register_user(
        data
    )

    if not success:

        return error_response(
            message,
            400
        )

    return success_response(
        message,
        status_code=201
    )