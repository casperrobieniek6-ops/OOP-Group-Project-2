"""Input validation helpers for the municipal request system."""
from datetime import datetime


class ErrorValidator:
    """Validates data before it is used to build request objects."""

    VALID_TYPES = {"Maintenance", "EventSupport", "Emergency"}
    VALID_STATUSES = {"Open", "In Progress", "Closed"}

    @staticmethod
    def require_text(value, field_name):
        value = str(value).strip()
        if not value:
            raise ValueError(f"{field_name} cannot be blank.")
        return value

    @staticmethod
    def validate_int(value, field_name, minimum=None, maximum=None):
        try:
            number = int(value)
        except (TypeError, ValueError):
            raise ValueError(f"{field_name} must be a whole number.")
        if minimum is not None and number < minimum:
            raise ValueError(f"{field_name} must be at least {minimum}.")
        if maximum is not None and number > maximum:
            raise ValueError(f"{field_name} must be no more than {maximum}.")
        return number

    @staticmethod
    def validate_float(value, field_name, minimum=None):
        try:
            number = float(value)
        except (TypeError, ValueError):
            raise ValueError(f"{field_name} must be a number.")
        if minimum is not None and number < minimum:
            raise ValueError(f"{field_name} must be at least {minimum}.")
        return number

    @staticmethod
    def validate_status(value):
        value = str(value).strip().title()
        if value not in ErrorValidator.VALID_STATUSES:
            raise ValueError("Status must be Open, In Progress, or Closed.")
        return value

    @staticmethod
    def validate_type(value):
        cleaned = str(value).strip().lower().replace(" ", "")
        type_map = {
            "maintenance": "Maintenance",
            "eventsupport": "EventSupport",
            "event": "EventSupport",
            "emergency": "Emergency",
        }
        if cleaned not in type_map:
            raise ValueError("Request type must be Maintenance, EventSupport, or Emergency.")
        return type_map[cleaned]

    @staticmethod
    def validate_date(value, field_name="Date"):
        value = str(value).strip()
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"{field_name} must use YYYY-MM-DD format.")
        return value
