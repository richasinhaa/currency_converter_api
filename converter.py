from app import app
from flask_cors import CORS

CORS(app, support_credentials=True)