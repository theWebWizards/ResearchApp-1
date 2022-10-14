from App.models import Publication
from App.models import user
from App.database import db
from App.auth import authenticate

def CreatePublication (PublicationTitle, PublicationContent, AuthorName, AuthorCredentials, CategoryInfo ):
    newPublication = Publication(PublicationTitle = PublicationTitle , PublicationContent= PublicationContent, AuthorName = AuthorName, AuthorCredentials = AuthorCredentials, CategoryInfo= CategoryInfo)
    db.session.add = (newPublication)
    db.session.commit()
    return newPublication

def get_publication_by_title(PublicationTitle):
    return Publication.query.filter_by(PublicationTitle= PublicationTitle).first()

def get_publication(id):
    return Publication.query.get(id)

def get_all_publications():
    return Publication.query.all()

def get_all_publication_json():
    Publication = Publications.query.all()
    if not Publication:
        return []
    Publication = [Publication.toJSON() for Publication in Publication]
    return Publication

def update_publication(id, PublicationContent):
    Publication = get_publication(id)
    Publication.PublicationContent = PublicationContent
    db.session.add(PublicationContent)
    db.session.commit()
    return None

def delete_publication(id):
    Publication = get_publication(id)
    if Publication:
        db.session.delete(Publication)
        db.session.commit()
    return None