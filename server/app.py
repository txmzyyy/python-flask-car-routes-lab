from flask import Flask

app = Flask(__name__)
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

@app.route('/')
def index():
    return "Welcome Flatiron Cars"

@app.route('/<model>')
def car_model(model):
    if model in existing_models:
        return {"model": model}
    else:
        return {"error": "No such car model exists"}

if __name__ == '__main__':
    app.run(debug=True, port=5000)