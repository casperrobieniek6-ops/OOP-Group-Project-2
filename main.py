from models.request import Request
from services.CSVreader_service import CSVReaderService

def row_to_request(row):
    return Request(
        row['request_id'],
        row['requester_name'],
        row['location'],
        row['urgency_level'],
        row['estimated_cost'],
        row['status'],
        row['issue_type'],
        row['days_open'],
        row['attendees'],
        row['event_date'],
        row['hazard_level'],
        row['response_time_minutes'])

def main():
     csv_reader = CSVReaderService("data/service_requests.csv")
     rows = csv_reader.get_requests()

     requests = []

     for row in rows:
         request = row_to_request(row)
         requests.append(request)

     for request in requests:
         print(request.display_request())

if __name__ == '__main__':
    main()