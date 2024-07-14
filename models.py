from extensions import db, login_manager, create_app 
from flask_login import UserMixin

app = create_app()

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    image_url = db.Column(db.String)
    text = db.Column(db.String)

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True) 
    password = db.Column(db.String)
    username = db.Column(db.String, unique=True) 
    role = db.Column(db.String)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(email="admin@gmail.com").first():
            admin = User(email="admin@gmail.com", password="admin1234", username="admin", role="admin")
            db.session.add(admin)
            db.session.commit()