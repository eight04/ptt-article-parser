#! python3

import re, time, uao_decode

ENCODING = "uao_decode"

class NoMatch(Exception):
	pass

def search(pattern, text):
	"""Wrap re.search. Raise NoMatch error if no match. Return decoded text."""
	match = re.search(pattern, text)
	if not match:
		raise NoMatch
	return [x.decode(ENCODING) for x in match.groups()]

class Article:
	def __init__(self, source):
		"""Give source Bytes to build an article"""
		self.originalSource = source
		self.source = re.sub(br"\x1b\[[\d;]*m", br"", source)

	def getTitle(self):
		"""Get the title"""
		if not hasattr(self, "title"):
			try:
				self.title, = search(br"\xbc\xd0\xc3D[: ]\s*(.+?)\s*(?:\n|$)", self.source)
			except NoMatch:
				self.title = None
		return self.title

	def getAuthor(self):
		"""Get the author"""
		if not hasattr(self, "author"):
			try:
				self.author, = search(
					br"\xa7@\xaa\xcc:?\s*(.+?)\s*(?:\xac\xdd\xaaO|\xaf\xb8\xa4\xba|\n|$)",
					self.source
				)
			except NoMatch:
				self.author = None
		return self.author

	def getTime(self):
		"""Get post time"""
		if not hasattr(self, "time"):
			try:
				self.time, = search(br"\xae\xc9\xb6\xa1[: ]\s*(.+?)\s*(?:\n|$)", self.source)
			except NoMatch:
				self.time = None
			else:
				self.time = time.strptime(self.time)
		return self.time

	def getBoard(self):
		"""Get board name"""
		if not hasattr(self, "board"):
			try:
				self.board, = search(br"(?:\xac\xdd\xaaO|\xaf\xb8\xa4\xba)[: ]\s*([^\s]+)", self.source)
			except NoMatch:
				self.board = None
		return self.board

	def getBody(self):
		"""Get article body"""
		pass

	def getIP(self):
		"""Get IP address"""
		pass

	def getURL(self):
		"""Get web version url"""
		pass

	def getEdits(self):
		"""Get eddit records"""
		pass

	def getPushes(self):
		"""Get push"""
		pass



class Edit:
	def __init__(self, record, *bodies):
		"""Create edit record"""
		self.record = record
		self.bodies = bodies

	def getAuthor(self):
		"""Get author"""
		pass

	def getIP(self):
		"""Get IP address"""
		pass

	def getTime(self):
		"""Get edit time"""
		pass

class Push:
	def __init__(self, source):
		"""Create push record"""
		self.source = source

	def getType(self):
		"""Get the type of push"""
		pass

	def getUser(self):
		"""Get user"""
		pass

	def getContent(self):
		"""Get push content"""
		pass

	def getIP(self):
		"""Get IP address"""
		pass

	def getTime(self):
		"""Get time"""
		pass
