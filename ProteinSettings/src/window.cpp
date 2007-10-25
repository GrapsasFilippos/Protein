/*===========================
       Grapsas Filippos
        GPLv2 License
===========================*/

#include "window.h"


Window::Window(QString FPath, QString TPath, QString EPath, QWidget *parent) : QWidget(parent)
{
	LFAHPath = new QLabel;
	LFAHPath->setText("&F@H directory:");
	TFAHPath = new QLineEdit;
	LFAHPath->setBuddy(TFAHPath);
	TFAHPath->setText(FPath);
	BFAHPath = new QToolButton;
	BFAHPath->setText("...");
	connect(BFAHPath, SIGNAL(clicked()), this, SLOT(BrFAHPath()));
	
	LThemesPath = new QLabel;
	LThemesPath->setText("&Themes directory:");
	TThemesPath = new QLineEdit;
	LThemesPath->setBuddy(TThemesPath);
	TThemesPath->setText(TPath);
	BThemesPath = new QToolButton;
	BThemesPath->setText("...");
	connect(BThemesPath, SIGNAL(clicked()), this, SLOT(BrThemesPath()));
	
	LEnginePath = new QLabel;
	LEnginePath->setText("&Engine path:");
	TEnginePath = new QLineEdit;
	LEnginePath->setBuddy(TEnginePath);
	TEnginePath->setText(EPath);
	BEnginePath = new QToolButton;
	BEnginePath->setText("...");
	connect(BEnginePath, SIGNAL(clicked()), this, SLOT(BrEnginePath()));
	
	BOk = new QPushButton;
	BOk->setText("&OK");
	BCansel = new QPushButton;
	BCansel->setText("&Cansel");
	
	connect(BOk, SIGNAL(clicked()), this, SLOT(Save()));
	connect(BCansel, SIGNAL(clicked()), this, SLOT(mQuit()));
	
	
	LyBase = new QGridLayout;
	LyBase->addWidget(LFAHPath, 0, 0);
	LyBase->addWidget(TFAHPath, 0, 1);
	LyBase->addWidget(BFAHPath, 0, 2);
	LyBase->addWidget(LThemesPath, 1, 0);
	LyBase->addWidget(TThemesPath, 1, 1);
	LyBase->addWidget(BThemesPath, 1, 2);
	LyBase->addWidget(LEnginePath, 2, 0);
	LyBase->addWidget(TEnginePath, 2, 1);
	LyBase->addWidget(BEnginePath, 2, 2);
	GbSettings = new QGroupBox;
	GbSettings->setTitle("Settings");
	GbSettings->setLayout(LyBase);
	LyOkBar = new QHBoxLayout;
	LyOkBar->addStretch();
	LyOkBar->addWidget(BOk);
	LyOkBar->addWidget(BCansel);
	LyTop = new QVBoxLayout;
	LyTop->addWidget(GbSettings);
	LyTop->addLayout(LyOkBar);
	
	setLayout(LyTop);
}

void Window::BrFAHPath()
{
	QString directory = QFileDialog::getExistingDirectory(this, "Find Files", TFAHPath->text());
	if (!directory.isEmpty())
	{
		TFAHPath->setText(directory);
	}
}
void Window::BrThemesPath()
{
	QString directory = QFileDialog::getExistingDirectory(this, "Find Files", TThemesPath->text());
	if (!directory.isEmpty())
	{
		TThemesPath->setText(directory);
	}
}
void Window::BrEnginePath()
{
	QString directory = QFileDialog::getOpenFileName(this, "Find Files", TEnginePath->text());
	if (!directory.isEmpty())
	{
		TEnginePath->setText(directory);
	}
}
void Window::Save()
{
	QTextStream qout(stdout);
	qout << "FAHPath:" << TFAHPath->text()
		<< "\nThemesPath:" << TThemesPath->text()
		<< "\nEnginePath:" << TEnginePath->text()
		<< "\n";
	qApp->quit();
}
void Window::mQuit()
{
	QTextStream qout(stdout);
	qout << "Cansel";
	qApp->quit();
}
