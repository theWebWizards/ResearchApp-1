from App.database import db
from enum import enum

class Publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    PublicationTitle= db.Column(db.String, nullable= False )
    PublicationContent = db.Column(db.String, nullable = False)
    AuthorInfo= db.Column(db.String, nullable= False )
    CoAuthorInfo = db.Column(db.String, nullable = True)
    CategoryInfo= db.Column(db.String, nullable= False )

    def __init__(self, PublicationTitle, PublicationContent, AuthorInfo, CoAuthorInfo, CategoryInfo):
        self.PublicationTitle= PublicationTitle
        self.PublicationContent = PublicationContent
        self.AuthorInfo= AuthorInfo
        self.CoAuthorInfo = CoAuthorInfo
        self.CategoryInfo= CategoryInfo


    def toJSON(self):
        return{
            'id': self.id,
            'Title':self.PublicationTitle,
            'Content': self.PublicationContent,
            'Author':self.AuthorInfo,
            'CoAuthor': self.CoAuthorInfo,
            'Category':self.CategoryInfo
        }