import csv
from data import *
#Class for CSV Reader
class CSVreader_service:

def __init__(self):
    self.table = []

    def read_file(self, file_name):
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            table = []
            for row in csv_reader:
                table.append(row)
    def add_data(self, data):
        self.table.append(data)