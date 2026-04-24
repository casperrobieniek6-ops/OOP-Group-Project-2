from services.CSVreader_service import CSVReaderService


def main():
     csv_reader = CSVReaderService("data/service_requests.csv")
     requests = csv_reader.get_requests()

     for request in requests:
         print(request)

if __name__ == '__main__':
    main()