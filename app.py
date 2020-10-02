# Project terminal commands
"""
** General
-> pipenv install flask, pipenv shell, pipenv install Flask-SQLAlchemy 

** ORM-SQL 
1. To create DB -> sqlite3 database/<name_data_base>.db  
2. To validate DB name created -> .databases 
3. To create Table -> from app import db + db.create_all() -- Tip: Run the code before create class related to table
4. To validate Table name created -> .tables
5. To see data on table -> select * from table_name

"""

from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

# Give the name from the app root to flask, a passed it as variable value.
app = Flask(__name__)
# Basic config from ORM (object-relational-mapping) SQLAlchemy to connect to SQL DB, on this project SQLite3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/tasks.db'
# Basic config from ORM (object-relational-mapping) SQLAlchemy to turn down default flask event system that It spend resources and has some hard bugs inside to fix it.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# You
db = SQLAlchemy(app)

# Object modeling so you create a table as a class and defines each column as a key
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    done = db.Column(db.Boolean)

# Define the home URL
@app.route('/')
def home():
    # Asking for all data on table
    tasks = Task.query.all()
# Confid to connect with front
    return render_template('index.html', list_tasks=tasks)

# Define a new url that It has method to create data
@app.route('/create-task', methods=['POST'])
def create():
    # Give value to each column (key). So you each time input is submit, it will create a new column with content as the input written and done as false / task is a instance from object Task
    new_task = Task(content=request.form['content'], done=False)
    # Add the value save on the task variable to db Task
    db.session.add(new_task)
    # Save the change
    db.session.commit()
    # Return redirection to url home
    return redirect(url_for('home'))

@app.route('/done/<id>')
def done(id):
# Query to table Task and filter by id (automatic data created). At first match parameter from url with id from table. It save save the change on a variable.
    confirm_task =Task.query.filter_by(id=int(id)).first()
    confirm_task.done = not(confirm_task.done)
    db.session.commit()
    return redirect(url_for('home'))

# Define a new url that It has method to delete data, with an id parameter on url and function as a identifier
@app.route('/delete/<id>')
def delete(id):
# Query to table Task and filter by id (automatic data created). At first match parameter from url with id from table. It save the change on a variable. And then delete it from DB.
    delete_task = Task.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('home'))

# Define the module name as the root module app
if __name__ == "__main__":
    # Run the app with flask on your pc, port 5000 and also It will give you debugging advice on terminal.
    app.run(host='127.0.0.1', port=5000, debug=True)
