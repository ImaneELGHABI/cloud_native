import requests

def test_predict_endpoint():
    url = 'http://localhost:6000/predict'
    data = {
        "bedrooms": 3,
        "bathrooms": 2.5,
        "sqft_living": 2000,
        "sqft_lot": 5000,
        "floors": 2.0,
        "waterfront": 0,
        "view": 1,
        "condition": 3,
        "grade": 7,
        "sqft_above": 1600,
        "sqft_basement": 400,
        "yr_built": 1990,
        "yr_renovated": 0,
        "zipcode": 98101,
        "lat": 47.6186,
        "long": -122.3381,
        "sqft_living15": 2100,
        "sqft_lot15": 5200
    }
    response = requests.post(url, json=data)
    print(response)
    print(response.text)

    assert response.status_code == 200
    assert 'prediction' in response.json()

test_predict_endpoint()