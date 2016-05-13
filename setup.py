#! python3

import re

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

def read(file):
	with open(path.join(here, file), encoding='utf-8') as f:
		content = f.read()
	return content
	
def find_version(file):
	return re.search(r"__version__ = (\S*)", read(file)).group(1).strip("\"'")
	
setup(
	name = "ptt-article-parser",
	version = find_version("ptt_article_parser/__init__.py"),
	description = 'A renaming tool for PTT articles',
	long_description = read('README.rst'),
	url = 'https://github.com/eight04/ptt-article-parser',
	author = 'eight',
	author_email = 'eight04@gmail.com',
	license = 'MIT',
	# See https://pypi.python.org/pypi?%3Aaction=list_classifiers
	classifiers = [
		"Development Status :: 4 - Beta",
		"Environment :: Console",
		"Environment :: Win32 (MS Windows)",
		"Intended Audience :: Developers",
		"Intended Audience :: End Users/Desktop",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: Chinese (Traditional)",
		"Operating System :: Microsoft :: Windows :: Windows 7",
		"Programming Language :: Python :: 3.5",
		"Topic :: Terminals"
	],
	keywords = 'ptt article parser',
	packages = find_packages(),
	install_requires = [
		"docopt~= 0.6.2", 
		"safeprint~=0.1.1"
	],
	entry_points = {
		"console_scripts": [
			"pap=ptt_article_parser.__main__:main"
		]
	}
)
