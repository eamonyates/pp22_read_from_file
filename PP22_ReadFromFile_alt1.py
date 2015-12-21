import requests
from bs4 import BeautifulSoup

def web_to_text(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')

	with open('sunDatabase.txt', 'w') as open_file:
		open_file.write(str(soup))


def count_categories(text_file):
	with open(text_file, 'r') as open_file:	
		
		category_dict = {}
		for line in open_file:
			split_line_list = line.split('/')
			category = split_line_list[2].strip()

			if category in category_dict:
				category_dict[category] += 1
			else:
				category_dict[category] = 1

		for k, v in category_dict.items():
			print (k, v)


if __name__ == '__main__':
	web_to_text('http://www.practicepython.org/assets/Training_01.txt')
	count_categories('sunDatabase.txt')
