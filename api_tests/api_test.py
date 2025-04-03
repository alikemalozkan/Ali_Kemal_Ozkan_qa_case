import requests

BASE_URL = "https://petstore.swagger.io/v2/pet"

def test_create_pet():
    pet_data = {"id": 12345, "name": "Fluffy", "status": "available"}
    response = requests.post(BASE_URL, json=pet_data)
    assert response.status_code == 200

def test_get_pet():
    response = requests.get(f"{BASE_URL}/12345")
    assert response.status_code == 200

def test_delete_pet():
    response = requests.delete(f"{BASE_URL}/12345")
    assert response.status_code == 200

if __name__ == "__main__":
    test_create_pet()
    test_get_pet()
    test_delete_pet()
