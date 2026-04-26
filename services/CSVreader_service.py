import csv
from models.request import Request
from models.event_service import EventService
from models.emergency_service import EmergencyService
from models.maintenence_service import MaintenanceService 
from services.error_validator import ErrorValidator

class CSVReaderService:
    """Handles reading and writing request data from/to CSV."""

    def __init__(self, file_path):
        self.file_path = file_path


    # LOAD ALL REQUESTS

    def load_requests(self):
        requests = []

        try:
            with open(self.file_path, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    cleaned = ErrorValidator.clean_row(row)
                    req_obj = self._create_request_object(cleaned)
                    requests.append(req_obj)

        except FileNotFoundError:
            print(f"ERROR: CSV file not found at {self.file_path}")

        return requests


    # CREATE CORRECT SUBCLASS

    def _create_request_object(self, row):
        """Determines which subclass to instantiate based on available fields."""

        # Emergency request
        if row.get("hazard_level") not in ("", None):
            return EmergencyService(
                row["request_id"],
                row["requester_name"],
                row["location"],
                int(row["urgency_level"]),
                float(row["estimated_cost"]),
                row["status"],
                int(row["hazard_level"]),
                int(row["response_time_minutes"])
            )

        # Event support request
        if row.get("attendees") not in ("", None):
            return EventService(
                row["request_id"],
                row["requester_name"],
                row["location"],
                int(row["urgency_level"]),
                float(row["estimated_cost"]),
                row["status"],
                int(row["attendees"]),
                row["event_date"]
            )

        # Maintenance request (if you have this class)
        if row.get("issue_type") not in ("", None):
            return MaintenanceService(
                row["request_id"],
                row["requester_name"],
                row["location"],
                int(row["urgency_level"]),
                float(row["estimated_cost"]),
                row["status"],
                row["issue_type"],
                int(row["days_open"])
            )

        # Default fallback
        return Request(**row)

    # -----------------------------
    # SAVE ALL REQUESTS BACK TO CSV
    # -----------------------------
    def save_requests(self, requests):
        if not requests:
            print("No requests to save.")
            return

        # Collect all possible CSV headers
        headers = [
            "request_id", "requester_name", "location", "urgency_level",
            "estimated_cost", "status", "issue_type", "days_open",
            "attendees", "event_date", "hazard_level", "response_time_minutes"
        ]

        with open(self.file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()

            for req in requests:
                writer.writerow(req.to_csv_row())
