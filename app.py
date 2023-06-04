from flask import Flask, request, render_template
import MLModel as model

# Create flask app
flask_app = Flask(__name__)

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    features= [str(x) for x in request.form.values()]
    print(features)
    prediction = model.predict(features[0],features[1],features[2],features[3])
    tup = model.precaution(prediction)
    return render_template("index.html", prediction_text = "You are suffering from: {} {}".format(prediction + "; Precautions:", tup[0]+", "+tup[1]+", "+tup[2]+", "+tup[3]))

@flask_app.route("/symptomsList", methods = ["POST"])
def symptomsList():
    symptomList = model.symptomsList()
    return render_template("index.html", symptom_text = "List of symptoms: {}".format(symptomList))

if __name__ == "__main__":
    flask_app.run(debug=True)