from marshmallow.validate import Validator
from marshmallow import ValidationError


class FirstCharNotNum(Validator):
    error = 'First character must not be a number.'

    def __call__(self, name):
        if name and '9' >= name[0] >= '0':
            raise ValidationError(FirstCharNotNum.error)
        return name
