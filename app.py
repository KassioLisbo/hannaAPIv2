from flask import Flask
from Routes.home import home_pg

app = Flask(__name__)

app.register_blueprint(home_pg)

app.run(debug=True) 