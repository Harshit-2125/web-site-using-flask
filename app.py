
from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Initialize the database
#db = SQLAlchemy(app)


# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the "Call us" button
@app.route('/call_us')
def call_us():
    # Redirecting back to the home page or provide a phone number
    return redirect(url_for('home'))
 
# Route for the Grow Shining page
@app.route('/grow_shining')
def grow_shining():
    return render_template('grow_shining.html')

# Route for the Illuminate page
@app.route('/illuminate')
def illuminate():
    return render_template('illuminate.html')


# Route for the "Contact" button
@app.route('/contact')
def contact():
    # Render the contact form page
    return render_template('contact.html')

# Route to handle contact form submission
@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Add your logic here (e.g., saving to a database or sending an email)
    # For now, it will redirect to a "thank you" page or back to the home page
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
