Yellow Light District Calculator (YLDC) 📏
Overview
The Yellow Light District Calculator is a full-stack project that demonstrates real-time computer vision capabilities. The application uses a Python Flask backend with OpenCV to detect two yellow objects in a live video stream, calculates the Euclidean distance between them, and displays it dynamically. The frontend is a modern portfolio website built with React and Tailwind CSS, which consumes the live video feed.

This project showcases a complete development pipeline, from computer vision algorithm design and backend streaming to frontend integration and deployment.

Features ✨
Real-time Object Detection: Identifies two yellow objects in a live video stream.

Distance Calculation: Computes the real-time distance between the detected objects.

Live Video Streaming: Streams the processed video feed from a Flask backend to a React frontend.

Interactive Frontend: A single-page, responsive portfolio site built with React and Tailwind CSS.

3D Animated Background: An engaging 3D logo rendered with Three.js.

Live Demo (Local Setup) 💻
The live video component of this project requires the Python server to be run locally as a remote server cannot access your webcam.

Step 1: Clone the Repository
git clone [https://github.com/debuggingbyadhvik/YDLC](https://github.com/debuggingbyadhvik/YDLC)
cd YOLO

Step 2: Install Python Dependencies
It is highly recommended to use a virtual environment.

pip install Flask opencv-python numpy

Step 3: Run the Flask Server
Navigate to the directory containing app.py and run the server.

python3 app.py

This will start the server on http://127.0.0.1:5000.

Step 4: Open the Web App
Open the portfolio.html file in your web browser. The "YOLO Distance Calculator" section will automatically connect to your webcam feed.

Tech Stack 🛠️
Backend:

Python: 🐍 The core programming language.

Flask: A lightweight web framework for the video streaming server.

OpenCV: 📸 The primary library for computer vision and object detection.

Frontend:

React: ⚛️ A JavaScript library for building the user interface.

Tailwind CSS: 🎨 A utility-first CSS framework for rapid styling.

Three.js: A JavaScript library for the 3D animated background.