import csv
from typing import List, Optional

from models import (
    Request,
    MaintenanceRequest,
    EventRequest,
    EmergencyRequest,
)


class CSVReaderService:
    """
    Handles loading and saving service requests from/to CSV.
    """

    def __init__(self, filepath: str):
        self.filepath = filepath

    def load_requests(self) -> List[Request]:
        requests: List[Request] = []
        try:
            with open(self.filepath, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    req = self._row_to_request(row)
                    if req is not None:
                        requests.append(req)
        except FileNotFoundError:
            # No file yet → start with empty list
            pass
        return requests

    def save_requests(self, requests: List[Request]) -> None:
        fieldnames = [
            "request_id",
            "requester_name",
            "location",
            "category",
            "urgency_level",
            "estimated_cost",
            "status",
            "issue_type",
            "days_open",
            "expected_attendees",
            "event_date",
            "hazard_level",
            "response_time",
        ]
        with open(self.filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for r in requests:
                row = {
                    "request_id": r.request_id,
                    "requester_name": r.requester_name,
                    "location": r.location,
                    "category": r.category,
                    "urgency_level": r.urgency_level,
                    "estimated_cost": r.estimated_cost,
                    "status": r.status,
                    "issue_type": getattr(r, "issue_type", None),
                    "days_open": getattr(r, "days_open", None),
                    "expected_attendees": getattr(r, "expected_attendees", None),
                    "event_date": getattr(r, "event_date", None),
                    "hazard_level": getattr(r, "hazard_level", None),
                    "response_time": getattr(r, "response_time", None),
                }
                writer.writerow(row)

    def _row_to_request(self, row: dict) -> Optional[Request]:
        category = (row.get("category") or "").strip().lower()

        def to_float(v):
            return float(v) if v not in (None, "", " ") else None

        def to_int(v):
            return int(v) if v not in (None, "", " ") else None

        base_kwargs = dict(
            request_id=row.get("request_id", ""),
            requester_name=row.get("requester_name", ""),
            location=row.get("location", ""),
            urgency_level=row.get("urgency_level", "Low"),
            estimated_cost=to_float(row.get("estimated_cost")),
            status=row.get("status", "Open"),
        )

        if category == "maintenance":
            return MaintenanceRequest(
                **base_kwargs,
                issue_type=row.get("issue_type") or None,
                days_open=to_int(row.get("days_open")),
            )
        elif category == "event":
            return EventRequest(
                **base_kwargs,
                expected_attendees=to_int(row.get("expected_attendees")),
                event_date=row.get("event_date") or None,
            )
        elif category == "emergency":
            return EmergencyRequest(
                **base_kwargs,
                hazard_level=row.get("hazard_level") or None,
                response_time=to_float(row.get("response_time")),
            )
        else:
            # Fallback: plain Request if category unknown
            return Request(
                request_id=base_kwargs["request_id"],
                requester_name=base_kwargs["requester_name"],
                location=base_kwargs["location"],
                category=category or "unknown",
                urgency_level=base_kwargs["urgency_level"],
                estimated_cost=base_kwargs["estimated_cost"],
                status=base_kwargs["status"],
            )
