from functools import wraps

from flask import request


def load_request_data(schema):
    """Deserialize a request data & validate it.

    :param schema: the schema used
    :return: deserialized data (dict)
    """

    def wrapper(func):
        @wraps(func)
        def decorated_func(*args, **kwargs):
            if request.method == 'GET':
                data = schema().load(request.args)
            else:
                data = schema().load(request.get_json())
            return func(data=data, *args, **kwargs)
        return decorated_func
    return wrapper
