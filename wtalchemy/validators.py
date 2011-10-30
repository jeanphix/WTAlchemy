from wtforms import ValidationError
from sqlalchemy.orm.exc import NoResultFound


class Unique(object):
    """Checks field value unicity against specified table field.
    """
    field_flags = ('unique', )

    def __init__(self, get_db_session, field, message=None):
        self.get_db_session = get_db_session
        self.field = field
        self.message = message

    def __call__(self, form, field):
        try:
            self.get_db_session().query(self.field)\
                .filter(self.field == field.data).one()
            if self.message is None:
                self.message = field.gettext(u'Allready exists.')
            raise ValidationError(self.message)
        except NoResultFound:
            pass
