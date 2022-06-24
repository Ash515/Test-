from pydoc import render_doc
from flask import render_template,Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model import db, InfoModel
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5433/flask_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db.init_app(app)
migrate = Migrate(app, db)
 


 
if __name__ == '__main__':
    app.run(debug=True)