WTAlchemy
---------

Provides a SQLAlchemy extension for WTForms.

Deals with relationship, unicity and more.::

    from wtalchemy.orm import model_form

    class User(Model):
        __tablename__ = "user"
        id = Column(Integer, primary_key=True)
        username = Column(String(255), nullable=False, unique=True)

    UserForm = model_form(User, db_session)
