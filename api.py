from flask import Flask, request, send_file
from roboflow import Roboflow
import os

app = Flask(__name__)

# Replace with your Roboflow API key
rf = Roboflow(api_key=os.environ.get("ROBOFLOW_API_KEY"))
project = rf.workspace().project("usbicon")
model = project.version(3).model

@app.route('/textoutput', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    
    if file:
        filename = "temp.jpg"
        file.save(filename)
        result = model.predict(filename, confidence=40, overlap=30).json()
        os.remove(filename)  # Remove the file after prediction
        return result

@app.route('/imageoutput', methods=['GET'])
def get_prediction_image():
    model.predict("temp.jpg", confidence=40, overlap=30).save("prediction.jpg")
    return send_file("prediction.jpg", mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
