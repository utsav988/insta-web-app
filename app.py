from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Upload configuration
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    media_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', media_files=media_files)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['media']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
    return redirect('/')

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(filepath):
        os.remove(filepath)
    return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect('/')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return redirect('/login')
    return render_template('signup.html')

if __name__ == '__main__':
    import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

