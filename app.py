from flask import Flask
from views import views

# ovaj dio inicijalizira aplikaciju
app = Flask(__name__)

app.secret_key = "kljuc"
#app.register_blueprint(views, url_prefix="/views")
app.register_blueprint(views)


# @app.route("/")
# def home():
#     return "this is the home page"

# run the app
# debug = True prati promjene pa ne moramo iznova pokretati app
if __name__ == '__main__':
    app.run(debug=True, port=8000)