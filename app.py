from flask import Flask, render_template, request, jsonify
from errors import check_errors

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    code = request.form['code']
    errors = check_errors(code)
    return jsonify(errors)

if __name__ == '__main__':
    app.run(debug=True)