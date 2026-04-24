import csv
from data import *
#Class for CSV Reader

class CSVReaderService:
    def __init__(self, filename):
        self.filename = filename

    def get_requests(self):
        requests_table = []

        with open(self.filename, mode= "r", newline="") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                requests_table.append(row)
        return requests_table