from flask import Flask, render_template, request, redirect, url_for, session, flash

import requests as req

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Get the input from post request
        input = {
            "bedrooms": request.form["bedrooms"],
            "bathrooms": request.form["bathrooms"],
            "sqft_living": request.form["sqft_living"],
            "sqft_lot": request.form["sqft_lot"],
            "floors": request.form["floors"],
            "waterfront": request.form["waterfront"],
            "view": request.form["view"],
            "condition": request.form["condition"],
            "grade": request.form["grade"],
            "sqft_above": request.form["sqft_above"],
            "sqft_basement": request.form["sqft_basement"],
            "yr_built": request.form["yr_built"],
            "yr_renovated": request.form["yr_renovated"],
            "zipcode": request.form["zipcode"],
            "lat": request.form["lat"],
            "long": request.form["long"],
            "sqft_living15": request.form["sqft_living15"],
            "sqft_lot15": request.form["sqft_lot15"],
        }

    # Send the input as a post request to the model
    response = req.post("http://localhost:6000/predict", json=input)
    prediction = response.json()["prediction"]
    return render_template("predict.html", prediction=prediction)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
