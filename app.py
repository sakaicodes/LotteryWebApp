# IMPORTS
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# CONFIG
app = Flask(__name__)
app.config['SECRET_KEY'] = 'LongAndRandomSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lottery.db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialise database
db = SQLAlchemy(app)


# HOME PAGE VIEW
@app.route('/')
def index():
    return render_template('main/index.html')


@app.errorhandler(400)
def bad_request(error):
    return render_template('400.html')


@app.errorhandler(403)
def bad_request(error):
    return render_template('403.html')


@app.errorhandler(404)
def bad_request(error):
    return render_template('404.html')


@app.errorhandler(500)
def bad_request(error):
    return render_template('500.html')


@app.errorhandler(503)
def bad_request(error):
    return render_template('503.html')


# BLUEPRINTS
# import blueprints
from users.views import users_blueprint
from admin.views import admin_blueprint
from lottery.views import lottery_blueprint
#
# # register blueprints with app
app.register_blueprint(users_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(lottery_blueprint)


if __name__ == "__main__":
    app.run()
