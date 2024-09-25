from flask import Flask, render_template
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
app.config['SQLALCHMEY_DATABASE_URI'] = 'sqlite:///app.db' 


@app.route('/')
def index():
    return render_template('index.html')

try:
    app.run(debug=True, host='0.0.0.0', port=8080)
except Exception as e:
    app.logger.error(f"App startup error: {str(e)}")

