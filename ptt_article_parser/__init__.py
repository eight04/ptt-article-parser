#! python3

import re, datetime

from . import uao_decode
from .version import __version__

ENCODING = "uao_decode"

class NoMatch(Exception):
	pass

class Article:
	def __init__(self, source):
		"""Give source Bytes to build an article"""
		self.originalSource = source
		self.source = re.sub(br"\x1b\[[\d;]*m", br"", source)
	
	def search(self, *patterns):
		for pattern in patterns:
			match = re.search(pattern, self.source, re.MULTILINE)
			if match:
				return match.group(1).decode(ENCODING)
		return None

	def getTitle(self):
		"""Get the title"""
		if not hasattr(self, "title"):
			self.title = self.search(
				br"\xbc\xd0\xc3D[: ]\s?(.+?)\s*$"
			)
		return self.title

	def getAuthor(self):
		"""Get the author"""
		if not hasattr(self, "author"):
			self.author = self.search(
				br"\xa7@\xaa\xcc:?\s*?(.+?)\s*?(?:\xac\xdd\xaaO|\xaf\xb8\xa4\xba|$)",
				br"\xa1\xb0 \xbds\xbf\xe8:\s*(\w+)"
			)
		return self.author

	def getTime(self):
		"""Get post time"""
		if not hasattr(self, "time"):
			for pattern, format in ((
						br"\xae\xc9\xb6\xa1[: ]\s?(\w+ \w+  ?\d+ \d+:\d+:\d+ \d+)",
						"%a %b %d %H:%M:%S %Y"
					),(
						b'\xa1\xb0 \xbds\xbf\xe8:.+?, (\\d{2}/\\d{2}/\\d{4} \\d{2}:\\d{2}:\\d{2})',
						"%m/%d/%Y %H:%M:%S"
					)):
				self.time = self.search(pattern)
				if self.time:
					self.time = datetime.datetime.strptime(self.time, format)
					break
		return self.time

	def getBoard(self):
		"""Get board name"""
		if not hasattr(self, "board"):
			self.board = self.search(
				br"(?:\xac\xdd\xaaO|\xaf\xb8\xa4\xba)[: ]\s?(\S+)",
				b'\xa1\xb0 \xa4\xe5\xb3\xb9\xba\xf4\xa7}: https://www\\.ptt\\.cc/bbs/([^/]+)'
			)
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
