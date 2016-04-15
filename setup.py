#! python3

"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
	
settings = {
	"name": "ptt-article-parser",
	"version": __import__("ptt_article_parser.version").__version__,
	"description": 'A renaming tool for PTT articles',
	# Get the long description from the relevant file
	"long_description": long_description,
	"url": 'https://github.com/eight04/ptt-article-parser',
	"author": 'eight',
	"author_email": 'eight04@gmail.com',
	"license": 'MIT',
	# See https://pypi.python.org/pypi?%3Aaction=list_classifiers
	"classifiers": [
		"Development Status :: 3 - Alpha",
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
	"keywords": 'ptt article parser',
	"packages": ["ptt_article_parser"],
	"install_requires": ["safeprint", "docopt"],
	"entry_points": {
		"console_scripts": [
			"pap=ptt_article_parser.__main__:main"
		]
	}
}

if __name__ == "__main__":
	setup(**settings)
