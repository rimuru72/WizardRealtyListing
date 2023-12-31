from website.models import Person, Employee, Client, Property, Address
from website import db, create_app

app = create_app()

with app.app_context():
        db.create_all()
        db.session.commit()

print("database updated successfully")
