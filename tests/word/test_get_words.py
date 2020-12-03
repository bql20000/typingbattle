import pytest

from tests.helpers import get_words_demo


@pytest.mark.parametrize(
    'mode, status_code',
    [
        ('basic', 200),
        ('random', 200),
    ]
)
def test_get_words_200(client, mode, status_code):
    resp = get_words_demo(client, mode)
    assert resp.status_code == status_code
    assert len(resp.get_json()) == 300


@pytest.mark.parametrize(
    'mode, status_code',
    [
        ('unknown', 400),
    ]
)
def test_get_words_400(client, mode, status_code):
    resp = get_words_demo(client, mode)
    assert resp.status_code == status_code
    assert 'message' in resp.get_json()

