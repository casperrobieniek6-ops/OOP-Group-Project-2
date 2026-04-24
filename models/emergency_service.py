"""Emergency request subclass."""
from models.request import Request


class EmergencyService(Request):
    """Represents urgent or hazardous service requests."""

    def __init__(self, request_id, requester_name, location, urgency_level, estimated_cost, status, hazard_level, response_time_minutes):
        super().__init__(request_id, requester_name, location, urgency_level, estimated_cost, status)
        self.hazard_level = int(hazard_level)
        self.response_time_minutes = int(response_time_minutes)

    def get_request_type(self):
        return "Emergency"

    def calculate_priority_score(self):
        score = super().calculate_priority_score() + (self.hazard_level * 10)
        if self.response_time_minutes <= 10:
            score += 10
        elif self.response_time_minutes <= 20:
            score += 5
        return score

    def type_specific_details(self):
        return f"Hazard Level: {self.hazard_level}; Response Time: {self.response_time_minutes} minutes"

    def get_recommendation(self):
        if self.hazard_level >= 5 or self.urgency_level >= 5:
            return "Dispatch emergency response immediately and alert public safety staff."
        if self.hazard_level >= 3:
            return "Send rapid response and keep the case open until risk is reduced."
        return "Investigate quickly and monitor for changes."

    def to_csv_row(self):
        row = super().to_csv_row()
        row["hazard_level"] = self.hazard_level
        row["response_time_minutes"] = self.response_time_minutes
        return row
