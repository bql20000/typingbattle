from main.models.product import ProductModel
from main.models.result import ResultModel
from main.models.unit import UnitModel
from main.models.user import UserModel
from main.models.word import WordModel


def init_users():
    """Create 2 sample users."""
    UserModel('long', '1234').save_to_db()
    UserModel('long2', '1234').save_to_db()


def init_words():
    """Create 200 words"""
    for i in range(200):
        WordModel('a').save_to_db()


def init_units():
    """Create 200 words"""
    for i in range(18):
        UnitModel('m').save_to_db()


def init_results():
    """Create 2 sample results"""
    ResultModel('basic', 15, 90, 60, 1).save_to_db()
    ResultModel('basic', 30, 100, 50, 1).save_to_db()


def init_products():
    """Create 1 sample product"""
    ProductModel('title', 'abc', 4.5, '.com', 100, 'USD', 12).save_to_db()


def create_db_samples():
    """Execute all the sample creations."""
    init_users()
    init_words()
    init_results()
    init_products()
    init_units()


def register_demo(client, request_data):
    """Return a response object received by the client after making a
    HTTP POST request to register.
    """
    return client.post('/register', json=request_data)


def login_demo(client, request_data):
    """Return a response object received by the client after making a
    HTTP POST request to login.
    """
    return client.post('/login', json=request_data)


def get_words_demo(client, mode):
    return client.get(f'/words?mode={mode}')


def get_results_demo(client, token):
    return client.get(f'/results', headers={'AUTHORIZATION': f'Bearer {token}'})


def get_products_demo(client, page, items_per_page):
    return client.get(f'products?page={page}&items_per_page={items_per_page}')


def get_token(client, username, password):
    """Returns JWT access token after some user logs in."""
    return login_demo(client, {'username': username, 'password': password}
                      ).get_json()['access_token']