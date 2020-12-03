def test_get_page(client):
    resp = client.get('/')
    assert resp.status_code == 200
