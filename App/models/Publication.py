from App.database import db
from App.models import user


class Publication(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    publicationId = db.Column(db.Integer, nullable = False)
    title= db.Column(db.String, nullable= False)
    content = db.Column(db.String, nullable = False)
    name= db.Column(db.String, db.ForeignKey(user.username),db.Reference(user.username), nullable = False)
    credentials = db.Column(db.String, db.ForeignKey(user.credentials), nullable = False)
    category = db.Column(db.String, nullable = False)

    def init(self, title, content, name, credentials, category):

        self.PublicationId = PublicationId
        self.title = title
        self.content = content
        self.name = name
        self.credentials = credentials
        self.category= category


    def toJSON(self):

        return{

            'id': self.id,
            'Publication ID': self.PublicationId,
            'title':self.title,
            'content': self.content,
            'author':self.name,
            'author credentials': self.credentials,
            'category':self.category

        }

