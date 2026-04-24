"""Event support request subclass."""
from datetime import datetime
from models.request import Request


class EventService(Request):
    """Represents requests for town support at community events."""

    def __init__(self, request_id, requester_name, location, urgency_level, estimated_cost, status, attendees, event_date):
        super().__init__(request_id, requester_name, location, urgency_level, estimated_cost, status)
        self.attendees = int(attendees)
        self.event_date = str(event_date).strip()

    def get_request_type(self):
        return "EventSupport"

    def calculate_priority_score(self):
        score = super().calculate_priority_score()
        if self.attendees >= 500:
            score += 15
        elif self.attendees >= 250:
            score += 8
        return score

    def type_specific_details(self):
        return f"Expected Attendees: {self.attendees}; Event Date: {self.event_date}"

    def get_recommendation(self):
        try:
            event = datetime.strptime(self.event_date, "%Y-%m-%d").date()
            today = datetime.today().date()
            days_until_event = (event - today).days
        except ValueError:
            days_until_event = None

        if self.attendees >= 500:
            return "Coordinate staffing, permits, traffic control, and safety planning."
        if days_until_event is not None and days_until_event <= 14:
            return "Confirm event support soon because the event date is approaching."
        return "Review needed equipment, staffing, and event logistics."

    def to_csv_row(self):
        row = super().to_csv_row()
        row["attendees"] = self.attendees
        row["event_date"] = self.event_date
        return row
