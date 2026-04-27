#Initialize all attributes of a service request

class Request:
    # 
    #    Initialize a Request object with all possible fields
    #    Possible some fields may be unused depending on request type.
    #
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
#Converts urgency and hazard for comparison
    def get_recommendation(self):
        urgency = str(self.urgency_level).lower()
        hazard = str(self.hazard_level).lower()
#If urgency is high, returns immediate action message
#Else if request has been open over 10 days, sends follow up notifying request open too long.
#Else if status is open, returns assignment message
#Otherwise, returns no action needed.
        if urgency == "high" or hazard == "high":
            return "Immediate attention required."
        elif self.days_open and int(self.days_open) > 10:
            return "Follow up soon because this request has been open too long."
        elif self.status.lower() == "open":
            return "Review and assign to the correct department."
        else:
            return "No immediate action needed."

    # Displays all attributes of a request
    # Return a formatted string containing:
    #    - all request attributes
    #    - recommendation from get_recommendation()
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
        
    #    
    # CREATE a dictionary
    # MAP each of its attributes to its CSV column name
    # RETURN the dictionary
    #
    
    def to_csv_row(self):
        return {
            "request_id": self.request_id,
            "requester_name": self.requester_name,
            "location": self.location,
            "urgency_level": self.urgency_level,
            "estimated_cost": self.estimated_cost,
            "status": self.status,
            "issue_type": self.issue_type,
            "days_open": self.days_open,
            "attendees": self.attendees,
            "event_date": self.event_date,
            "hazard_level": self.hazard_level,
            "response_time_minutes": self.response_time_minutes
        }
