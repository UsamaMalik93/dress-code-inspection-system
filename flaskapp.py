from flask import Flask, render_template, Response, session, request
from werkzeug.security import generate_password_hash, check_password_hash
from YOLO_Video import video_detection
import cv2
import os
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Usama'

# Simple user database (in production, use a real database)
users = {
    'usamamalik2033@gmail.com': {
        'password_hash': generate_password_hash('admin'),
        'name': 'Usama Malik'
    }
}

# Password hashing functions
def hash_password(password):
    """Hash a password for storing"""
    return generate_password_hash(password)

def verify_password(stored_password_hash, provided_password):
    """Verify a stored password against one provided by user"""
    return check_password_hash(stored_password_hash, provided_password)

# Main Yolo Detection function
def generate_frames_web(path_x):
    yolo_output = video_detection(path_x)
    for detection_ in yolo_output:
        ref,buffer=cv2.imencode('.jpg',detection_)

        frame=buffer.tobytes()
        yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame +b'\r\n')
# Function Ended

# Defining Routes
@app.route("/") #default home route
@app.route("/home")
def home():
    session.clear()
    return render_template('index.html')

@app.route("/detect", methods=['GET','POST'])
def detect():
    if 'email' in session:
        return render_template('detect.html')
    else:
        return render_template('login.html')

@app.route('/webapp')
def webapp():
    session.clear()
    return Response(generate_frames_web(path_x=0), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/contact')
def contact():
    session.clear()
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginn', methods=['POST'])
def loginn():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        # Check if user exists and verify password
        if email in users and verify_password(users[email]['password_hash'], password):
            session['email'] = email
            session['user_name'] = users[email]['name']
            return render_template('detect.html', email=email, user_name=users[email]['name'])
        else:
            msg = "Invalid email or password"
            return render_template('login.html', msg=msg)

@app.route("/logout")
def logout():
    session.pop('email', None)
    session.pop('user_name', None)
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form.get('name', 'User')
        
        # Check if user already exists
        if email in users:
            msg = "User already exists with this email"
            return render_template('signup.html', msg=msg)
        
        # Add new user with hashed password
        users[email] = {
            'password_hash': hash_password(password),
            'name': name
        }
        
        msg = "Registration successful! Please login."
        return render_template('login.html', msg=msg)
    
    session.clear()
    return render_template('signup.html')

@app.route('/about')
def about():
    session.clear()
    return render_template('about.html')

# Utility route to add users (for testing - remove in production)
@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form.get('name', 'User')
        
        users[email] = {
            'password_hash': hash_password(password),
            'name': name
        }
        
        return f"User {email} added successfully!"
    
    return "Use POST method"

if __name__ == "__main__":
    app.run(debug=True)
