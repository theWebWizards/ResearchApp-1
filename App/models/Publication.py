from App.database import db
from App.models import user


class Publication(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    publicationid = db.Column(db.Integer, nullable = False, primary_key=True)
    title= db.Column(db.String, nullable= False)
    content = db.Column(db.String, nullable = False)
    userid= db.Column(db.String, db.ForeignKey('user.userid'))
    #credentials = db.Column(db.String, db.ForeignKey('user.credentials'))
    category = db.Column(db.String, nullable = False)

    def _init_(self, publicationid, title, content, userid, category):

        self.publicationid = publicationid
        self.title = title
        self.content = content
        self.userid = userid
        #self.username = username
        #self.credentials = credentials
        self.category = category


    def toJSON(self):

        return{

            'id': self.id,
            'publicationid': self.PublicationId,
            'title':self.title,
            'content': self.content,
            'username':self.username,
            #'author credentials': self.credentials,
            'category':self.category

        }

