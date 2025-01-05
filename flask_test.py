from flask import Flask, render_template, request, redirect, url_for
import os

# Flask App erstellen
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Startseite
@app.route('/')
def index():
    return render_template('index.html')

# Route zum Hochladen von Dateien
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "Keine Datei hochgeladen!", 400

    file = request.files['file']
    if file.filename == '':
        return "Datei hat keinen Namen!", 400

    # Datei speichern
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    return redirect(url_for('uploaded_file', filename=file.filename))

# Route zur Anzeige der hochgeladenen Datei
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return render_template('uploaded.html', filename=filename)

# Server starten
if __name__ == '__main__':
    app.run(debug=True)