from App.models import Publication
from App.models import user
from App.database import db
from App.auth import authenticate

def CreatePublication (PublicationTitle, PublicationContent, AuthorInfo, CoAuthorInfo, CategoryInfo ):
    newPublication = Publication(PublicationTitle = PublicationTitle , PublicationContent= PublicationContent, AuthorInfo= AuthorInfo, CoAuthorInfo= CoAuthor, CategoryInfo= CategoryInfo)
    db.session.add= (newPublication)
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

def update_publication(id, PublicationTitle, PublicationContent, CategoryInfo, AuthorInfo, CoAuthorInfo, password):
    Publication= get_publication(id)
    if Publication: 

    
    return None