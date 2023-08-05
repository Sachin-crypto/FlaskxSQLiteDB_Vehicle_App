from flask import Flask, render_template, request, redirect, url_for
from database import db


# Creating Flask App
app = Flask(__name__)
# Database Name
db_name = 'vehicle.db'

# Configuring SQLite Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

# To suppress warnings while making modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialising SQLAlchemy with Flask App
db.init_app(app)

""" Creating Database with App Context"""
def create_db():
    with app.app_context():
        db.create_all()

""" Creating Routes """
@app.route("/")
def home():
    details = Vehicle.query.all()
    return render_template("home.html", details=details)

@app.route("/add-vehicle", methods=['GET', 'POST'])
def add_vehicle():
    if request.method == 'POST':
        v_name = request.form.get('vehicle')
        price = request.form.get('price')

        add_detail = Vehicle(
            name=v_name,
            price=price
        )
        db.session.add(add_detail)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("vehicle.html")

if __name__ == "__main__":
    from models import Vehicle
    create_db()
    app.run(debug=True)