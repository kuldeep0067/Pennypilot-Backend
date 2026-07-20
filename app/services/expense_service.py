from datetime import datetime

from app.extensions.database import db

from app.models.expense import Expense

from app.utils.validators import (
    validate_expense
)

from app.utils.validators import (
    validate_expense,
    validate_expense_update
)


def create_expense(
    data,
    user_id
):

    valid, error = validate_expense(
        data
    )

    if not valid:

        return False, error

    expense = Expense(

        title=data.get("title"),

        amount=data.get("amount"),

        category=data.get("category"),

        date=datetime.strptime(
            data.get("date"),
            "%Y-%m-%d"
        ).date(),

        description=data.get(
            "description"
        ),

        user_id=user_id
    )

    db.session.add(expense)

    db.session.commit()

    return (
        True,
        "Expense created successfully"
    )
    
def get_all_expenses(user_id):

    expenses = Expense.query.filter_by(
        user_id=user_id
    ).order_by(
        Expense.created_at.desc()
    ).all()

    expense_list = [
        expense.to_dict()
        for expense in expenses
    ]

    return expense_list

def get_expense_by_id(
    expense_id,
    user_id
):

    expense = Expense.query.get(
        expense_id
    )

    if not expense:

        return (
            False,
            "Expense not found",
            None,
            404
        )

    if expense.user_id != int(user_id):

        return (
            False,
            "Access denied",
            None,
            403
        )

    return (
        True,
        "Expense fetched successfully",
        expense.to_dict(),
        200
    )
    
def update_expense(
    expense_id,
    user_id,
    data
):

    expense = Expense.query.get(
        expense_id
    )

    if not expense:

        return (
            False,
            "Expense not found",
            404
        )

    if expense.user_id != int(user_id):

        return (
            False,
            "Access denied",
            403
        )

    valid, error = (
        validate_expense_update(
            data
        )
    )

    if not valid:

        return (
            False,
            error,
            400
        )

    if "title" in data:

        expense.title = data["title"]

    if "amount" in data:

        expense.amount = float(
            data["amount"]
        )

    if "category" in data:

        expense.category = (
            data["category"]
        )

    if "description" in data:

        expense.description = (
            data["description"]
        )

    if "date" in data:

        expense.date = (
            datetime.strptime(
                data["date"],
                "%Y-%m-%d"
            ).date()
        )

    db.session.commit()

    return (
        True,
        "Expense updated successfully",
        200
    )