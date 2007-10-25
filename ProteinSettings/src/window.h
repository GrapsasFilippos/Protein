/*===========================
       Grapsas Filippos
        GPLv2 License
===========================*/

#ifndef __WINDOW_H__
#define __WINDOW_H__

#include <QApplication>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QToolButton>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QGridLayout>
#include <QGroupBox>
#include <QString>
#include <QFileDialog>
#include <QTextStream>


class Window : public QWidget
{
	Q_OBJECT
	
	public:
	Window(QString FPath, QString TPath, QString EPath, QWidget *parent = 0);
	
	private slots:
	void BrFAHPath();
	void BrThemesPath();
	void BrEnginePath();
	void Save();
	void mQuit();
	
	private:
	QLabel *LFAHPath;
	QLineEdit *TFAHPath;
	QToolButton *BFAHPath;
	QLabel *LThemesPath;
	QLineEdit *TThemesPath;
	QToolButton *BThemesPath;
	QLabel *LEnginePath;
	QLineEdit *TEnginePath;
	QToolButton *BEnginePath;
	QPushButton *BOk;
	QPushButton *BCansel;
	
	QGridLayout *LyBase;
	QGroupBox *GbSettings;
	QHBoxLayout *LyOkBar;
	QVBoxLayout *LyTop;
};

#endif // __WINDOW_H__
