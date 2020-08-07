from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    # {'user': 'bd', 'message': ''}
    # {'user': 'jj', 'message': ''}
    messages = [
    ]
    return render_template('index.html', messages=messages)
