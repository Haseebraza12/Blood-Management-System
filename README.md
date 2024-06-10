Blood Management System
Table of Contents
Problem Definition
Methodology
Toolkit
Test Cases
Installation
Usage
Contributing
License
Problem Definition
The management and distribution of blood and its products are critical for healthcare systems worldwide. However, inefficiencies and lack of coordination among blood banks, hospitals, NGOs, and donors often result in shortages or wastage of blood. Our Blood Management System aims to streamline the process of blood donation and distribution through a web-based application.

Objectives:
Simplify the process of blood donation and requisition.
Ensure the availability of blood for patients in need.
Facilitate coordination between donors, hospitals, and NGOs.
Provide a transparent system for tracking blood donations and requests.
Methodology
Our Blood Management System is designed with the following components and features:

User Roles:
Admin: Oversees the entire system, manages users, and maintains records.
Patient: Can request blood and view the status of their requests.
NGO: Can refer patients and manage donor drives.
Hospital: Can refer patients and manage blood inventory.
Donor: Can register to donate blood and view donation history.
Process Flow:
Registration: Users register as patients, donors, hospitals, or NGOs.
Login: Users log in using their credentials.
Request Blood: Patients can request blood directly or through hospital/NGO references.
Donation Management: Donors can register their donations, and hospitals/NGOs can manage donor drives.
Inventory Management: Hospitals manage their blood inventory and update the system accordingly.
Notification System: Users receive notifications regarding blood requests, donations, and inventory status.
Toolkit
The application is built using the following tools and technologies:

Framework: Django (Python)
Database: SQLite3 (default for Django)
Frontend: HTML, CSS, JavaScript
Libraries/Packages:
Django Rest Framework (for API endpoints)
Bootstrap (for responsive design)
jQuery (for enhanced frontend interactions)
Test Cases
To ensure the functionality and reliability of the system, the following test cases were defined and executed:

User Registration:

Test successful registration for each user role (Admin, Patient, NGO, Hospital, Donor).
Test registration with missing/invalid data.
User Login:

Test successful login for each user role.
Test login with incorrect credentials.
Blood Request:

Test creating a blood request by a patient.
Test creating a blood request through hospital/NGO reference.
Test viewing the status of a blood request.
Blood Donation:

Test donor registration for blood donation.
Test updating donor's donation history.
Inventory Management:

Test hospital's ability to update blood inventory.
Test notification system for low inventory levels.
Notification System:

Test sending notifications for blood requests.
Test sending notifications for donation drives and low inventory.
Installation
To run this project locally, follow these steps:

Clone the repository:

Copy code
git clone https://github.com/Haseebraza12/blood-management-system.git
cd blood-management-system
Create a virtual environment:

Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
Usage
After setting up the project, open a web browser and go to http://127.0.0.1:8000/ to access the application. Users can register and log in according to their roles and perform the necessary actions as described in the methodology section.

Contributing
We welcome contributions from the community. If you wish to contribute, please follow these steps:

License
This project is licensed under the MIT License. See the LICENSE file for more details.

