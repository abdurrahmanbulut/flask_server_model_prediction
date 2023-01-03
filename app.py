import jsonpickle
from flask import Flask, request, jsonify
from flask_cors import CORS

# Load the model from the JSON file
with open("model.json", "r") as f:
    model_json = f.read()
model = jsonpickle.decode(model_json)




# Initialize the Flask app
app = Flask(__name__)
CORS(app)



@app.route("/predict", methods=["POST"])
def predict():
    # Get the input data from the request body
    data = request.get_json(force=True)
    input_data = data["input"]
    print("sd", data)
    # Use the model to make a prediction
    prediction = model.predict(input_data).tolist()

    # Return the prediction as a JSON response
    return jsonify(prediction)

if __name__ == "__main__":
    app.run()
	