from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1> Hello world! </h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello!"


def cel_to_fahrenheit(cel):
    return cel * 9.0 / 5.0 + 32


@app.route('/convert/<celsius>')
def convert(celsius):
    try:
        fahrenheit = cel_to_fahrenheit(float(celsius))
        return f"The temperature in Fahrenheit is {fahrenheit}"
    except ValueError:
        abort(400, description="Invalid temperature provided.")


app.run(debug=True)
