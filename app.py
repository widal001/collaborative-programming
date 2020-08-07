from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    # {'user': 'bd', 'message': ''}
    # {'user': 'jj', 'message': ''}
    messages = [
        {'user': 'bd', 'message': 'Hi'},
        {'user': 'bd', 'message': 'This is Billy'},
        {'user': 'jj', 'message': 'Hey how\'s it going?'},
        
    ]
    return render_template('index.html', messages=messages)
