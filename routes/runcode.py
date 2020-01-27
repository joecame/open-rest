from flask import Blueprint,request
import requests

runcode = Blueprint('runcode', __name__)

languages = ['C', 'Cpp', 'Cpp14', 'Java', 'Python', 'Python3', 'Scala', 'Php', 'Perl', 'Csharp']

# ['C', 'CPP', 'CPP11', 'CPP14', 'CLOJURE', 'CSHARP', 'GO', 'HASKELL', 
# 'JAVA', 'JAVA8', 'JAVASCRIPT', 'JAVASCRIPT_NODE', 'OBJECTIVEC', 'PASCAL', 
# 'PERL', 'PHP', 'PYTHON', 'PYTHON3', 'R', 'RUBY', 'RUST', 'SCALA', 'SWIFT', 'SWIFT_4_1']
@runcode.route('/api/runcodev2/<lang>/<code>', methods=['GET'])
def run_code(lang,code):
	# 73a1fc29f9a43c67a8bc996777ebb248d9b8b9cd
	data = {
		'client_secret': '69c68a6905f73de654c15c05744a5e93147c1132',
		'async': 0,
		'source': code,
		'lang': lang.upper(),
		'time_limit': 5,
		'memory_limit': 262144,
	}
	r = requests.post(u'https://api.hackerearth.com/v3/code/run/', data=data)
	return r.json()["run_status"]

@runcode.route('/api/runcode', methods=['POST'])
def gfg_compile():	
	user_code = request.json['code']
	lang_choosed = request.json['lang']
	data = {'lang': lang_choosed,'code': user_code,'input': None,'save': False}
	r = requests.post("https://ide.geeksforgeeks.org/main.php", data=data)
	return r.json()