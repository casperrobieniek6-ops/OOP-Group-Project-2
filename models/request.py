from services.CSVreader_service import CSVReaderService
class Request:
    def __init__(self, request_id, requester_name, location, urgency_level, estimated_cost, status, issue_type, days_open, attendees, event_date, hazard_level, response_time_minutes):
        self.request_id = request_id
        self.requester_name = requester_name
        self.location = location
        self.urgency_level = urgency_level
        self.estimated_cost = estimated_cost
        self.status = status
        self.issue_type = issue_type
        self.days_open = days_open
        self.attendees = attendees
        self.event_date = event_date
        self.hazard_level = hazard_level
        self.response_time_minutes = response_time_minutes

    def display_request(self):
        return {
            f"ID: {self.request_id} | "
            f"Requester: {self.requester_name} | "
            f"Location: {self.location} | "
            f"Urgency: {self.urgency_level} | "
            f"Cost: {self.estimated_cost} | "
            f"Status: {self.status}"
        }