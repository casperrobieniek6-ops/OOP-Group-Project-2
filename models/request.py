class Request:
    def __init__(self, request_id, requester_name, location, urgency_level,
                 estimated_cost, status, issue_type="", days_open=0,
                 attendees=0, event_date="", hazard_level="",
                 response_time_minutes=0):
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

    def get_recommendation(self):
        urgency = str(self.urgency_level).lower()
        hazard = str(self.hazard_level).lower()

        if urgency == "high" or hazard == "high":
            return "Immediate attention required."
        elif self.days_open and int(self.days_open) > 10:
            return "Follow up soon because this request has been open too long."
        elif self.status.lower() == "open":
            return "Review and assign to the correct department."
        else:
            return "No immediate action needed."

    def display_request(self):
        return (
            f"ID: {self.request_id} | "
            f"Requester: {self.requester_name} | "
            f"Location: {self.location} | "
            f"Urgency: {self.urgency_level} | "
            f"Cost: ${self.estimated_cost} | "
            f"Status: {self.status} | "
            f"Issue Type: {self.issue_type} | "
            f"Days Open: {self.days_open} | "
            f"Attendees: {self.attendees} | "
            f"Event Date: {self.event_date} | "
            f"Hazard Level: {self.hazard_level} | "
            f"Response Time: {self.response_time_minutes} minutes | "
            f"Recommendation: {self.get_recommendation()}"
        )
