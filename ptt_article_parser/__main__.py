#! python3

"""
PTT Article Parser (PAP)

Usage:
  pap rename [--format=<format>] [--dir=<file>] <file>...
  pap rename [--format=<format>] [--dir=<file>] --interactive
  pap (--help | --version)
	
Options:
  -v --version          Show version.
  -h --help             Show this.
  -f --format=<format>  Set output format. 
                        [default: [{board}] {title} [{author}] ({time:%Y%m%d%H%M%S}).ans]
  -d --dir=<file>       Read additional ".DIR" file. The tool always tries to 
                        read the ".DIR" file under the parent folder of the
                        article. Use this option to read from other locations.
  -i --interactive      Use interactive mode, get file name from stdin.
  <file>                File path. If the file doesn't exists, pap will try to
                        parse it as glob pattern.
  
"""

import glob
import os.path
import docopt
from . import __version__
from .tools import rename

def do_rename(pattern, format, dir=None):
	"""Use glob pattern if file dosn't exist"""
	def get_files():
		if os.path.isfile(pattern):
			yield pattern
		else:
			yield from glob.iglob(pattern, recursive=True)

	for file in get_files():
		rename(file, format, dir)

def main():
	"""Main entry"""
	args = docopt.docopt(__doc__, version=__version__)
	
	# Rename file
	if args["rename"]:
		def files_from_input():
			print("You are using interactive mode, please input the file path. ^Z to exit:")
			while True:
				try:
					file = input()
					if file:
						yield file
				except EOFError:
					break
					
		from .dir import DIR
		dir = DIR()
		if args["--dir"]:
			dir.read_file(args["--dir"])
			
		for file in files_from_input() if args["--interactive"] else args["<file>"]:
			do_rename(file, args["--format"], dir=dir)
				
if __name__ == "__main__":
	main()
