from flask import Flask, request, jsonify, send_from_directory, render_template
# existing imports..
import os
from werkzeug.utils import secure_filename
from document_converter import DocumentConverter

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Initialize your converter
converter = DocumentConverter(output_dir=OUTPUT_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_files():
    if 'files' not in request.files:
        return jsonify({'error': 'No files part in the request'}), 400

    files = request.files.getlist('files')
    if not files:
        return jsonify({'error': 'No files uploaded'}), 400

    results = []

    for file in files:
        filename = secure_filename(file.filename)
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(input_path)

        result = converter.convert_to_txt(input_path)
        if result.endswith(".txt"):
            results.append({
                'original_file': filename,
                'converted_file': result,
                'download_url': f"/download/{result}"
            })
        else:
            results.append({
                'original_file': filename,
                'error': result
            })

    return jsonify({'results': results})

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

