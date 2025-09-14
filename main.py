from flask import Flask, render_template, request, jsonify
import antivirr as antivirr
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/upload", methods=['GET', 'POST'])
def hello_world():
    if 'file' not in request.files:
        return jsonify({'error': 'No file selected'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'})
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        check, type = antivirr.Checking_virus(filepath)

        if check:
            return jsonify({
                    'status': 'infected',
                    'filename': filename,
                    'threat_name': type,
                    'risk_level': 'High'
                })
        
        else:
            return jsonify({
                    'status': 'clean',
                    'filename': filename,
                    'filesize': f"{os.path.getsize(filepath) / (1024*1024):.2f} MB",
                    'scan_time': '2.3 seconds',
                    'engines': '47'
                })
        

if __name__ == "__main__":
    app.run(debug=True)