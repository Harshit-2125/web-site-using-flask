from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Initialize the database
#db = SQLAlchemy(app)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for API jobs (example for fetching data)
#@app.route("/api/jobs")
#def get_jobs():

# Main entry point to run the app
if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
