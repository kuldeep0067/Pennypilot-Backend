from flask import Blueprint

from flask import request

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from app.services.expense_service import (
    create_expense,
    get_all_expenses,
    get_expense_by_id
)

from app.utils.response import (
    success_response,
    error_response
)

from app.services.expense_service import (
    create_expense,
    get_all_expenses,
    get_expense_by_id,
    update_expense
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
    
@expense_bp.route(
    "",
    methods=["GET"]
)
@jwt_required()
def get_expenses():

    user_id = get_jwt_identity()

    expenses = get_all_expenses(
        user_id
    )

    return success_response(
        "Expenses fetched successfully",
        expenses
    )
    
@expense_bp.route(
    "/<int:expense_id>",
    methods=["GET"]
)
@jwt_required()
def get_expense(expense_id):

    user_id = get_jwt_identity()

    success, message, data, status = (
        get_expense_by_id(
            expense_id,
            user_id
        )
    )

    if not success:

        return error_response(
            message,
            status
        )

    return success_response(
        message,
        data,
        status
    )
    
@expense_bp.route(
    "/<int:expense_id>",
    methods=["PUT"]
)
@jwt_required()
def edit_expense(expense_id):

    user_id = get_jwt_identity()

    data = request.get_json()

    success, message, status = (
        update_expense(
            expense_id,
            user_id,
            data
        )
    )

    if not success:

        return error_response(
            message,
            status
        )

    return success_response(
        message,
        status_code=status
    )