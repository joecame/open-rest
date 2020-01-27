from flask import Blueprint,jsonify
import requests
from bs4 import BeautifulSoup

atom = Blueprint('atom', __name__)

@atom.route('/api/atom/package/<name>', methods=['GET'])
def atom_package_details(name):
	resp = requests.get(f'https://atom.io/packages/search?q={name}')
	soup = BeautifulSoup(resp.content, 'html.parser')
	elemnt = soup.find('div', class_='grid-cell')

	package_author = elemnt.find('a', class_='author').get_text()
	package_gravatar = elemnt.find('img', class_='gravatar')
	
	package_name = elemnt.find('span', class_='css-truncate-target')
	package_desc = elemnt.find('span', class_='card-description').get_text()
	package_downloads = elemnt.find('span', class_='value').get_text()
	package_stars = elemnt.find('div', class_='star-box').get_text().strip()
	package_url = 'https://atom.io'+package_name.findChildren()[0]['href']

	# get package tags
	package_tags_ul = elemnt.find('ul', class_='keywords').findChildren()
	package_tags = []
	for t in package_tags_ul:
		tagname = t.get_text().replace('#', '')
		if tagname not in package_tags:
			package_tags.append(tagname)

	return jsonify({
		'package_author':package_author.strip(),
		'package_gravatar':package_gravatar['src'],
		'package_name':package_name.get_text(),
		'package_desc':package_desc,
		'package_url':package_url,
		'package_stars':package_stars,
		'package_downloads':package_downloads,
		'package_tags':package_tags
	})
