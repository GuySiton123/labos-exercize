from flask import Flask
from datetime import date

app = Flask(__name__)


@app.route("/")
def serve_file():
    with open("date.html", "r") as f:
        today = date.today()
        content = f.read()
        content = content.replace("[DAY_OF_WEEK]", "{}".format(today.strftime("%A")))
        content = content.replace("[CURRENT_DATE]", "{}".format(today.strftime("%d/%m/%Y")))
    return content


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
