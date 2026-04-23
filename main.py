DATA_FILE = "data/service_requests.csv"
SEARCHABLE_FIELDS = {
    "1": "request_id",
    "2": "request_type",
    "3": "requester_name",
    "4": "location",
    "5": "status",
}

class ServiceRequestManager:
    def __init__(self, file_name: str):
        self.csv_service = CSVreader_service(file_name)
        self.requests = self.csv_service.read_file()

