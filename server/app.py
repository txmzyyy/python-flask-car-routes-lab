from flask import Flask

app = Flask(__name__)
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

@app.route('/')
def index():
    return "Welcome Flatiron Cars"

@app.route('/models')
def car_models():
    if existing_models:
        return {"models": existing_models}
    else:
        return {"error": "No such car model exists"}
