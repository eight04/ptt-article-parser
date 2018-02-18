#! python3
# pylint: disable=invalid-name, line-too-long

import re, datetime

from . import uao_decode # pylint: disable=unused-import
from .__pkginfo__ import __version__

ENCODING = "uao_decode"

def strip_color(b):
	return re.sub(br"\x1b\[[\d;]*m", br"", b)

class Article:
	def __init__(self, source):
		"""Give source Bytes to build an article"""
		self.original_source = source
		
		# remove ansi, encode to string
		self.source = strip_color(source).decode(ENCODING)
		
		# get headers
		matches = re.finditer(r'作者:?\s*(.+?) *(?:看板:?\s*([a-zA-Z0-9-_]+) *)?\n\s*標題:?\s*(.+?) *\n\s*時間:?\s*(\w+ \w+  ?\d+ \d+:\d+:\d+ \d+) *\n?(?:─+ *\r?\n?)?', self.source)
		self.headers = [Header(*m.groups(), m.start, m.end) for m in matches]
		
		# get forward heads
		matches = re.finditer(r"※ \[本文轉錄自\s*([a-zA-Z0-9-_]+)\s*看板\s*(#[a-zA-Z0-9-_]{8})\s*\] *\n?", self.source)
		self.forward_heads = [ForwardHead(*m.groups(), m.start(), m.end()) for m in matches]
		
		# get forward foot
		matches = re.finditer(r"※ 發信站: 批踢踢實業坊\(ptt\.cc\)\s*※ 轉錄者: (\w+) \((\d+.\d+.\d+.\d+)\),\s*(?:時間:\s*)?(\d+/\d+/\d+ \d+:\d+:\d+) *\n?", self.source)
		self.forward_foots = [ForwardFoot(*m.groups(), m.start(), m.end()) for m in matches]
				
		# get sign
		match = re.search(r"※ 發信站: 批踢踢實業坊\(ptt\.cc\), 來自: (\d+\.\d+\.\d+\.\d+) *\n※ 文章網址: (http\S+) *\n?", self.source)
		self.sign = match and Sign(*match.groups(), match.start(), match.end())
			
		# old sign
		match = re.search(r"※ 發信站: 批踢踢實業坊\(ptt\.cc\)\n◆ From: (\d+\.\d+\.\d+\.\d+)", self.source)
		self.old_sign = match and Sign(match.group(1), None, match.start(), match.end())
				
		# get edits
		self.edits = []
		matches = re.finditer(r"※ 編輯: (\w+) \((\d+\.\d+\.\d+\.\d+)\), (\d+/\d+/\d+ \d+:\d+:\d+)", self.source)
		for match in matches:
			author, ip, time = match.groups()
			time = datetime.datetime.strptime(time, "%m/%d/%Y %H:%M:%S")
			self.edits.append(Edit(author, ip, time, match.start(), match.end()))
			
		# old edits
		self.old_edits = []
		matches = re.finditer(r"※ 編輯: (\w+)\s*來自: (\d+\.\d+\.\d+\.\d+)\s*\((\d+/\d+ \d+:\d+)\)", self.source)
		for match in matches:
			author, ip, time = match.groups()
			time = datetime.datetime.strptime(time, "%m/%d %H:%M")
			self.old_edits.append(Edit(author, ip, time, match.start(), match.end()))
	
	def getTitle(self):
		"""Get the title"""
		i = len(self.forward_heads)
		if i in self.headers:
			return self.headers[i].title
		if self.headers:
			return self.headers[0].title
		return None

	def getAuthor(self):
		"""Get the author"""
		i = len(self.forward_heads)
		if i in self.headers:
			return self.headers[i].author
		if self.headers:
			return self.headers[0].author
		if self.edits:
			return self.edits[0].author
		if self.old_edits:
			return self.old_edits[0].author
		return None

	def getTime(self):
		"""Get post time"""
		i = len(self.forward_heads)
		if i in self.headers:
			return self.headers[i].time
		if self.headers:
			return self.headers[0].time
		min_record = min(self.edits + self.forward_foots, key=lambda x: x.time, default=None)
		if min_record:
			return min_record.time
		return None

	def getBoard(self):
		"""Get board name"""
		i = len(self.forward_heads)
		if i in self.headers and self.headers[i].board:
			return self.headers[i].board
		if self.headers and self.headers[0].board:
			return self.headers[0].board
		if self.sign:
			match = re.search(r"www\.ptt\.cc/bbs/([^/]+)", self.sign.url)
			if match:
				return match.group(1)
		if self.forward_heads:
			return self.forward_heads[-1].board
		return None

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
	"""Forwarding info header"""
	def __init__(self, board, aid, start, end):
		self.board = board
		self.aid = aid
		self.start = start
		self.end = end
		
class Header:
	"""Article header"""
	def __init__(self, author, board, title, time, start, end):
		self.author = author
		self.board = board
		self.title = title
		self.time = datetime.datetime.strptime(time, "%a %b %d %H:%M:%S %Y")
		self.start = start
		self.end = end

class Sign:
	"""Article sign"""
	def __init__(self, ip, url, start, end):
		self.ip = ip
		self.url = url
		self.start = start
		self.end = end

class ForwardFoot:
	"""Forwarding info footer"""
	def __init__(self, author, ip, time, start, end):
		self.author = author
		self.ip = ip
		self.time = datetime.datetime.strptime(time, "%m/%d/%Y %H:%M:%S")
		self.start = start
		self.end = end

class Edit:
	"""Edit record"""
	def __init__(self, author, ip, time, start, end):
		"""Create edit record"""
		self.author = author
		self.ip = ip
		self.time = time
		self.start = start
		self.end = end

class Push:
	"""Push record"""
	def __init__(self, type, author, message, time):
		"""Create push record"""
		self.type = type
		self.author = author
		self.message = message
		self.time = time
