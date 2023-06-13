import click
from BANK.ext.database import db
from BANK.models import Users, Roles


def create_db(app):
    """Creates database"""
    with app.app_context():
        db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
            Roles(id=1, description="Jose description role"),
            Roles(id=2, description="Raquel description role"),
            Users(id=1, name="Jose", role_id="1", email="jose@gmail.com"),
            Users(id=2, name="Raquel", role_id="2", description="raquel@email.com")
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return [Users.query.all(), Roles.query.all()]


def init_app(app):
    create_db(app)
