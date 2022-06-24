from flask import Flask,render_template,request
from flask_migrate import Migrate
from model import db, InfoModel
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5433/flask_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)
 
@app.route('/')
def form():
    return render_template('login.html')
 
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        new_user = InfoModel(name=name, age=age)
        db.session.add(new_user)
        db.session.commit()
        return f"Done!!"
 
 
if __name__ == '__main__':
    app.run(debug=True)