from flask import Blueprint

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def index():	
	return "hello world"