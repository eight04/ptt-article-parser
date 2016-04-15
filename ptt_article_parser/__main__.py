#! python3

"""
PTT Article Parser (PAP)

Usage:
  pap rename [--format=<format>] <file>...
  pap rename [--format=<format>] --interactive
  pap --help
	
Options:
  -h --help             Show this.
  -f --format=<format>  Set output format. 
                        [default: [{board}] {title} [{author}] ({time:%Y%m%d%H%M%S}).ans]
  -i --interactive      Use interactive mode, get file name from stdin.
  <file>                File path. You can use glob pattern
  
"""

import glob

from docopt import docopt

from . import Article
from .tools import rename

def main():
	try:
		imp_main()
	except Exception:
		import traceback
		traceback.print_exc()		
		input("\n\nPress enter to exit...")
		
		
def imp_main():
	args = docopt(__doc__)
	
	# Rename file
	if args["rename"]:
		from .tools import rename
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
	main()
