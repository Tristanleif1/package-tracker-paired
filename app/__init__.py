from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from .config import Configuration
from .routes import packages

app = Flask(__name__)

app.config.from_object(config.Configuration)
# print(dir(Configuration))
# print(Configuration.SQLALCHEMY_DATABASE_URI)
app.register_blueprint(packages.bp)


db = SQLAlchemy()

db.init_app(app)


@app.route("/", methods=["GET"])
def root():
    return render_template('index.html', title='title')

@app.route("/new_package", methods=["GET, POST"])
def new_package():
    return render_template('shipping_request.html', request='request')