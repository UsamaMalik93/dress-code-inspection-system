from flask import Flask, render_template, Response, session, send_from_directory, request
from YOLO_Video import video_detection
import cv2
import os
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Usama'

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
        if (email=='usamamalik2033@gmail.com' and password=='admin'):
            session['email'] = email
            return render_template('detect.html', email=email)
        else:
            msg = "wrong email, password"
            return  render_template('login.html', msg = msg)

@app.route("/logout")
def logout():
    session.pop('email', None)
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    session.clear()
    return render_template('signup.html')

@app.route('/about')
def about():
    session.clear()
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
