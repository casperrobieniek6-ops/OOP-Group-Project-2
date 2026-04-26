from typing import Optional


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


class ErrorValidator:
    @staticmethod
    def validate_non_empty(value: str, field_name: str) -> str:
        value = value.strip()
        if not value:
            raise ValidationError(f"{field_name} cannot be empty.")
        return value

    @staticmethod
    def validate_float(value: str, field_name: str) -> Optional[float]:
        value = value.strip()
        if value == "":
            return None
        try:
            return float(value)
        except ValueError:
            raise ValidationError(f"{field_name} must be a number.")

    @staticmethod
    def validate_int(value: str, field_name: str) -> Optional[int]:
        value = value.strip()
        if value == "":
            return None
        try:
            return int(value)
        except ValueError:
            raise ValidationError(f"{field_name} must be an integer.")

    @staticmethod
    def validate_category(value: str) -> str:
        allowed = {"maintenance", "event", "emergency"}
        v = value.strip().lower()
        if v not in allowed:
            raise ValidationError(f"Category must be one of: {', '.join(allowed)}.")
        return v

    @staticmethod
    def validate_urgency(value: str) -> str:
        allowed = {"low", "medium", "high", "critical"}
        v = value.strip().lower()
        if v not in allowed:
            raise ValidationError(f"Urgency must be one of: {', '.join(allowed)}.")
        return v.capitalize()

