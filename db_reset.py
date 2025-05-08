from app import app
from models.db import db
from models.auth import User

with app.app_context():
    db.drop_all()
    db.create_all()
    print("Database reset complete ✅")
