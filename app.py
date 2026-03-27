from flask import Flask
# from flask import SocketIO
from flask import render_template
from board import generate_board  

app = Flask(__name__)



@app.route('/')
def index():
    board = generate_board()
    return render_template('main.html', board=board)

if __name__ == '__main__':
    app.run(debug=True)
