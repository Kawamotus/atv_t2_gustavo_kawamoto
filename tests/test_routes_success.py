from unittest.mock import patch


def test_get_all_data_success(client):
    mock_data = [{"id": 1, "title": "mock"}]
    with patch("app.services.requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_data
        response = client.get("/data/")
    assert response.status_code == 200
    assert response.json() == mock_data


def test_get_data_by_id_success(client):
    mock_item = {"id": 1, "title": "mock item"}
    with patch("app.services.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_item
        response = client.get("/data/1")
    assert response.status_code == 200
    assert response.json() == mock_item


def test_create_data_success(client):
    mock_response = {"id": 101, "title": "new item"}
    with patch("app.services.requests.post") as mock_post:
        mock_post.return_value.json.return_value = mock_response
        response = client.post("/data/", json={"title": "new item"})
    assert response.status_code == 200
    assert response.json() == mock_response
