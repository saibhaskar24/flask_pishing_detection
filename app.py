from os import error
from flask import Flask, request, render_template
# from loader import makeTokens
import loader

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def check():
    message = None
    website = None
    is_good = None
    is_bad = None
    if request.method == "POST":
        url_data = request.form.get("url_data")
        y = loader.check_is_pissing(url_data)
        message = y[0]
        website = url_data
        if message == "good":
            is_good = "True"
        else:
            is_bad = "True"

    return render_template("authentication.html",website = website, message = message, is_good= is_good, is_bad=is_bad)

if __name__=='__main__':
    app.run()