#! python3

"""
PTT Article Parser (PAP)

Usage:
  pap rename [--format=<format>] <file>...
  pap rename [--format=<format>] --interactive
  pap (--help | --version)
	
Options:
  -v --version          Show version.
  -h --help             Show this.
  -f --format=<format>  Set output format. 
                        [default: [{board}] {title} [{author}] ({time:%Y%m%d%H%M%S}).ans]
  -i --interactive      Use interactive mode, get file name from stdin.
  <file>                File path. If the file doesn't exists, pap will try to parse it as glob pattern.
  
"""

import docopt, os.path, glob

from . import Article, __version__
from .tools import rename
from .helper import gen_file

def do_rename(file, format):
	"""Use glob pattern if file dosn't exist"""
	if os.path.isfile(file):
		rename(file, format)
	else:
		for f in glob.iglob(file):
			rename(f, format)

def main():
	"""Main entry"""
	args = docopt.docopt(__doc__, version=__version__)
	
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
					do_rename(file, args["--format"])
		else:
			for file in args["<file>"]:
				do_rename(file, args["--format"])
				
if __name__ == "__main__":
	main()
