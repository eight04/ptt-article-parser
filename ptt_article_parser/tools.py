#! python3

import pathlib

from safeprint import print

from . import Article
from .helper import safe_file_name, format_dummy
from .dir import DIR

def rename(file, format_spec, dir=DIR()):
	"""Rename article with specified format"""
	file = pathlib.Path(file)
	
	print("Parsing {name}...".format(name=file.name))
	
	article = Article(file.read_bytes())
	
	new_file = format_spec.format(
		article = article,
		title = dir.getTitle(file) or article.getTitle(),
		author = article.getAuthor() or dir.getAuthor(file),
		board = article.getBoard(),
		time = article.getTime() or dir.getTime(file) or format_dummy
	)
	new_file = safe_file_name(new_file)
	new_file = file.with_name(new_file)
	
	if file == new_file:
		print("Same file name!\n")
		return
	
	if new_file.exists():
		num = 2
		
		while True:
			temp_file = "{name} ({num}){ext}".format(
				num = num,
				name = new_file.stem,
				ext = new_file.suffix
			)
			temp_file = new_file.with_name(temp_file)
			
			if file == temp_file:
				print("Same file name!\n")
				return
				
			if not temp_file.exists():
				new_file = temp_file
				break
				
			num += 1
	
	print("Rename to {name}...\n".format(name=new_file.name))
	
	file.rename(new_file)
