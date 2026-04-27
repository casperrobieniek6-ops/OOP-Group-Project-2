"""Emergency request subclass."""
from models.request import Request

#
# CLASS: EmergencyService
#    Represents urgent or dangerous service requests that require
#    faster response and higher priority.
#
#    DEFINE EmergencyService as subclass of Request
#    STORE the hazard level and response time
#    PROVIDE methods to
#        - identify the request type
#        - calculate the priority score
#        - return the type specific details
#        - generate emergency-specific recommendations
#        - convert the object to a CSV row
#


class EmergencyService(Request):
    """Represents urgent or hazardous service requests."""
    #
    #    Initialize EmergencyService object
    #    CALL parent constructor to set shared fields
    #    CONVERT hazard_level to an INT
    #    CONVERT response_time_minutes to INT
    #

    def __init__(self, request_id, requester_name, location, urgency_level, estimated_cost, status, hazard_level, response_time_minutes):
        super().__init__(request_id, requester_name, location, urgency_level, estimated_cost, status)
        self.hazard_level = int(hazard_level)
        self.response_time_minutes = int(response_time_minutes)

    #
    #    RETURN the string "Emergency"
    #    Used by the system to identify request category
    #

    def get_request_type(self):
        return "Emergency"

    #
    #    START with base priority score from the REQUEST class
    #    ADD (hazard_level * 10) to score
    #    
    #    IF response_time_minutes less than/equal to 10
    #        ADD 10
    #    ELSE IF response_time_minutes less than/equal to 20
    #        ADD 5
    #
    #    RETURN final score
    #

    def calculate_priority_score(self):
        score = super().calculate_priority_score() + (self.hazard_level * 10)
        if self.response_time_minutes <= 10:
            score += 10
        elif self.response_time_minutes <= 20:
            score += 5
        return score
    #
    #    RETURN a formatted string containing
    #        - hazard level
    #        - response time in radius
    #

    def type_specific_details(self):
        return f"Hazard Level: {self.hazard_level}; Response Time: {self.response_time_minutes} minutes"

    #
    #    IF hazard_level is (greater than)/equal to 5 OR urgency_level (greater than)/equal to 5
    #        RETURN message "Dispatch emergency response immediately"
    #
    #    ELSE IF hazard_level is (greater than)/equal 3
    #        RETURN message "Send rapid response and keep case open"
    #
    #    ELSE:
    #        RETURN message "Investigate quickly and monitor"
    #

    def get_recommendation(self):
        if self.hazard_level >= 5 or self.urgency_level >= 5:
            return "Dispatch emergency response immediately and alert public safety staff."
        if self.hazard_level >= 3:
            return "Send rapid response and keep the case open until risk is reduced."
        return "Investigate quickly and monitor for changes."

    #
    #    CALL parent to_csv_row() to get base dictionary
    #    ADD hazard_level to dictionary
    #    ADD response_time_minutes to dictionary
    #    RETURN updated dictionary
    #
    def to_csv_row(self):
        row = super().to_csv_row()
        row["hazard_level"] = self.hazard_level
        row["response_time_minutes"] = self.response_time_minutes
        return row
