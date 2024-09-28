# Hotel-Management
Hotel Management System is a web-based application that allows the hotel manager to handle all hotel activities online
## Project Overview
The Hotel Management System is a Python-driven project designed to simplify hotel operations such as booking management, room availability, and staff coordination. With this system, managers can view and manage available rooms, handle guest reservations, and coordinate staff responsibilities. The system offers a flexible and interactive platform to cater to hotel managers’ day-to-day needs, ensuring smooth operation without the need for manual tracking.
Data is managed using an SQLite database for persistent and reliable storage, making the system lightweight and portable. A command-line interface (CLI) is used to manage the various functions in an easy-to-navigate manner, suitable for hotel managers who prefer a straightforward solution.

## Key Features
### Room Management:
* Add, edit, and delete room details.
* Track room availability and categorize rooms by type (e.g., single, double, suite).
* Mark rooms as available or occupied based on bookings.

### Booking Management:
* Manage customer bookings, including the ability to add, modify, or cancel reservations.
* Track customer details such as check-in/check-out dates, room type, and payment status.
* Automated room assignment based on availability.

### Service Management:
* Manage additional hotel services (e.g., room service, laundry, spa).
* Provide customers with service status updates and manage billing for services.

### Report Generation:
* Generate booking reports, summarizing room occupancy and revenue.
* Create customer reports, allowing better management oversight.
* Detailed financial summaries, showing income from bookings and services.

## Implementation Details
### Database Setup:
The project uses SQLite to store all data, ensuring a simple and portable solution.
The database includes several tables:
* rooms: Stores room details such as room type, availability, and price.
* bookings: Tracks customer reservations, including check-in/check-out dates and payment status.
* services: Stores available services and customer service requests

### Command-Line Interface:
The CLI allows hotel managers to interact with the system by performing operations such as:
* Adding rooms, bookings, staff, and services.
* Modifying or deleting records.
* Generating reports.
The CLI is designed to be interactive, prompting the user for inputs to complete operations.

### Data Operations:
* Functions to add, update, and delete records in the database ensure smooth data management.
* Search and filter functions allow managers to easily retrieve and view relevant data, such as available rooms or upcoming bookings.

### Reporting:
* The system generates reports from the database, summarizing room occupancy and revenue.
* Reports can be exported to text or displayed in the CLI for quick insights.

## Usage Instructions
### Setup:
* Ensure Python is installed on your system.
* No additional setup is required beyond Python's standard sqlite3 module.

### Running the Script:
* Run the main Python script from the command line to access the Hotel Management System.
* Use the interactive CLI to perform various operations.

### Example Commands:
Add a Room: Enter the room type, price, and availability status.
Add a Booking: Enter customer details, room type, and check-in/check-out dates.
Generate Reports: View room occupancy and financial summaries.
