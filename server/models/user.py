from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password= db.Column(db.String(100), nullable=False)
    
    def set_password(self, password):
        self.password_harsh = generate_password_hash(password)
        
    def check_password(self, password):
        return  check_password_hash (self.check_password, password)
    
    def to_dict(self):
        return{
            'id': self.id,
            'username': self.username
        }