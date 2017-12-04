import datetime
import pathlib
import struct
from . import uao_decode

FILE_HEAD = struct.Struct("!33sc14s6s73sc")

def to_str(bytes):
	return bytes.partition(b"\0")[0].decode("uao_decode")

class DIR:
	def __init__(self):
		self.items = {}
		
	def getTitle(self, key):
		if key in self.items:
			return self.items[key].title
		
	def getAuthor(self, key):
		if key in self.items:
			return self.items[key].owner
		
	def getTime(self, key):
		if key in self.items:
			return self.items[key].date
	
	@classmethod
	def from_file(cls, file):
		file = pathlib.Path(file).read_bytes()
		dir = cls()
		for args in FILE_HEAD.iter_unpack(file):
			filename, savemode, owner, date, title, filemode = (
				to_str(i) for i in args)
			dir.items[filename] = Item(owner, date, title)
		return dir

class Item:
	def __init__(self, owner, date, title):
		self.owner = owner
		month, sep, day = date.partition("/")
		self.date = datetime.datetime.today().replace(month=int(month), day=int(day))
		self.title = title
