# Virtual Environment Activation
"""
(In the command prompt)
- pip install virtualenv
- virtualenv env
- env/Scripts/activate.bat (in windows) | source env/bin/activate (in mac/linux)
- pip install flask flask-sqlalchemy
"""

# Application => https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#create-the-tables
from flask import Flask, render_template, url_for
app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emobiexpress.db' # Sqlite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@localhost/flask_app_db' # Mysql


# Databases 
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# Constants
import enum
from sqlalchemy import Enum
class status(enum.Enum):
    Opened = 1
    Onprocess = 2
    Closed = 3

# Models => https://overiq.com/flask-101/database-modelling-in-flask/#google_vignette
from datetime import datetime
class database(db.Model):
    OrderID = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String(255), nullable=False)
    Contact = db.Column(db.String(10), nullable=False)
    OrderDetails = db.Column(db.Text(), nullable=False)
    Status = db.Column(Enum(status))
    CreatedAt = db.Column(db.DateTime(), default=datetime.utcnow) # onupdate=datetime.utcnow

    def __repr__(self):
        return "ID: %r" % self.id
    
# Intialize the database
with app.app_context():
    db.create_all()

"""
Extra Steps: To reintialize the database while working on websites
After the completion of Models, Please try the above steps to create a database
Note: Make sure the environment variable is activated!
- python (in command prompt)
- from main import app, db
- app.app_context().push()
- db.create_all()
- exit()
"""


# Routes
@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template("index.html")

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')



# Driver Code
if __name__ == "__main__":
    app.run(debug=True, port=8080)
