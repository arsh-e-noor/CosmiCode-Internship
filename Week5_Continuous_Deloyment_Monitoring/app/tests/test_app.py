import pytest
from app.app import app

app.testing = True
client = app.test_client()

def test_homepage():
    response = client.get("/") 
    assert response.status_code == 200  

def test_valid_city():
    response = client.post("/", data={"city": "London"})
    assert response.status_code == 200
    assert b"London" in response.data or b"temp" in response.data

def test_invalid_city():
    response = client.post("/", data={"city": "InvalidCityName123"})
    assert response.status_code == 200
    assert b"city not found" in response.data
