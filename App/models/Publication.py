from App.database import db
from enum import enum

class Publication(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    PublicationId = db.Column(db.Integer, nullable = False)
    PublicationTitle= db.Column(db.String, nullable= False)
    PublicationContent = db.Column(db.String, nullable = False)
    AuthorName= db.Column(db.String, db.ForeignKey(user.fullname), nullable = False)
    AuthorCredentials = db.Column(db.String, db.ForeignKey(user.credentials), nullable = False)
    CategoryInfo= db.Column(db.String, nullable = False)

    def init(self, PublicationId, PublicationTitle, PublicationContent, AuthorName, AuthorCredentials, CategoryInfo):

        self.PublicationId = PublicationId
        self.PublicationTitle= PublicationTitle
        self.PublicationContent = PublicationContent
        self.AuthorName = AuthorName
        self.AuthorCredentials = AuthorCredentials
        self.CategoryInfo= CategoryInfo


    def toJSON(self):

        return{

            'id': self.id,
            'Publication ID': self.PublicationId,
            'Title':self.PublicationTitle,
            'Content': self.PublicationContent,
            'Author':self.AuthorInfo,
            'Author Credentials': self.AuthorCredentials,
            'Category':self.CategoryInfo

        }
        