"""Maintenance request subclass."""
from models.request import Request


class MaintenanceService(Request):
    """Represents routine maintenance needs like potholes and water leaks."""

    def __init__(self, request_id, requester_name, location, urgency_level, estimated_cost, status, issue_type, days_open):
        super().__init__(request_id, requester_name, location, urgency_level, estimated_cost, status)
        self.issue_type = str(issue_type).strip()
        self.days_open = int(days_open)

    def get_request_type(self):
        return "Maintenance"

    def calculate_priority_score(self):
        score = super().calculate_priority_score()
        if self.days_open >= 14:
            score += 15
        elif self.days_open >= 7:
            score += 8
        if self.issue_type.lower() in {"water leak", "sidewalk damage", "pothole"}:
            score += 5
        return score

    def type_specific_details(self):
        return f"Issue Type: {self.issue_type}; Days Open: {self.days_open}"

    def get_recommendation(self):
        if self.urgency_level >= 5 or self.days_open >= 14:
            return "Send a maintenance crew as soon as possible."
        if self.days_open >= 7:
            return "Schedule maintenance this week and check for safety concerns."
        return "Place in the regular maintenance schedule."

    def to_csv_row(self):
        row = super().to_csv_row()
        row["issue_type"] = self.issue_type
        row["days_open"] = self.days_open
        return row
