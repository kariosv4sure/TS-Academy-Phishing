from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Route to serve images if needed explicitly
@app.route('/images/<filename>')
def images(filename):
    return send_from_directory('images', filename)

# Main route
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

