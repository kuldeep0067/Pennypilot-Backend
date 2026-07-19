import re
from datetime import datetime

from app.utils.constants import (
    CATEGORIES
)

def is_valid_email(email):

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(
        pattern,
        email
    )
    
def validate_expense(data):

    title = data.get("title")

    amount = data.get("amount")

    category = data.get("category")

    date = data.get("date")

    if not title:

        return False, "Title is required"

    if amount is None:

        return False, "Amount is required"

    if float(amount) < 0:

        return False, "Amount cannot be negative"

    if category not in CATEGORIES:

        return (
            False,
            "Invalid category"
        )

    try:

        datetime.strptime(
            date,
            "%Y-%m-%d"
        )

    except Exception:

        return False, "Invalid date"

    return True, None
