from flask import Flask, Response, render_template

# FIXED: Response and render_template were added to the import list

app = Flask(__name__)

# --- Flask Video Streaming (Not functional on PythonAnywhere) ---

# Note: This entire section will NOT work on PythonAnywhere
# because a remote server cannot access your webcam.
# The code is included for completeness, but it will only
# serve the "Camera Not Found" error message.
#
# Your project's live video feature will need to be demonstrated locally.

def generate_frames():
    # Placeholder for the video streaming logic
    import cv2
    import numpy as np

    error_img = np.zeros((480, 640, 3), dtype=np.uint8)
    cv2.putText(error_img, "Camera Not Found on Server", (150, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    ret, buffer = cv2.imencode('.jpg', error_img)
    frame_bytes = buffer.tobytes()
    
    while True:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# --- Main Flask Route ---

@app.route('/')
def index():
    """Serves the main portfolio HTML file."""
    # This will look for portfolio.html inside a 'templates' folder.
    return render_template('portfolio.html')

if __name__ == "__main__":
    app.run()
