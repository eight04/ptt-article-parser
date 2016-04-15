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
  <file>                File path. You can use glob pattern
  
"""

import docopt

from . import Article, __version__
from .tools import rename
from .helper import gen_file

def main():
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
					rename(file, args["--format"])
		else:
			for file in gen_file(args["<file>"]):
				rename(file, args["--format"])

if __name__ == "__main__":
	main()
