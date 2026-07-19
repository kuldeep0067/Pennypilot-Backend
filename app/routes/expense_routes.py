from flask import Blueprint

from flask import request

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from app.services.expense_service import (
    create_expense
)

from app.utils.response import (
    success_response,
    error_response
)

expense_bp = Blueprint(
    "expense",
    __name__,
    url_prefix="/api/expenses"
)

@expense_bp.route(
    "",
    methods=["POST"]
)
@jwt_required()
def add_expense():

    data = request.get_json()

    user_id = get_jwt_identity()

    success, message = create_expense(
        data,
        user_id
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