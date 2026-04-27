from models.request import Request
from services.CSVreader_service import CSVReaderService

# 
# Function to display all requests
# Prints the header "All Service Requests"
# FOR each request within the list:
#     CALL request.display_request()
#     PRINT the returned formmatted string

def display_all_requests(requests):
    print("\n--- ALL SERVICE REQUESTS ---")
    for request in requests:
        print(request.display_request())

# Function to add single request
#     PRINT header "Add New Request"
#     TRY:
#         COLLECT all of the request fields from user input
#         CREATE a new request object using the input values
#         APPEND the new object to the list of requests
#         PRINT message of success
#    EXCEPT ValueError:
#         PRINT the error message for invalid number input
#
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

# Function to search requests by requester, location, status
#    PROMPT the user for a keyword
#    CONVERT the keyword to lowercase
#    FILTER requests based on if the keyword appears in:
#        - requester_name
#        - location
#        -status
#    IF matches are found:
#        PRINT each of the matching request
#    ELSE:
#        PRINT that there is "No matching requests found"
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


# Prints menu
#    CREATE CSVReaderService that creates a path to CSV file
#    LOAD all requests from the CSV into a list
#    
#    LOOP forever:
#        DISPLAY all menu options
#        GET user choice
#
#        If choice is 1
#            CALL display_all_requests
#        ELSE IF choice is 2
#            CALL search_requests
#        ELSE IF choice is 3
#            CALL add_request
#        ELSE IF choice is 4
#            PRINT the exit message
#            This breaks the loop
#        ELSE anything else inputted:
#            PRINT an invalid choice message
#

def main():
    csv_reader = CSVReaderService("data/service_requests.csv")
    requests = csv_reader.load_requests()


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
