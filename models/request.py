from services.CSVreader_service import
class Request:
    def __init__(self):
        self.table = []

    def add_data(self, data):
        self.table.append(data)