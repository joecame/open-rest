from flask import Flask
import os
from flask_cors import CORS
from routes.home import home
from routes.github import github
from routes.runcode import runcode
from routes.atom import atom

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(home, url_prefix='/')
app.register_blueprint(github, url_prefix='/api/github')
app.register_blueprint(atom, url_prefix='/')
app.register_blueprint(runcode, url_prefix='/')

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=port)