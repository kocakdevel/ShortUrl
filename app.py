from flask import Flask, render_template
from dotenv import load_dotenv
from models import db, User, ShortUrl
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


def init_db():
    with app.app_context():
        db.create_all()
        app.logger.info("Database initialized")

try:
    init_db()
    app.run(debug=True, host='0.0.0.0', port=8080)
except Exception as e:
    app.logger.error(f"App startup error: {str(e)}")
