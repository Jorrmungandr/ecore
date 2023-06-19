from datetime import datetime

from schematics.models import Model
from schematics.exceptions import DataError

class BaseEntity(Model):
    def validate(self, *args, **kwargs):
        super(BaseEntity, self).validate(*args, **kwargs)

        errors = {}

        for key, value in self.items():
            if isinstance(value, str) and ',' in value:
                errors[key] = 'Field cannot contain commas.'

        if errors:
            raise DataError(errors)

    def values(self):
        values = super().values()

        for index, value in enumerate(values):
            if isinstance(value, datetime):
                values[index] = value.strftime('%m/%Y')

        return values
