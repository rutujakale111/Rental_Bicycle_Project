<h1>Bicycle Rental System</h1>

## Overview

The Bicycle Rental System is a web-based application built using Flask and MongoDB. It enables users to rent bicycles, track rental history, and manage bicycle availability efficiently. The system includes features for user registration, rental transactions, and contact form submissions.

#3 Features

**User Registration:** Users can register with their email and password.

**Rent a Bicycle:** Users can rent a bicycle and track their rental status.

**Return a Bicycle:** Users can return rented bicycles, and the system calculates rental costs based on hourly rates.

**Rental History:** Users can view their past rentals.

**Contact Us:** Users can send messages or inquiries via a contact form.

**Admin Management:** MongoDB stores all records for users, bicycles, rentals, and messages.

## Technologies Used

**Backend:** Flask (Python)

**Database:** MongoDB (via PyMongo)

**Frontend:** HTML, CSS

**Authentication:** Flask session management

## Installation & Setup

Python 3.x installed

MongoDB installed and running

Steps to Run the Project :
**1. Clone the repository:**
git clone https://github.com/rutujakale111
cd Rental_Bicycle_Project
**2. Install dependencies:**
Install dependencies:
pip install -r requirements.txt
**3.Set up the database:**

Start MongoDB.

The system will automatically create collections (users, bicycles, rentals, messages).

Optionally, run the provided script to insert sample bicycle data.
##Run the Flask application:
**python app.py**
**4.Access the application:**

Open <b>http://127.0.0.1:5000/</b> in your web browser.
## Project Structure
/ bicycle-rental-system
|-- static/
|   |-- css/
|   |   |-- styles.css
|-- templates/
|   |-- index.html
|   |-- about.html
|   |-- contact.html
|   |-- register.html
|-- app.py
|-- config.py
|-- database.py
|-- requirements.txt
|-- README.md
## Usage

Home Page: Displays available bicycles for rent.

Register Page: Allows users to create an account.

Rent Page: Users can rent bicycles.

Return Bicycle: Users can return bicycles and calculate rental fees.

History Page: Displays a record of past rentals.

Contact Us: Users can submit inquiries.
