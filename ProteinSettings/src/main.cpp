/*===========================
       Grapsas Filippos
        GPLv2 License
===========================*/

#include <QApplication>
#include <QRegExp>

#include "window.h"


int main(int argc, char *argv[])
{
	QApplication app(argc, argv);
	
	QTextStream qout(stdout);
	QString agrument;
	bool version = 0;
	QRegExp rxV("-v");
	bool fPath = 0;
	QString FPath = "";
	QRegExp rxFPath("-f");
	bool tPath = 0;
	QString TPath = "";
	QRegExp rxTPath("-t");
	bool ePath = 0;
	QString EPath = "";
	QRegExp rxEPath("-e");
	
	
	for (int i=1; i<=argc; i++)
	{
		agrument = QCoreApplication::arguments().at((i-1));
		if (!version) {
			if (rxV.exactMatch(agrument)) {
				version = 1;
			}
		}
		if (!fPath) {
			if (rxFPath.exactMatch(agrument)) {
				FPath = QCoreApplication::arguments().at((i));
				fPath = 1;
			}
		}
		if (!tPath) {
			if (rxTPath.exactMatch(agrument)) {
				TPath = QCoreApplication::arguments().at((i));
				tPath = 1;
			}
		}
		if (!ePath) {
			if (rxEPath.exactMatch(agrument)) {
				EPath = QCoreApplication::arguments().at((i));
				ePath = 1;
			}
		}
	}
	
	if(!version)
	{
		Window window(FPath, TPath, EPath);
		window.show();
		
		return app.exec();
	}
	else {
		qout << "\n ProteinSettings, version 1\n Copyright (C) 2007 Grapsas Filippos\n\n";
	}
}
