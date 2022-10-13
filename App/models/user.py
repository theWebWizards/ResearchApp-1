from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class RegUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False)
    

    def __init__(self, username, password, email, fullname):
        self.username = username
        
       

    def toJSON(self):
        return{
            'id': self.id,
            'username': self.username,
            
        }

    

class Author(RegUser):
    email =  db.Column(db.String,nullable=False)
    fullname = db.Column(db.String,nullable=False)
    password = db.Column(db.String(120),nullable=False)
    credentials= db.Column(db.String,nullable=False )




    def __init__(self,  password, email, fullname, credentials):
       
        self.fullname = fullname
        self.set_password(password)
        self.email=email
        self.credentials= credentials

    def toJSON(self):
        return{
            'name': self.fullname,
            'email': self.email,
            'credentials': self.credentials
        }
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)