from flask import Flask
from flask_cors import CORS
from routes.home import home
from routes.github import github
from routes.runcode import runcode
from routes.atom import atom

app = Flask(__name__)
app.debug = True
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(home, url_prefix='/')
app.register_blueprint(github, url_prefix='/api/github')
app.register_blueprint(atom, url_prefix='/')
app.register_blueprint(runcode, url_prefix='/')
