from flask import Flask, render_template, request, redirect, url_for, flash, session
from config import users_collection, bicycles_collection, rentals_collection, messages_collection
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # For session management

# Home Page
@app.route('/')
def index():
    bikes = list(bicycles_collection.find({"status": "available"}))
    return render_template('index.html', bikes=bikes)

# About Us Page
@app.route('/about')
def about():
    return render_template('about.html') 

# Contact Us Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Store message in database
        messages_collection.insert_one({"name": name, "email": email, "message": message, "date": datetime.now()})
        
        flash("Your message has been sent successfully!", "success")
        return redirect(url_for('contact'))

    return render_template('contact.html')

# User Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])  # Hash password

        # Check if user already exists
        if users_collection.find_one({"email": email}):
            flash("Email already registered. Please login!", "error")
            return redirect(url_for('register'))

        # Save user in MongoDB
        users_collection.insert_one({"name": name, "email": email, "password": password})
        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for('index'))

    return render_template('register.html')

# Rent a Bicycle
@app.route('/rent', methods=['POST'])
def rent_bicycle():
    bike_id = int(request.form['bike_id'])
    user_email = request.form['email']

    # Update bike status
    bicycles_collection.update_one({"bike_id": bike_id}, {"$set": {"status": "rented"}})

    # Store rental info
    rentals_collection.insert_one({
        "bike_id": bike_id,
        "user_email": user_email,
        "rent_time": datetime.now(),
        "status": "ongoing"
    })

    flash("Bicycle rented successfully!", "success")
    return redirect(url_for('index'))

# Return a Bicycle
@app.route('/return/<int:bike_id>', methods=['POST'])
def return_bicycle(bike_id):
    rental = rentals_collection.find_one({"bike_id": bike_id, "status": "ongoing"})

    if rental:
        rent_time = rental['rent_time']
        return_time = datetime.now()
        duration = (return_time - rent_time).seconds // 3600  # Hours
        hourly_rate = bicycles_collection.find_one({"bike_id": bike_id})['hourly_rate']
        total_cost = max(duration, 1) * hourly_rate  # At least 1 hour charge

        # Update records
        rentals_collection.update_one({"bike_id": bike_id}, {"$set": {"status": "returned", "return_time": return_time, "cost": total_cost}})
        bicycles_collection.update_one({"bike_id": bike_id}, {"$set": {"status": "available"}})

        return {"message": "Bicycle returned!", "cost": total_cost}

    return {"message": "No ongoing rental found!"}

# Rental History
@app.route('/history')
def history():
    rental_history = list(rentals_collection.find())
    return render_template('history.html', rentals=rental_history)

if __name__ == '__main__':
    app.run(debug=True)
