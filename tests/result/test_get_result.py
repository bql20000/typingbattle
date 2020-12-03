import pytest

from tests.helpers import get_results_demo, get_token


@pytest.mark.parametrize(
    'status_code',
    [
        200,
    ]
)
def test_get_results_200(client, status_code):
    token = get_token(client, 'long', '1234')
    resp = get_results_demo(client, token)
    assert resp.status_code == status_code