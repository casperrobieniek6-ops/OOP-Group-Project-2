import csv
from data import *
#Class for CSV Reader
class CSVreader_service:
    table = ['request_id', 'request_type', 'requester_name', 'location', 'urgency_level', 'estimated_cost', 'status',
             'issue_type', 'days_open', 'attendees', 'event_date', 'hazard_level', 'response_time_minutes']

    def __init__(self):
        pass
        def read_file(self, file_name):
            with open(file_name) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                table = []
                for row in csv_reader:
                    table.append(row)