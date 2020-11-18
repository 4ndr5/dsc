from flask import Flask, render_template
from wtform_fields import *
from models import *

# App configuartion
app = Flask(__name__)
app.secret_key = 'csrf.token'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI']='postgres://ztgdtarcblhscz:f75e1a6cd2bcfd802b30e756567c9e448190fa5dd1a51c2670a3d6919fc379ac@ec2-54-224-175-142.compute-1.amazonaws.com:5432/d8h1aim9ltuv4k' 

db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()

    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "Insterted into a db!"

    return render_template("index.html", form=reg_form)


if __name__ == "__main__":
    app.run(debug=True)