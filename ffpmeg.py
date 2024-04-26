from flask import Flask, send_from_directory, request
import os

app = Flask(__name__)

# Directory where the HLS files are stored
MEDIA_FOLDER = 'video'

@app.route('/video/<path:filename>')
def stream(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
