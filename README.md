# DressCodeAI

DressCodeAI is an AI-powered web application for intelligent video and image analysis using YOLO object detection. Built with Flask, it provides a user-friendly interface for real-time detection and analysis.

## Features

- Real-time video detection using YOLO
- User authentication (login/signup)
- Responsive web interface
- About and Contact pages

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/DressCodeAI.git
   cd DressCodeAI
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Download YOLO weights:**
   Place your YOLO weights file (e.g., `best.pt`) in the project root.

5. **Run the Flask app:**
   ```sh
   python flaskapp.py
   ```

6. **Open in browser:**
   Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to use the app.

## Project Structure

```
DressCodeAI/
├── flaskapp.py
├── YOLO_Video.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── login.html
│   ├── signup.html
│   └── detect.html
└── static/
    └── assets/
        ├── css/
        ├── js/
        └── img/
```

## License

This project is licensed under the MIT License.

## Credits

- [Flask](https://flask.palletsprojects.com/)
-
### Best FYP Award In FYP EXPO 2023
![fyp](https://github.com/UsamaMalik93/Dress_Code_inspection_System/assets/136118359/40b67527-e79f-4070-9604-b4d7271c9b22)


