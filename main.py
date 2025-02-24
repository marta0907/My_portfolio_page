from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/developer")
def dev():
    return render_template('DEV.html')

@app.route("/economy_analyst")
def econ():
    return render_template('ECON.html')

@app.route("/hobby")
def hobby():
    return render_template('HOBBY.html')


if __name__ == "__main__":
    app.run(debug=True)
