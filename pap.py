#! python3

"""
PTT Article Parser (PAP)

Usage:
  pap.py rename [--format=<format>] <file>...
  pap.py rename [--format=<format>] --interactive
  pap.py --help
	
Options:
  -h --help             Show this.
  -f --format=<format>  Set output format. 
                        [default: [@board] @title by @author.@time.ans]
  -i --interactive      Use interactive mode, get file name from stdin.
  <file>                File path. You can use glob pattern
  
"""

from docopt import docopt
from core import Article
from safeprint import print
import time, re, os, sys, glob

def makeSafeFileName(path):
	d = {
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
	pattern = re.compile(r"[/\\?|<>:\"*]")
	return pattern.sub(lambda x: d[x.group()], path)
	
def safeRename(src, new):
	dir, old = os.path.split(src)
	
	if old == new:
		return
	
	dest = os.path.join(dir, new)	
	
	if os.path.isfile(dest):
		fn, ext = os.path.splitext(new)
		
		i = 2
		while True:
			dest = os.path.join(dir, "{} ({}){}".format(fn, i, ext))
			if not os.path.isfile(dest):
				break
			i += 1
	
	os.rename(src, dest)

	
def rename(file, format):
	with open(file, "rb") as f:
		source = f.read()
		
	dir, filename = os.path.split(file)
	
	print("Parse {}...".format(filename))
		
	article = Article(source)
	
	repl = {}
	repl["@title"] = article.getTitle() or "None"
	repl["@author"] = article.getAuthor() or "None"
	repl["@board"] = article.getBoard() or "None"
	tm = article.getTime()
	if tm:
		tm = time.strftime("%Y%m%d%H%M%S", tm)
	repl["@time"] = tm or "None"
	
	pattern = re.compile(r"(" + "|".join(repl.keys()) + ")")
	newFile = pattern.sub(lambda x: repl[x.group()], format)
	newFile = makeSafeFileName(newFile)
	
	print("Rename to {}...\n".format(newFile))
	
	safeRename(file, newFile)
	
def main():
	args = docopt(__doc__)
	
	# Rename file
	if args["rename"]:
		if args["--interactive"]:
			print("You are using interactive mode, please input the file path. ^Z to exit:")
			while True:
				try:
					file = input()
				except EOFError:
					break
				else:
					rename(file, args["--format"])
		else:
			files = args["<file>"]
			for file_pattern in file_patterns:
				for file in glob.iglob(file_pattern):
					rename(file, args["--format"])

if __name__ == "__main__":
	try:
		main()
	except Exception:
		import traceback
		traceback.print_exc()		
		input("\n\nPress enter to exit...")
