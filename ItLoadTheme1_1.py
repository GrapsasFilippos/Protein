#===========================
# Grapsas Filippos
# GPLv2 License
#===========================

import re
from ItTheme import ItTheme

class ItLoadTheme1_1:
	Theme = ItTheme()
	
	def LoadTheme(self, xmldoc):
		ETheme = xmldoc.getElementsByTagName('Theme')
		
		EAuthor = xmldoc.getElementsByTagName('Author')[0]
		self.Theme.Author.author = EAuthor.getElementsByTagName('author')[0].firstChild.data
		self.Theme.Author.author_email = EAuthor.getElementsByTagName('author_email')[0].firstChild.data
		self.Theme.Author.homepage = EAuthor.getElementsByTagName('homepage')[0].firstChild.data
		self.Theme.Author.version = EAuthor.getElementsByTagName('version')[0].firstChild.data
		self.Theme.Author.license = EAuthor.getElementsByTagName('license')[0].firstChild.data
		
		EMode = xmldoc.getElementsByTagName('Mode')
		for n in EMode:
			if n.attributes["id"].value == 'Theme':
				self.Theme.Theme.version = n.getElementsByTagName('version')[0].firstChild.data
				self.Theme.Theme.w = int(n.getElementsByTagName('w')[0].firstChild.data)
				self.Theme.Theme.h = int(n.getElementsByTagName('h')[0].firstChild.data)
				self.Theme.Theme.interval = int(n.getElementsByTagName('i')[0].firstChild.data)
				self.Theme.Theme.f = n.getElementsByTagName('f')[0].firstChild.data
				c = n.getElementsByTagName('c')[0].firstChild.data
				c = re.findall('[0-9]{1,3}', c)
				self.Theme.Theme.c[0] = int(c[0])
				self.Theme.Theme.c[1] = int(c[1])
				self.Theme.Theme.c[2] = int(c[2])
				self.Theme.Theme.s = int(n.getElementsByTagName('s')[0].firstChild.data)
				self.Theme.Theme.sw = int(n.getElementsByTagName('sw')[0].firstChild.data)
			
			if n.attributes["id"].value == 'Menu':
				EItem = n.getElementsByTagName('Item')
				for j in EItem:
					at = j.attributes["id"].value
					if at == 'Title':
						self.Theme.Menu.LTitle.setFromXML(j)
						self.Theme.Menu.LTitle.v1 = j.getElementsByTagName('v1')[0].firstChild.data
						self.Theme.Menu.LTitle.v2 = j.getElementsByTagName('v2')[0].firstChild.data
						self.Theme.Menu.LTitle.v3 = j.getElementsByTagName('v3')[0].firstChild.data
						self.Theme.Menu.LTitle.v = self.Theme.Menu.LTitle.v1
					if at == 'Image': self.Theme.Menu.IMenu.setFromXML(j)
					if at == 'Background': self.Theme.Menu.IBG.setFromXML(j)
					if at == 'MenuStyle': self.Theme.Menu.Style = j.firstChild.data
			
			if n.attributes["id"].value == 'Progress':
				EItem = n.getElementsByTagName('Item')
				for j in EItem:
					at = j.attributes["id"].value
					if at == 'LSince': self.Theme.ProgressMode.LSince.setFromXML(j)
					if at == 'LDue': self.Theme.ProgressMode.LDue.setFromXML(j)
					if at == 'LPoints': self.Theme.ProgressMode.LPoints.setFromXML(j)
					if at == 'LName': self.Theme.ProgressMode.LName.setFromXML(j)
					if at == 'LPercentage': self.Theme.ProgressMode.LPercentage.setFromXML(j)
					if at == 'LRemaining': self.Theme.ProgressMode.LRemaining.setFromXML(j)
					if at == 'LRunning': self.Theme.ProgressMode.LRunning.setFromXML(j)
					if at == 'LSerial': self.Theme.ProgressMode.LSerial.setFromXML(j)
					if at == 'TSince': self.Theme.ProgressMode.TSince.setFromXML(j)
					if at == 'TDue': self.Theme.ProgressMode.TDue.setFromXML(j)
					if at == 'TPoints': self.Theme.ProgressMode.TPoints.setFromXML(j)
					if at == 'TName': self.Theme.ProgressMode.TName.setFromXML(j)
					if at == 'TPercentage': self.Theme.ProgressMode.TPercentage.setFromXML(j)
					if at == 'TRemaining': self.Theme.ProgressMode.TRemaining.setFromXML(j)
					if at == 'TRunning': self.Theme.ProgressMode.TRunning.setFromXML(j)
					if at == 'TSerial': self.Theme.ProgressMode.TSerial.setFromXML(j)
					if at == 'BProgress': self.Theme.ProgressMode.BProgress.setFromXML(j)
					if at == 'LProgress': self.Theme.ProgressMode.LProgress.setFromXML(j)
			
			if n.attributes["id"].value == 'Self':
				EItem = n.getElementsByTagName('Item')
				for j in EItem:
					at = j.attributes["id"].value
					if at == 'LUsername': self.Theme.SelfMode.LUsername.setFromXML(j)
					if at == 'TUsername': self.Theme.SelfMode.TUsername.setFromXML(j)
					if at == 'LScore': self.Theme.SelfMode.LScore.setFromXML(j)
					if at == 'TScore': self.Theme.SelfMode.TScore.setFromXML(j)
					if at == 'LWUs': self.Theme.SelfMode.LWUs.setFromXML(j)
					if at == 'TWUs': self.Theme.SelfMode.TWUs.setFromXML(j)
					if at == 'LTeamRank': self.Theme.SelfMode.LTeamRank.setFromXML(j)
					if at == 'TTeamRank': self.Theme.SelfMode.TTeamRank.setFromXML(j)
					if at == 'LRank': self.Theme.SelfMode.LRank.setFromXML(j)
					if at == 'TRank': self.Theme.SelfMode.TRank.setFromXML(j)
			
			if n.attributes["id"].value == 'Team':
				EItem = n.getElementsByTagName('Item')
				for j in EItem:
					at = j.attributes["id"].value
					if at == 'LTeamName': self.Theme.TeamMode.LTeamName.setFromXML(j)
					if at == 'TTeamName': self.Theme.TeamMode.TTeamName.setFromXML(j)
					if at == 'LScore': self.Theme.TeamMode.LScore.setFromXML(j)
					if at == 'TScore': self.Theme.TeamMode.TScore.setFromXML(j)
					if at == 'LWUs': self.Theme.TeamMode.LWUs.setFromXML(j)
					if at == 'TWUs': self.Theme.TeamMode.TWUs.setFromXML(j)
					if at == 'LRank': self.Theme.TeamMode.LRank.setFromXML(j)
					if at == 'TRank': self.Theme.TeamMode.TRank.setFromXML(j)
					if at == 'LMembers': self.Theme.TeamMode.LMembers.setFromXML(j)
					if at == 'TMembers': self.Theme.TeamMode.TMembers.setFromXML(j)
					if at == 'LTeamNumber': self.Theme.TeamMode.LTeamNumber.setFromXML(j)
					if at == 'TTeamNumber': self.Theme.TeamMode.TTeamNumber.setFromXML(j)
		return self.Theme