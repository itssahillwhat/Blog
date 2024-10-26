from db import db, BlogPost, Users

with db.app.app_context():
    db.create_all()