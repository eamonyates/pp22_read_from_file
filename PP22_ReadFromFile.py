import requests
from bs4 import BeautifulSoup

def web_to_text(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')

	with open('nameslist.txt', 'w') as open_file:
		open_file.write(str(soup))


def count_names(text_file):
	with open(text_file, 'r') as open_file:	
		#create a dictionary with the list of names and the number of times it appears
		name_dict = {}
		for name in open_file:
			strip_name = name.strip()

			if strip_name in name_dict:
				name_dict[strip_name] += 1
			else:
				name_dict[strip_name] = 1

		for k, v in name_dict.items():
			print (k, v)


if __name__ == '__main__':
	web_to_text('http://www.practicepython.org/assets/nameslist.txt')
	count_names('nameslist.txt')
