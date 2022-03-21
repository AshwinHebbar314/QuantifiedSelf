import os
from flask import Flask, render_template, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from application.database import db 
from flask_login import LoginManager, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'sicrit'
db = SQLAlchemy(app)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

app.app_context().push()


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


from application.methods import * 
@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')




if __name__ == '__main__':
  app.debug = True
  app.run()