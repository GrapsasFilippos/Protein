#===========================
# Grapsas Filippos
# GPLv2 License
#===========================

import re

class ItItem:
	x = None
	y = None
	w = None
	h = None
	v = None
	c = [None, None, None]
	f = None
	s = None
	sw = None
	align = None
	
	def format(self):
		if self.x == 'None': self.x = None
		if self.y == 'None': self.y = None
		if self.w == 'None': self.w = None
		if self.h == 'None': self.h = None
		if self.v == 'None': self.v = None
		if self.c[1] == 'None': self.c = [None, None, None]
		if self.f == 'None': self.f = None
		if self.s == 'None': self.s = None
		if self.sw == 'None': self.sw = None
		if self.align == 'None': self.align = None
		
		if self.x != None: self.x = int(self.x)
		if self.y != None: self.y = int(self.y)
		if self.w != None: self.w = int(self.w)
		if self.h != None: self.h = int(self.h)
		if self.s != None: self.s = int(self.s)
		if self.sw != None: self.sw = int(self.sw)
		if self.c[0] == 'new':
			print self.c
			c = re.findall('[0-9]{1,3}', self.c[1])
			self.c = [int(c[0]), int(c[1]), int(c[2])]
		if self.f == None: self.f = ItTheme.Theme.f
		if self.s == None: self.s = ItTheme.Theme.s
		if self.c[0] == None: self.c = ItTheme.Theme.c
		if self.sw == None: self.sw = ItTheme.Theme.sw
	
	def setFromXML(self, n):
		try: self.x = n.getElementsByTagName('x')[0].firstChild.data
		except: pass
		try: self.y = n.getElementsByTagName('y')[0].firstChild.data
		except: pass
		try: self.w = n.getElementsByTagName('w')[0].firstChild.data
		except: pass
		try: self.h = n.getElementsByTagName('h')[0].firstChild.data
		except: pass
		try: self.v = n.getElementsByTagName('v')[0].firstChild.data
		except: pass
		try: self.c = ['new', n.getElementsByTagName('c')[0].firstChild.data]
		except: pass
		try: self.f = n.getElementsByTagName('f')[0].firstChild.data
		except: pass
		try: self.s = n.getElementsByTagName('s')[0].firstChild.data
		except: pass
		try: self.sw = n.getElementsByTagName('sw')[0].firstChild.data
		except: pass
		try: self.align = n.getElementsByTagName('align')[0].firstChild.data
		except: pass
		
		self.format()

class ItTeamMode:
	LTeamName = ItItem()
	LScore = ItItem()
	LWUs = ItItem()
	LRank = ItItem()
	LMembers = ItItem()
	LTeamNumber = ItItem()
	
	TTeamName = ItItem()
	TScore = ItItem()
	TWUs = ItItem()
	TRank = ItItem()
	TMembers = ItItem()
	TTeamNumber = ItItem()

class ItSelfMode:
	LUsername = ItItem()
	LScore = ItItem()
	LWUs = ItItem()
	LTeamRank = ItItem()
	LRank = ItItem()
	
	TUsername = ItItem()
	TScore = ItItem()
	TWUs = ItItem()
	TTeamRank = ItItem()
	TRank = ItItem()

class ItProgressMode:
	LSince = ItItem()
	LDue = ItItem()
	LPoints = ItItem()
	LName = ItItem()
	LPercentage = ItItem()
	LRemaining = ItItem()
	LRunning = ItItem()
	LSerial = ItItem()
	
	TSince = ItItem()
	TDue = ItItem()
	TPoints = ItItem()
	TName = ItItem()
	TPercentage = ItItem()
	TRemaining = ItItem()
	TRunning = ItItem()
	TSerial = ItItem()
	
	BProgress = ItItem()
	LProgress = ItItem()

class ItMenu:
	IMenu = ItItem()
	IBG = ItItem()
	Style = None
	
	LTitle = ItItem()
	LTitle.v1 = None
	LTitle.v2 = None
	LTitle.v3 = None

class ItTheme:
	version = None
	w = None
	h = None
	interval = None
	f = None
	s = None
	c = [0, 0, 0]
	sw = None
	bg = None
	im = None
	pb = None
	pl = None

class ItAuthor:
	author       = None
	author_email = None
	homepage    = None
	version     = None
	license     = None

class ItTheme:
	Author = ItAuthor()
	Theme = ItTheme()
	Menu = ItMenu()
	ProgressMode = ItProgressMode()
	SelfMode = ItSelfMode()
	TeamMode = ItTeamMode()
