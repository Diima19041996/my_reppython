import os.path

from flask import Flask, render_template
from flask import request
from flask import url_for
from flask import redirect


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


from settings import *

basedir = os.path.abspath((os.path.dirname(__file__)))
app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URL'] = (
    f'{DIALECT_BD}+pymysql://{USER_BD}:{PASSWORD_BD}@{HOST_BD}:{PORT_BD}/'
    f'{NAME_BD}?charset=utf-8'
)
app.config['SQLFAlchemy_TRAC_MODIFICATION'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primari_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.Syring(100), nullable=False)

    def __repr__(self):
        return f'Student {self.firstname} {self.lastname}'




@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(HOST, PORT, DEBUG)
