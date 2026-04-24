from models.request import Request
from services.CSVreader_service import CSVReaderService

def row_to_request(row):
    try:
        return Request(
            row.get('request_id', ''),
            row.get('requester_name', ''),
            row.get('location', ''),
            row.get('urgency_level', ''),
            float(row.get('estimated_cost', 0) or 0),
            row.get('status', ''),
            row.get('issue_type', ''),
            int(row.get('days_open', 0) or 0),
            int(row.get('attendees', 0) or 0),
            row.get('event_date', ''),
            row.get('hazard_level', ''),
            int(row.get('response_time_minutes', 0) or 0)
        )
    except ValueError:
        print(f"Invalid data found in row: {row}")
        return None


def display_all_requests(requests):
    print("\n--- ALL SERVICE REQUESTS ---")
    for request in requests:
        print(request.display_request())


def search_requests(requests):
    keyword = input("Enter keyword to search (name/location/status): ").lower()
    results = [
        r for r in requests
        if keyword in r.requester_name.lower()
        or keyword in r.location.lower()
        or keyword in r.status.lower()
    ]

    print("\n--- SEARCH RESULTS ---")
    if results:
        for r in results:
            print(r.display_request())
    else:
        print("No matching requests found.")


def add_request(requests):
    print("\n--- ADD NEW REQUEST ---")
    try:
        request = Request(
            input("Request ID: "),
            input("Requester Name: "),
            input("Location: "),
            input("Urgency Level: "),
            float(input("Estimated Cost: ")),
            input("Status: "),
            input("Issue Type: "),
            int(input("Days Open: ")),
            int(input("Attendees: ")),
            input("Event Date: "),
            input("Hazard Level: "),
            int(input("Response Time (minutes): "))
        )
        requests.append(request)
        print("Request added successfully.")
    except ValueError:
        print("Invalid input. Request not added.")


def main():
    csv_reader = CSVReaderService("data/service_requests.csv")
    rows = csv_reader.get_requests()

    requests = []

    for row in rows:
        request = row_to_request(row)
        if request:
            requests.append(request)

    while True:
        print("\n--- MUNICIPAL SERVICE SYSTEM ---")
        print("1. View All Requests")
        print("2. Search Requests")
        print("3. Add New Request")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            display_all_requests(requests)
        elif choice == "2":
            search_requests(requests)
        elif choice == "3":
            add_request(requests)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()
