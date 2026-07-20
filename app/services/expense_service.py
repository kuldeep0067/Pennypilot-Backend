from datetime import datetime

from app.extensions.database import db

from app.models.expense import Expense

from app.utils.validators import (
    validate_expense
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
