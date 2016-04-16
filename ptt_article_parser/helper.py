#! python

import re, glob

fn_repl = {
	"/": "／",
	"\\": "＼",
	"?": "？",
	"|": "｜",
	"<": "＜",
	">": "＞",
	":": "：",
	"\"": "＂",
	"*": "＊"
}

fn_pattern = re.compile(r"[/\\?|<>:\"*]")

def fn_repl_func(match):
	return fn_repl[match.group()]

def safe_file_name(name):
	"""Replace unsafe characters"""
	return fn_pattern.sub(fn_repl_func, name)

class FormatDummy:
	"""A dummy object which always returns None in __format__"""
	def __format__(self, spec):
		return "None"
		
format_dummy = FormatDummy()
