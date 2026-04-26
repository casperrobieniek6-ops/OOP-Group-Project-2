class ErrorValidator:

    @staticmethod
    def clean_row(row):
        """Ensures all expected fields exist and converts invalid values safely."""

        cleaned = {}

        # Required fields
        cleaned["request_id"] = row.get("request_id", "").strip()
        cleaned["requester_name"] = row.get("requester_name", "").strip()
        cleaned["location"] = row.get("location", "").strip()
        cleaned["status"] = row.get("status", "Open").strip()

        # Numeric fields with safe conversion
        cleaned["urgency_level"] = ErrorValidator.safe_int(row.get("urgency_level"), default=1)
        cleaned["estimated_cost"] = ErrorValidator.safe_float(row.get("estimated_cost"), default=0.0)
        cleaned["days_open"] = ErrorValidator.safe_int(row.get("days_open"), default=0)
        cleaned["attendees"] = ErrorValidator.safe_int(row.get("attendees"), default=None)
        cleaned["hazard_level"] = ErrorValidator.safe_int(row.get("hazard_level"), default=None)
        cleaned["response_time_minutes"] = ErrorValidator.safe_int(row.get("response_time_minutes"), default=None)

        # Strings
        cleaned["issue_type"] = row.get("issue_type", "").strip()
        cleaned["event_date"] = row.get("event_date", "").strip()

        return cleaned

    @staticmethod
    def safe_int(value, default=0):
        try:
            if value in ("", None):
                return default
            return int(value)
        except ValueError:
            return default

    @staticmethod
    def safe_float(value, default=0.0):
        try:
            if value in ("", None):
                return default
            return float(value)
        except ValueError:
            return default
