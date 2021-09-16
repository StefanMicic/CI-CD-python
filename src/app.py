from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "CI/CD works!!"


if __name__ == "__main__":
    app.run()
