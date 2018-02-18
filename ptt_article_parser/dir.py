import datetime
import pathlib
import struct
from . import uao_decode, strip_color

FILE_HEAD = struct.Struct("!33sc14s6s73sc")

def to_str(bytes):
	return bytes.partition(b"\0")[0].decode("uao_decode")
	
class DIR:
	def __init__(self):
		self.items = {}
		self.read_cache = set()
		self.read_fail = set()
		
	def getTitle(self, file):
		file = pathlib.Path(file)
		self.read_file(file.with_name(".DIR"))
		if file.name in self.items:
			return self.items[file.name].title
		
	def getAuthor(self, file):
		file = pathlib.Path(file)
		self.read_file(file.with_name(".DIR"))
		if file.name in self.items:
			return self.items[file.name].owner
		
	def getTime(self, file):
		file = pathlib.Path(file)
		self.read_file(file.with_name(".DIR"))
		if file.name in self.items:
			return self.items[file.name].date
			
	def read_file(self, file, throw_error=False):
		file = pathlib.Path(file).resolve()
		if str(file) in self.read_cache:
			return
		if str(file) in self.read_fail and not throw_error:
			return
		try:
			content = file.read_bytes()
		except OSError:
			self.read_fail.add(str(file))
			if throw_error:
				raise
			return
		self.read_cache.add(str(file))
				
		for args in FILE_HEAD.iter_unpack(content):
			filename, savemode, owner, date, title, filemode = (
				to_str(strip_color(i)) for i in args)
			self.items[filename] = Item(owner, date, title)

class Item:
	def __init__(self, owner, date, title):
		self.owner = owner
		month, sep, day = date.partition("/")
		self.date = datetime.datetime.today().replace(month=int(month), day=int(day))
		self.title = title
