import pytest

from tests.helpers import get_products_demo


@pytest.mark.parametrize(
    'page, items_per_page, status_code',
    [
        (1, 6, 200),
    ]
)
def test_get_products_200(client, page, items_per_page, status_code):
    resp = get_products_demo(client, page, items_per_page)
    assert resp.status_code == status_code
    assert len(resp.get_json()) == 2
