from models.request import Request
from services.CSVreader_service import CSVReaderService

#Function to display all requests
def display_all_requests(requests):
    print("\n--- ALL SERVICE REQUESTS ---")
    for request in requests:
        print(request.display_request())

#Function to add single request
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

#Function to search requests by requester, location, status
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
        for request in results:
            print(request.display_request())
    else:
        print("No matching requests found.")



def main():
    csv_reader = CSVReaderService("data/service_requests.csv")
    requests = csv_reader.load_requests()

#Prints menu
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
