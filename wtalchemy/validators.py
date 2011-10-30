from wtforms import ValidationError
from sqlalchemy.orm.exc import NoResultFound


class Unique(object):
    """Checks field value unicity against specified table field.
    """
    field_flags = ('unique', )

    def __init__(self, get_session, model, column, message=None):
        self.get_session = get_session
        self.model = model
        self.column = column
        self.message = message

    def __call__(self, form, field):
        try:
            obj = self.get_session().query(self.model)\
                .filter(self.column == field.data).one()
            if not hasattr(form, '_obj') or not form._obj == obj:
                if self.message is None:
                    self.message = field.gettext(u'Allready exists.')
                raise ValidationError(self.message)
        except NoResultFound:
            pass
