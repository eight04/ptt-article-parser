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
	return fn_pattern.sub(fn_repl_func, name)

class FormatDummy:
	def __format__(self, spec):
		return "None"
		
format_dummy = FormatDummy()