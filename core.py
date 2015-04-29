#! python3

import re, time, uao_decode

ENCODING = "uao_decode"

class Article:
	def __init__(self, source):
		"""Give source Bytes to build an article"""
		self.originalSource = source
		
		# Get clean source
		self.source = re.sub(br"\x1b\[[\d;]*m", br"", source)
		
		class NoMatch(Exception):
			pass
		
		def matchPhase(pattern):
			match = re.search(pattern, self.source)
			if not match:
				raise NoMatch
			self.source = (self.source[:match.start()] + 
					self.source[match.end():])
			return [x.decode(ENCODING) for x in match.groups()]
				
		
		# Get author and board name
		try:
			self.author, self.board = matchPhase(
				br"\xa7@\xaa\xcc:?\s*(.+?)\s*\xac\xdd\xaaO[: ]\s*([^\s]+)"
			)
		except NoMatch:
			try:
				self.author, = matchPhase(
					br"\xa7@\xaa\xcc[: ]\s*(.+?)\s*(?:\n|$)"
				)
			except NoMatch:
				pass
		
		# Get title
		try:
			self.title, = matchPhase(br"\xbc\xd0\xc3D[: ]\s*(.+?)\s*(?:\n|$)")
		except NoMatch:
			pass
			
		# Get time
		try:
			self.time, = matchPhase(br"\xae\xc9\xb6\xa1[: ]\s*(.+?)\s*(?:\n|$)")
		except NoMatch:
			pass
		else:
			self.time = time.strptime(self.time)
		
	def getTitle(self):
		"""Get the title"""
		return getattr(self, "title", None)
		
	def getAuthor(self):
		"""Get the author"""
		return getattr(self, "author", None)
		
	def getTime(self):
		"""Get post time"""
		return getattr(self, "time", None)
		
	def getBoard(self):
		"""Get board name"""
		return getattr(self, "board", None)
		
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
		