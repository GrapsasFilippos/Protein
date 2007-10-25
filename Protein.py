#===========================
# Grapsas Filippos
# GPLv2 License
#===========================

import karamba, commands, re, sys, os
from xml.dom import minidom

from ItSettings import ItSettings
from ItTheme import ItTheme
from ItLoadTheme1e1 import ItLoadTheme1
from ItLoadTheme1_1 import ItLoadTheme1_1
from ItLoadTheme1_1_1 import ItLoadTheme1_1_1

class CsModeTeam:
	LLTeamName = None
	LLScore = None
	LLWUs = None
	LLRank = None
	LLMembers = None
	LLTeamNumber = None
	
	LTTeamName = None
	LTScore = None
	LTWUs = None
	LTRank = None
	LTMembers = None
	LTTeamNumber = None
	
	def make(self, widget):
		self.craft(widget)
		self.hide(widget)
	
	def show(self, widget):
		karamba.showText(widget, self.LLTeamName)
		karamba.showText(widget, self.LLScore)
		karamba.showText(widget, self.LLWUs)
		karamba.showText(widget, self.LLRank)
		karamba.showText(widget, self.LLMembers)
		karamba.showText(widget, self.LTTeamName)
		karamba.showText(widget, self.LTScore)
		karamba.showText(widget, self.LTWUs)
		karamba.showText(widget, self.LTRank)
		karamba.showText(widget, self.LTMembers)
		karamba.showText(widget, self.LLTeamNumber)
		karamba.showText(widget, self.LTTeamNumber)
		
	def hide(self, widget):
		karamba.hideText(widget, self.LLTeamName)
		karamba.hideText(widget, self.LLScore)
		karamba.hideText(widget, self.LLWUs)
		karamba.hideText(widget, self.LLRank)
		karamba.hideText(widget, self.LLMembers)
		karamba.hideText(widget, self.LTTeamName)
		karamba.hideText(widget, self.LTScore)
		karamba.hideText(widget, self.LTWUs)
		karamba.hideText(widget, self.LTRank)
		karamba.hideText(widget, self.LTMembers)
		karamba.hideText(widget, self.LLTeamNumber)
		karamba.hideText(widget, self.LTTeamNumber)

	def craft(self, widget):
		self.LLTeamName = CMain.CTools.createText(widget, CMain.ItTheme.TeamMode.LTeamName, 0)
		self.LTTeamName = CMain.CTools.createText(widget, CMain.ItTheme.TeamMode.TTeamName, 0)
		self.LLScore = CMain.CTools.createText(widget, CMain.ItTheme.TeamMode.LScore, 0)
		self.LTScore = CMain.CTools.createText(widget, CMain.ItTheme.TeamMode.TScore, 0)
		self.LLWUs = CMain.CTools.createText(widget, CMain.ItTheme.TeamMode.LWUs, 0)
		self.LTWUs = CMain.CTools.createText(widget, CMain.ItTheme.TeamMode.TWUs, 0)
		self.LLRank = CMain.CTools.createText(widget, CMain.ItTheme.TeamMode.LRank, 0)
		self.LTRank = CMain.CTools.createText(widget, CMain.ItTheme.TeamMode.TRank, 0)
		self.LLMembers = CMain.CTools.createText(widget, CMain.ItTheme.TeamMode.LMembers, 0)
		self.LTMembers = CMain.CTools.createText(widget, CMain.ItTheme.TeamMode.TMembers, 0)
		self.LLTeamNumber = CMain.CTools.createText(widget, CMain.ItTheme.TeamMode.LTeamNumber, 0)
		self.LTTeamNumber = CMain.CTools.createText(widget, CMain.ItTheme.TeamMode.TTeamNumber, 0)
	
	def refresh(self, widget):
		karamba.changeText(widget, self.LTTeamName, CMain.CStats.TeamName)
		karamba.changeText(widget, self.LTScore, CMain.CStats.TeamPoints)
		karamba.changeText(widget, self.LTWUs, CMain.CStats.TeamWUs)
		karamba.changeText(widget, self.LTRank, CMain.CStats.TeamRank)
		karamba.changeText(widget, self.LTMembers, CMain.CStats.TeamMembers)
		karamba.changeText(widget, self.LTTeamNumber, CMain.CStats.TeamNumber)

class CsModeSelf:
	LLUsername = None
	LLScore = None
	LLWUs = None
	LLTeamRank = None
	LLRank = None
	
	LTUsername = None
	LTScore = None
	LTWUs = None
	LTTeamRank = None
	LTRank = None
	
	def make(self, widget):
		self.craft(widget)
		self.hide(widget)
	
	def show(self, widget):
		karamba.showText(widget, self.LLUsername)
		karamba.showText(widget, self.LLScore)
		karamba.showText(widget, self.LLWUs)
		karamba.showText(widget, self.LLTeamRank)
		karamba.showText(widget, self.LLRank)
		karamba.showText(widget, self.LTUsername)
		karamba.showText(widget, self.LTScore)
		karamba.showText(widget, self.LTWUs)
		karamba.showText(widget, self.LTTeamRank)
		karamba.showText(widget, self.LTRank)
	
	def hide(self, widget):
		karamba.hideText(widget, self.LLUsername)
		karamba.hideText(widget, self.LLScore)
		karamba.hideText(widget, self.LLWUs)
		karamba.hideText(widget, self.LLTeamRank)
		karamba.hideText(widget, self.LLRank)
		karamba.hideText(widget, self.LTUsername)
		karamba.hideText(widget, self.LTScore)
		karamba.hideText(widget, self.LTWUs)
		karamba.hideText(widget, self.LTTeamRank)
		karamba.hideText(widget, self.LTRank)
	
	def craft(self, widget):
		self.LLUsername = CMain.CTools.createText(widget, CMain.ItTheme.SelfMode.LUsername, 0)
		self.LTUsername = CMain.CTools.createText(widget, CMain.ItTheme.SelfMode.TUsername, 0)
		self.LLScore = CMain.CTools.createText(widget, CMain.ItTheme.SelfMode.LScore, 0)
		self.LTScore = CMain.CTools.createText(widget, CMain.ItTheme.SelfMode.TScore, 0)
		self.LLWUs = CMain.CTools.createText(widget, CMain.ItTheme.SelfMode.LWUs, 0)
		self.LTWUs = CMain.CTools.createText(widget, CMain.ItTheme.SelfMode.TWUs, 0)
		self.LLTeamRank = CMain.CTools.createText(widget, CMain.ItTheme.SelfMode.LTeamRank, 0)
		self.LTTeamRank = CMain.CTools.createText(widget, CMain.ItTheme.SelfMode.TTeamRank, 0)
		self.LLRank = CMain.CTools.createText(widget, CMain.ItTheme.SelfMode.LRank, 0)
		self.LTRank = CMain.CTools.createText(widget, CMain.ItTheme.SelfMode.TRank, 0)
	
	def refresh(self, widget):
		karamba.changeText(widget, self.LTUsername, CMain.CStats.UserName)
		karamba.changeText(widget, self.LTScore, CMain.CStats.UserPoints)
		karamba.changeText(widget, self.LTWUs, CMain.CStats.UserWUs)
		karamba.changeText(widget, self.LTTeamRank, CMain.CStats.UserTeamRank)
		karamba.changeText(widget, self.LTRank, CMain.CStats.UserRank)

class CsModeProgress:
	LLSince = None
	LLDue = None
	LLPoints = None
	LLName = None
	LLPercentage = None
	LLRemaining = None
	LLRunning = None
	LLSerial = None
	
	LTSince = None
	LTDue = None
	LTPoints = None
	LTName = None
	LTPercentage = None
	LTRemaining = None
	LTRunning = None
	LTSerial = None
	
	BBProgress = None
	BLProgress = None
	
	def make(self, widget):
		self.craft(widget)
		self.hide(widget)
	
	def show(self, widget):
		karamba.showImage(widget, self.BBProgress)
		karamba.showBar(widget, self.BLProgress)
		karamba.showText(widget, self.LLSince)
		karamba.showText(widget, self.LLDue)
		karamba.showText(widget, self.LLPoints)
		karamba.showText(widget, self.LLName)
		karamba.showText(widget, self.LLPercentage)
		karamba.showText(widget, self.LTSince)
		karamba.showText(widget, self.LTDue)
		karamba.showText(widget, self.LTPoints)
		karamba.showText(widget, self.LTName)
		karamba.showText(widget, self.LTPercentage)
		karamba.showText(widget, self.LLRemaining)
		karamba.showText(widget, self.LLRunning)
		karamba.showText(widget, self.LTRemaining)
		karamba.showText(widget, self.LTRunning)
		karamba.showText(widget, self.LLSerial)
		karamba.showText(widget, self.LTSerial)
		
	def hide(self, widget):
		karamba.hideImage(widget, self.BBProgress)
		karamba.hideBar(widget, self.BLProgress)
		karamba.hideText(widget, self.LLSince)
		karamba.hideText(widget, self.LLDue)
		karamba.hideText(widget, self.LLPoints)
		karamba.hideText(widget, self.LLName)
		karamba.hideText(widget, self.LLPercentage)
		karamba.hideText(widget, self.LTSince)
		karamba.hideText(widget, self.LTDue)
		karamba.hideText(widget, self.LTPoints)
		karamba.hideText(widget, self.LTName)
		karamba.hideText(widget, self.LTPercentage)
		karamba.hideText(widget, self.LLRemaining)
		karamba.hideText(widget, self.LLRunning)
		karamba.hideText(widget, self.LTRemaining)
		karamba.hideText(widget, self.LTRunning)
		karamba.hideText(widget, self.LLSerial)
		karamba.hideText(widget, self.LTSerial)

	def craft(self, widget):
		self.LLPercentage = CMain.CTools.createText(widget, CMain.ItTheme.ProgressMode.LPercentage, 0)
		self.LTPercentage = CMain.CTools.createText(widget, CMain.ItTheme.ProgressMode.TPercentage, 0)
		self.LLRemaining = CMain.CTools.createText(widget, CMain.ItTheme.ProgressMode.LRemaining, 0)
		self.LTRemaining = CMain.CTools.createText(widget, CMain.ItTheme.ProgressMode.TRemaining, 0)
		self.LLPoints = CMain.CTools.createText(widget, CMain.ItTheme.ProgressMode.LPoints, 0)
		self.LTPoints = CMain.CTools.createText(widget, CMain.ItTheme.ProgressMode.TPoints, 0)
		self.LLRunning = CMain.CTools.createText(widget, CMain.ItTheme.ProgressMode.LRunning, 0)
		self.LTRunning = CMain.CTools.createText(widget, CMain.ItTheme.ProgressMode.TRunning, 0)
		self.LLSince = CMain.CTools.createText(widget, CMain.ItTheme.ProgressMode.LSince, 0)
		self.LTSince = CMain.CTools.createText(widget, CMain.ItTheme.ProgressMode.TSince, 0)
		self.LLDue = CMain.CTools.createText(widget, CMain.ItTheme.ProgressMode.LDue, 0)
		self.LTDue = CMain.CTools.createText(widget, CMain.ItTheme.ProgressMode.TDue, 0)
		self.LLName = CMain.CTools.createText(widget, CMain.ItTheme.ProgressMode.LName, 0)
		self.LTName = CMain.CTools.createText(widget, CMain.ItTheme.ProgressMode.TName, 0)
		self.LLSerial = CMain.CTools.createText(widget, CMain.ItTheme.ProgressMode.LSerial, 0)
		self.LTSerial = CMain.CTools.createText(widget, CMain.ItTheme.ProgressMode.TSerial, 0)
		self.BBProgress = karamba.createImage(widget, CMain.ItTheme.ProgressMode.BProgress.x, CMain.ItTheme.ProgressMode.BProgress.y, CMain.ItSettings.Theme.ImagePath + CMain.ItTheme.ProgressMode.BProgress.v)
		self.BLProgress = karamba.createBar(widget, CMain.ItTheme.ProgressMode.LProgress.x, CMain.ItTheme.ProgressMode.LProgress.y, CMain.ItTheme.ProgressMode.LProgress.w, CMain.ItTheme.ProgressMode.LProgress.h, CMain.ItSettings.Theme.ImagePath + CMain.ItTheme.ProgressMode.LProgress.v)
		karamba.setBarValue(widget, self.BLProgress, 0)
	
	def refresh(self, widget):
		karamba.changeText(widget, self.LTPercentage, (CMain.CStats.ProteinProgress + '%'))
		karamba.changeText(widget, self.LTPoints, CMain.CStats.ProteinPoints)
		karamba.changeText(widget, self.LTName, CMain.CStats.ProteinName)
		karamba.changeText(widget, self.LTSince, CMain.CStats.ProteinSince)
		karamba.changeText(widget, self.LTDue, CMain.CStats.ProteineDue)
		karamba.changeText(widget, self.LTRemaining, CMain.CStats.ProteinRemainingTime)
		karamba.changeText(widget, self.LTRunning, CMain.CStats.ProteinRunningTime)
		karamba.changeText(widget, self.LTSerial, CMain.CStats.ProteinSerial)
		karamba.setBarValue(widget, self.BLProgress, int(CMain.CStats.ProteinProgress))

class CsStats:
	UserName = None
	UserPoints = None
	UserWUs = None
	UserTeamRank = None
	UserRank = None
	TeamNumber = None
	TeamRank = None
	TeamPoints = None
	TeamWUs = None
	TeamName = None
	TeamMembers = None
	ProteinName = None
	ProteinPoints = None
	ProteinProgress = None
	ProteinSince = None
	ProteineDue = None
	ProteinSerial = None
	ProteinRunningTime = None
	ProteinRemainingTime = None
	
	def refresh(self, widget):
		if CMain.CEngine.EngineFlag:
			Stats = commands.getoutput(CMain.ItSettings.Engine.path + ' ' + CMain.ItSettings.FAHClient.path + ' username team points wu userTeamRank globalRank protein proteinValue proteinProgress proteinSince proteinDue teamRank teamPoints teamWUs teamName proteinSerial runningTime remainingTime teamMembers')
			Stats = re.split('\n', Stats)
			self.UserName = Stats[0]
			self.TeamNumber = Stats[1]
			self.UserPoints = Stats[2]
			self.UserWUs = Stats[3]
			self.UserTeamRank = Stats[4]
			self.UserRank = Stats[5]
			self.ProteinName = Stats[6]
			self.ProteinPoints = Stats[7]
			self.ProteinProgress = re.findall('[0-9]{1,3}', Stats[8])[0]
			self.ProteinSince = Stats[9]
			self.ProteineDue = Stats[10]
			self.TeamRank = Stats[11]
			self.TeamPoints = Stats[12]
			self.TeamWUs = Stats[13]
			self.TeamName = Stats[14]
			self.ProteinSerial = Stats[15]
			self.ProteinRunningTime = Stats[16]
			self.ProteinRemainingTime = Stats[17]
			self.TeamMembers = Stats[18]
			
			CMain.CModeProgress.refresh(widget)
			CMain.CModeSelf.refresh(widget)
			CMain.CModeTeam.refresh(widget)
		else:
			print "Stats refresh disabled"

class CsMenu_b:
	IMenu = None
	LTitle = None
	IBg = None
	
	Mode = 0
	
	def changeMode(self, widget):
		self.Mode += 1
		if self.Mode > 3:
			self.Mode = 1
		
		if self.Mode == 1:
			CMain.CItems.hide(widget)
			CMain.CModeProgress.show(widget)
			karamba.changeText(widget, self.LTitle, CMain.ItTheme.Menu.LTitle.v1)
		elif self.Mode == 2:
			CMain.CItems.hide(widget)
			CMain.CModeSelf.show(widget)
			karamba.changeText(widget, self.LTitle, CMain.ItTheme.Menu.LTitle.v2)
		elif self.Mode == 3:
			CMain.CItems.hide(widget)
			CMain.CModeTeam.show(widget)
			karamba.changeText(widget, self.LTitle, CMain.ItTheme.Menu.LTitle.v3)
	
	def make(self, widget):
		self.craft(widget, 0, 20)
		self.hide(widget)
	
	def show(self, widget):
		karamba.showImage(widget, self.IBg)
		karamba.showImage(widget, self.IMenu)
		karamba.showText(widget, self.LTitle)
		self.changeMode(widget)
		
	def hide(self, widget):
		karamba.hideImage(widget, self.IBg)
		karamba.hideImage(widget, self.IMenu)
		karamba.hideText(widget, self.LTitle)

	def craft(self, widget, x, y):
		self.IBg = karamba.createImage(widget, CMain.ItTheme.Menu.IBG.x, CMain.ItTheme.Menu.IBG.y, CMain.ItSettings.Theme.ImagePath + CMain.ItTheme.Menu.IBG.v)
		self.IMenu = karamba.createImage(widget, CMain.ItTheme.Menu.IMenu.x, CMain.ItTheme.Menu.IMenu.y, CMain.ItSettings.Theme.ImagePath + CMain.ItTheme.Menu.IMenu.v)
		karamba.attachClickArea(widget, self.IMenu)
		self.LTitle = CMain.CTools.createText(widget, CMain.ItTheme.Menu.LTitle, 1)

class CsMenu_c:
	IBg = None
	
	def showStats(self, widget):
		CMain.CModeProgress.show(widget)
		CMain.CModeSelf.show(widget)
		CMain.CModeTeam.show(widget)
	
	def make(self, widget):
		self.craft(widget, 0, 20)
		self.hide(widget)
	
	def show(self, widget):
		karamba.showImage(widget, self.IBg)
		self.showStats(widget)
		
	def hide(self, widget):
		karamba.hideImage(widget, self.IBg)

	def craft(self, widget, x, y):
		self.IBg = karamba.createImage(widget, CMain.ItTheme.Menu.IBG.x, CMain.ItTheme.Menu.IBG.y, CMain.ItSettings.Theme.ImagePath + CMain.ItTheme.Menu.IBG.v)

class CsThemes:
	ThemesList = []
	ThemeAuthor = []
	ThemeName = None
	
	def getTheme(self, ThemeName):
		flag = True
		TVersion = None
		
		try: xmldoc = minidom.parse(CMain.ItSettings.Theme.Themes.path + ThemeName + '/config.xml')
		except: flag = False
		
		if flag:
			ETheme = xmldoc.getElementsByTagName('Theme')
			EMode = xmldoc.getElementsByTagName('Mode')
			for n in EMode:
				if n.attributes["id"].value == 'Theme':
					TVersion = n.getElementsByTagName('version')[0].firstChild.data
					break
			
			if TVersion == '1': ItLoadTheme = ItLoadTheme1()
			elif TVersion == '1.1': ItLoadTheme = ItLoadTheme1_1()
			elif TVersion == '1.1.1': ItLoadTheme = ItLoadTheme1_1_1()
			return ItLoadTheme.LoadTheme(xmldoc)
		else:
			return flag
	
	def loadList(self):
		ls = os.listdir(CMain.ItSettings.Theme.Themes.path)
		for x in ls:
			try:
				f = open(CMain.ItSettings.Theme.Themes.path + x + '/config.xml')
			except:
				f = 0
			if f:
				f.close()
				self.ThemeAuthor.append(self.getTheme(x).Author.author)
				self.ThemesList.append(x)
	
	def loadTheme(self, ThemeName):
		TVersion = None
		
		try:
			xmldoc = minidom.parse(CMain.ItSettings.Theme.Themes.path + ThemeName + '/config.xml')
		except:
			ThemeName = self.ThemesList[0]
			xmldoc = minidom.parse(CMain.ItSettings.Theme.Themes.path + ThemeName + '/config.xml')
		
		CMain.ItSettings.Theme.ImagePath = CMain.ItSettings.Theme.path + 'themes/' + ThemeName + '/'
		self.ThemeName = ThemeName
		
		ETheme = xmldoc.getElementsByTagName('Theme')
		EMode = xmldoc.getElementsByTagName('Mode')
		for n in EMode:
			if n.attributes["id"].value == 'Theme':
				TVersion = n.getElementsByTagName('version')[0].firstChild.data
				break
		
		if TVersion == '1':
			ItLoadTheme = ItLoadTheme1()
		elif TVersion == '1.1':
			ItLoadTheme = ItLoadTheme1_1()
		elif TVersion == '1.1.1':
			ItLoadTheme = ItLoadTheme1_1_1()
		CMain.ItTheme = ItLoadTheme.LoadTheme(xmldoc)
		
		if CMain.ItTheme.Menu.Style == 'b':
			CMain.CMenu = CsMenu_b()
		elif CMain.ItTheme.Menu.Style == 'c':
			CMain.CMenu = CsMenu_c()
		
		#print CMain.ItTheme.ProgressMode.TPercentage.align

class CsConfig:
	def craft(self, widget):
		karamba.addMenuConfigOption(widget, "settings", "Settings")
		karamba.addMenuConfigOption(widget, "564897981312", "--------")
		karamba.setMenuConfigOption(widget, "settings", False)
		karamba.setMenuConfigOption(widget, "564897981312", False)
		
		x = CMain.CThemes.ThemesList
		y = CMain.CThemes.ThemeAuthor
		for i in range(0, len(CMain.CThemes.ThemesList)):
			karamba.addMenuConfigOption(widget, x[i], x[i] + ', ' + y[i])
		self.CheckUp(widget)
	
	def CheckUp(self, widget):
		if karamba.readConfigEntry(widget, 'bg') == None:
			karamba.writeConfigEntry(widget, 'bg', CMain.CThemes.ThemeName)
		for x in CMain.CThemes.ThemesList:
			karamba.setMenuConfigOption(widget, x, False)
		karamba.setMenuConfigOption(widget, karamba.readConfigEntry(widget, 'bg'), True)
		karamba.redrawWidget(widget)
	
	def OptionClicked(self, widget, key, value):
		if (key == "settings") or (key == "564897981312"):
			karamba.setMenuConfigOption(widget, key, False)
			if key == "settings":
				CMain.CSettings.changeSettings(widget)
		else:
			for x in CMain.CThemes.ThemesList:
				karamba.setMenuConfigOption(widget, x, False)
			karamba.setMenuConfigOption(widget, key, True)
			karamba.writeConfigEntry(widget, 'bg', key)
			karamba.reloadTheme(widget)

class CsItems:
	def make(self, widget):
		CMain.CMenu.make(widget)
		CMain.CModeProgress.make(widget)
		CMain.CModeSelf.make(widget)
		CMain.CModeTeam.make(widget)
		CMain.CConfig.craft(widget)
	
	def hide(self, widget):
		CMain.CModeProgress.hide(widget)
		CMain.CModeSelf.hide(widget)
		CMain.CModeTeam.hide(widget)
	
	def show(self, widget):
		CMain.CModeProgress.show(widget)
		CMain.CModeSelf.show(widget)
		Cmain.CModeTeam.show(widget)

class CsEngine:
	EngineFlag = None
	
	def Test(self):
		flag = True
		
		try:
			f = open(CMain.ItSettings.Engine.path)
			f.close()
		except:
			print 'What\'s this?: ' + CMain.ItSettings.Engine.path
			flag = False
		
		cmd = commands.getoutput(CMain.ItSettings.Engine.path + ' ' + CMain.ItSettings.FAHClient.path + ' proteinProgress')
		if cmd == 'Error':
			print CMain.ItSettings.FAHClient.path + ': Problem with Folding@Home client directory'
			flag = False
		elif not re.findall('.{1,3}%', cmd):
			print 'This is Engine for me?: ' + CMain.ItSettings.Engine.path
			flag = False
		
		self.EngineFlag = flag
		return flag

class CsSettings:
	def init(self, widget):
		CMain.ItSettings.Theme.path = karamba.getThemePath(widget)
		
		#print karamba.readConfigEntry(widget, "FAHPath")
		CMain.ItSettings.FAHClient.path = karamba.readConfigEntry(widget, "FAHPath")
		CMain.ItSettings.Engine.path = karamba.readConfigEntry(widget, "EnginePath")
		CMain.ItSettings.Theme.Themes.path = karamba.readConfigEntry(widget, "ThemesPath")
		
		if CMain.ItSettings.FAHClient.path == None:
			CMain.ItSettings.FAHClient.path = ""
			karamba.writeConfigEntry(widget, "FAHPath", CMain.ItSettings.FAHClient.path)
		if CMain.ItSettings.Engine.path == None:
			CMain.ItSettings.Engine.path = "default"
			karamba.writeConfigEntry(widget, "EnginePath", CMain.ItSettings.Engine.path)
		if CMain.ItSettings.Theme.Themes.path == None:
			CMain.ItSettings.Theme.Themes.path = "default"
			karamba.writeConfigEntry(widget, "ThemesPath", CMain.ItSettings.Theme.Themes.path)
		
		if CMain.ItSettings.Engine.path == "default":
			CMain.ItSettings.Engine.path = CMain.ItSettings.Theme.path + 'info'
		if CMain.ItSettings.Theme.Themes.path == "default":
			CMain.ItSettings.Theme.Themes.path = CMain.ItSettings.Theme.path + 'themes/'
		
		#print CMain.ItSettings.FAHClient.path
		
		if not CMain.CEngine.EngineFlag:
			print "FAHPath=" + CMain.ItSettings.FAHClient.path
			print "EnginePath=" + CMain.ItSettings.Engine.path
			print "ThemesPath=" + CMain.ItSettings.Theme.Themes.path
	
	def changeSettings(self, widget):
		cmd = CMain.ItSettings.Theme.path + "ProteinSettings/ProteinSettings -e " + karamba.readConfigEntry(widget, "EnginePath") + " -t " + karamba.readConfigEntry(widget, "ThemesPath")
		if CMain.ItSettings.FAHClient.path != "":
			cmd = cmd + " -f " + karamba.readConfigEntry(widget, "FAHPath")
		rPaths = re.split("\n", commands.getoutput(cmd))
		for r in rPaths:
			if re.findall("FAHPath:", r):
				FAH = re.split("FAHPath:", r)[1]
			if re.findall("ThemesPath:", r):
				Themes = re.split("ThemesPath:", r)[1]
			if re.findall("EnginePath:", r):
				Engine = re.split("EnginePath:", r)[1]
		
		if rPaths[0] != "Cansel":
			karamba.writeConfigEntry(widget, "FAHPath", FAH)
			karamba.writeConfigEntry(widget, "EnginePath", Engine)
			karamba.writeConfigEntry(widget, "ThemesPath", Themes)
			karamba.reloadTheme(widget)

class CsTools:
	def createText(self, widget, item, ClickArea):
		text = karamba.createText(widget, item.x, item.y, item.w, item.h, item.v)
		if item.f: karamba.changeTextFont(widget, text, item.f)
		if item.s: karamba.changeTextSize(widget, text, item.s)
		if item.c: karamba.changeTextColor(widget, text, item.c[0], item.c[1], item.c[2])
		if item.sw: karamba.changeTextShadow(widget, text, item.sw)
		if item.align: karamba.setTextAlign(widget, text, item.align)
		if ClickArea: karamba.attachClickArea(widget, text)
		return text

class CsMain:
	CItems        = CsItems()
	CMenu         = None
	CModeProgress = CsModeProgress()
	CModeSelf     = CsModeSelf()
	CModeTeam     = CsModeTeam()
	CStats        = CsStats()
	CSettings     = CsSettings()
	CConfig       = CsConfig()
	CEngine       = CsEngine()
	CThemes       = CsThemes()
	CTools        = CsTools()
	
	ItSettings = ItSettings()
	ItTheme = ItTheme()
	
	def __init__(self):
		pass
	
	def widgetUpdated(self, widget):
		self.CStats.refresh(widget)
		karamba.redrawWidget(widget)
	
	def menuOptionChanged(self, widget, key, value):
		self.CConfig.OptionClicked(widget, key, value)
	
	def meterClicked(self, widget, meter, button):
		if meter == self.CMenu.IMenu:
			self.CMenu.changeMode(widget)
			karamba.redrawWidget(widget)
		elif meter == self.CMenu.LTitle:
			self.widgetUpdated(widget)
	
	def initWidget(self, widget):
		self.CSettings.init(widget)
		self.CThemes.loadList()
		self.CThemes.loadTheme(karamba.readConfigEntry(widget, 'bg'))
		self.CEngine.Test()
		
		karamba.changeInterval(widget, CMain.ItTheme.Theme.interval)
		karamba.resizeWidget(widget, CMain.ItTheme.Theme.w, CMain.ItTheme.Theme.h)
		
		self.CItems.make(widget)
		self.CMenu.show(widget)
		karamba.redrawWidget(widget)
		self.CStats.refresh(widget)
		
		karamba.redrawWidget(widget)

CMain = CsMain()
def menuOptionChanged(widget, key, value):
	CMain.menuOptionChanged(widget, key, value)
def meterClicked(widget, meter, button):
	CMain.meterClicked(widget, meter, button)
def initWidget(widget):
	CMain.initWidget(widget)
def widgetUpdated(widget):
	CMain.widgetUpdated(widget)
