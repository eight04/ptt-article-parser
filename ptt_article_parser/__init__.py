#! python3

import re, datetime

from . import uao_decode
from .version import __version__

ENCODING = "uao_decode"

def decode_func(b):
	return b.decode(ENCODING)

class NoMatch(Exception):
	pass

class Article:
	def __init__(self, source):
		"""Give source Bytes to build an article"""
		self.original_source = source
		
		# remove ansi, encode to string
		self.source = re.sub(br"\x1b\[[\d;]*m", br"", source).decode(ENCODING)
		
		# get headers
		match = self.finditer(r'作者:?\s*(.+?) *(?:看板:?\s*([a-zA-Z0-9-_]+) *)?\n\s*標題:?\s*(.+?) *\n\s*時間:?\s*(\w+ \w+  ?\d+ \d+:\d+:\d+ \d+) *\n?(?:─+ *\r?\n?)?', self.source)
		if match:
			self.headers = [Header(*m.groups(), m.start, m.end) for m in match]
		
		# get forward heads
		match = re.finditer(r"※ \[本文轉錄自\s*([a-zA-Z0-9-_]+)\s*看板\s*(#[a-zA-Z0-9-_]{8})\s*\] *\n?", self.source)
		if match:
			self.forward_heads = [ForwardHead(*m.groups(), m.start(), m.end()) for m in match]
		
		# get forward foot
		match = re.finditer(r"※ 發信站: 批踢踢實業坊\(ptt\.cc\)\s*※ 轉錄者: (\w+) \((\d+.\d+.\d+.\d+)\),\s*(?:時間:\s*)?(\d+/\d+/\d+ \d+:\d+:\d+) *\n?", self.source)
		if match:
			self.forward_foots = [ForwardFoot(*m.groups(), m.start(), m.end()) for m in match]
				
		# get sign
		match = re.search(r"※ 發信站: 批踢踢實業坊\(ptt\.cc\), 來自: (\d+\.\d+\.\d+\.\d+) *\n※ 文章網址: (http\w+) *\n?", getattr(self, "body_source", self.source))
		if match:
			self.sign = Sign(*match.groups())
			if hasattr(self, "body_source"):
				self.body_source = 
				
		# get first push
		
		
		if not hasattr(self, "body_source"):
			self.body_source = self.source
			
		# get forward head
		match = re.search(r"※ \[本文轉錄自\s*([a-zA-Z0-9-_]+)\s*看板\s*(#[a-zA-Z0-9-_]{8})\s*\] *\n?", self.body_source)
			
		# get url
		match = re.search(r"※ 文章網址: (http\S+)", self.source)
		if match:
			self.url = match.group(1)
			if not body_end:
				body_end = match.start()
		
		# get ip
			
		# get body
		
		# get edits
	
	def search(self, *patterns):
		for pattern in patterns:
			matcher = re.compile(pattern, re.MULTILINE)
			match = matcher.search(self.source)
			if match:
				if matcher.groups > 1:
					return match.groups()
				return match.group(1)
		if matcher.groups > 1:
			return [None] * matcher.groups
		return None

	def getTitle(self):
		"""Get the title"""
		return self.title

	def getAuthor(self):
		"""Get the author"""
		return self.author

	def getTime(self):
		"""Get post time"""
		return self.time

	def getBoard(self):
		"""Get board name"""
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
		
class ForwardHead:
	def __init__(self, board, pid, start, end):
		self.board = board
		self.title = title
		self.start = start
		self.end = end
		
class Header:
	def __init__(self, author, board, title, time, start, end):
		self.author = author
		self.board = board
		self.title = title
		self.time = datetime.datetime.strptime(time, "%a %b %d %H:%M:%S %Y")
		self.start = start
		self.end = end

class Sign:
	def __init__(self, ip, url=None):
		self.ip = ip
		self.url = url

class ForwardFoot:
	def __init__(self, author, ip, time, start, end):
		self.author = author
		self.ip = ip
		self.time = datetime.datetime.strptime(time, "%m/%d/%Y %H:%M:%S")
		self.start = start
		self.end = end

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
