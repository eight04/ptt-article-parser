#! python3

import re, time, uao_decode

ENCODING = "uao_decode"

class Article:
	def __init__(self, source):
		"""Give source Bytes to build an article"""
		self.originalSource = source
		
		# Get clean source
		source = re.sub(br"\x1b\[[\d;]*m", br"", source)
		
		# Start parsing meta
		metaStart = None
		metaEnd = None
		
		# Get author and board name
		match = re.search(
			br"\xa7@\xaa\xcc:?\s*(.+?)\s*\xac\xdd\xaaO:?\s*([^\s]+)",
			source
		)
		if match:
			if metaStart is None:
				metaStart = match.start()
			metaEnd = match.end()
			self.author = match.group(1).decode(ENCODING)
			self.board = match.group(2).decode(ENCODING)
		else:
			# Get author
			match = re.search(
				br"\xa7@\xaa\xcc:?\s*(.+?)\s*(\n|$)",
				source
			)
			if match:
				if metaStart is None:
					metaStart = match.start()
				metaEnd = match.end()
				self.author = match.group(1).decode(ENCODING)
			
		# Get title
		match = re.search(
			br"\xbc\xd0\xc3D:?\s*(.+)",
			source
		)
		if match:
			if metaStart is None:
				metaStart = match.start()
			metaEnd = match.end()
			self.title = match.group(1).decode(ENCODING)
			
		# Get time
		match = re.search(
			br"\xae\xc9\xb6\xa1:?\s*(.+)",
			source
		)
		if match:
			if metaStart is None:
				metaStart = match.start()
			metaEnd = match.end()
			timeStr = match.group(1).decode(ENCODING)
			self.time = time.strptime(timeStr)
			
		if None not in (metaStart, metaEnd):
			source = source[:metaStart] + source[metaEnd:]
			
		self.source = source
		
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
		