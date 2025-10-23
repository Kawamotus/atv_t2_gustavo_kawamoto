from unittest.mock import patch

def test_get_data_by_id_not_found(client):
    with patch("app.services.requests.get") as mock_get:
        mock_get.return_value.status_code = 404
        response = client.get("/data/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_create_data_invalid_json(client):
    response = client.post("/data/", data="invalid")
    assert response.status_code == 422 
