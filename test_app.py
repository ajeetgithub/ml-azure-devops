import json
from app import app

def test_home():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200

def test_prediction():
    tester = app.test_client()
    payload = {"features": [1, 2, 3, 4]}
    response = tester.post(
        "/predict",
        data=json.dumps(payload),
        content_type="application/json"
    )
    data = json.loads(response.data)
    assert response.status_code == 200
    assert "prediction" in data