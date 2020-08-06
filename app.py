from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    messages = [
        {'user': 'bd', 'message': 'HEYO!!! WOOT!'},
        {'user': 'jj', 'message': 'Looks good!'},
        {'user': 'bd', 'message': 'Sooo slow'}
    ]
    return render_template('index.html', messages=messages)
