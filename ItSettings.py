#===========================
# Grapsas Filippos
# GPLv2 License
#===========================

class It_Engine:
	path = None

class It_FAHClient:
	path = None

class It_Themes:
	path = None

class It_Theme:
	Themes = It_Themes()
	
	path = None
	ImagesPath = None
	

class ItSettings:
	Theme = It_Theme()
	FAHClient = It_FAHClient()
	Engine = It_Engine()