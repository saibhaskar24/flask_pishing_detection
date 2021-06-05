from os import error
from flask import Flask, request, render_template
# from loader import makeTokens
import loader

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def check():
    message = None
    website = None
    if request.method == "POST":
       url_data = request.form.get("url_data")
       y = loader.check_is_pissing(url_data)
       message = y[0]
       website = url_data
    return render_template("authentication.html",website = website, message = message)

if __name__=='__main__':
    app.run()