from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello!'

@app.route('/drinks')
def get_drinks():
    with app.app_context():
        # Use the database within the app context
        # ...
        return {"drinks": "drink data"}

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

if __name__ == '__main__':
    app.run(debug=True)
