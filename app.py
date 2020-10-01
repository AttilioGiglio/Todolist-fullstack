from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/tasks.db'

db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

# @app.route('/users', methods=['POST'])
# def create_user():
#     print(request.json)
#     return 'success'

# @app.route('/users', methods=['GET'])
# def get_user():
#     return 'success'

# @app.route('/users/<id>', methods=['DELETE'])
# def delete_user():
#     return 'success'

# @app.route('/users/<id>', methods=['PUT'])
# def update_user():
#     return 'success'