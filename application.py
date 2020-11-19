from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from flask_socketio import SocketIO, send, emit
from wtform_fields import *
from models import *


# App configuartion
app = Flask(__name__)
app.secret_key = 'csrf.token'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI']='postgres://ztgdtarcblhscz:f75e1a6cd2bcfd802b30e756567c9e448190fa5dd1a51c2670a3d6919fc379ac@ec2-54-224-175-142.compute-1.amazonaws.com:5432/d8h1aim9ltuv4k' 

db = SQLAlchemy(app)
#Initialize Flask Socketio
socketio= SocketIO(app)

# Flask login configuration
login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id_):

    return User.query.get(int(id_))

@app.route("/", methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()
    #Update db if validation succeed
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        #hash pwrd
        hash_pwrd = pbkdf2_sha256.hash(password)

        #Add user to db
        user = User(username=username, password=hash_pwrd)
        db.session.add(user)
        db.session.commit()

        flash('Registration succesful, please log in.', 'success')

        return redirect(url_for("login"))

    return render_template("index.html", form=reg_form)

@app.route("/login", methods=["GET", "POST"])
def login():

    login_form = LoginForm()

    #allow login if validation succeed
    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username=login_form.username.data).first()
        
        login_user(user_object)
        return redirect(url_for('chat'))
    
    return render_template("login.html", form=login_form)

# Prevent non-logged-in users from chat access
@app.route("/chat", methods=['GET', 'POST'])
def chat():

    #if not current_user.is_authenticated:
     #   flash('Please log in.', 'danger')
      #  return redirect(url_for('login'))

    return render_template('chat.html')

# Logout
@app.route("/logout", methods=['GET'])
def logout():

    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))

@socketio.on('message')
def message(data):

    #print(f"\n\n{data}\n\n")
    send(data)
    #emit("event", 'this is a custom event message')

# Run debug
if __name__ == "__main__":
    socketio.run(app, debug=True)