# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste.ui'
#
# Created: Tue May 24 13:32:09 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!
import subprocess
import os

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

def gmail():
	subprocess.Popen("google-chrome http://gmail.com", shell=True)

def facebook():
	subprocess.Popen("google-chrome http://facebook.com", shell=True)

def nosso():
	subprocess.Popen("google-chrome http://viviedidi.biz", shell=True)

def casafofa():
	subprocess.Popen("google-chrome http://casafofa.com", shell=True)

class Ui_bemvinda(object):
    def setupUi(self, bemvinda):
        script_path = os.path.dirname(os.path.realpath(__file__))
        imagem_fofa = os.path.join(script_path, 'vidi.png')
        bemvinda.setObjectName(_fromUtf8("bemvinda"))
        bemvinda.setFocus()
        bemvinda.resize(398, 342)
        bemvinda.setMinimumSize(QtCore.QSize(398, 342))
        bemvinda.setMaximumSize(QtCore.QSize(398, 342))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(imagem_fofa)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        bemvinda.setWindowIcon(icon)
        bemvinda.setAutoFillBackground(False)
        self.graphicsView = QtGui.QGraphicsView(bemvinda)
        self.graphicsView.setGeometry(QtCore.QRect(70, 20, 256, 281))
        self.graphicsView.setStyleSheet(_fromUtf8("border-image: url(%s);" % imagem_fofa))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.pushButton = QtGui.QPushButton(bemvinda)
        self.pushButton.setGeometry(QtCore.QRect(290, 310, 95, 27))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(bemvinda)
        self.pushButton_2.setGeometry(QtCore.QRect(5, 310, 95, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(bemvinda)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 310, 95, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(bemvinda)
        self.pushButton_4.setGeometry(QtCore.QRect(195, 310, 95, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.retranslateUi(bemvinda)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), facebook)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), nosso)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), gmail)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), casafofa)


        QtCore.QMetaObject.connectSlotsByName(bemvinda)


    def retranslateUi(self, bemvinda):
        bemvinda.setWindowTitle(QtGui.QApplication.translate("bemvinda", "Bem Vinda Amor!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("bemvinda", "Facebook", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("bemvinda", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("bemvinda", "Nosso Site", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("bemvinda", "Casa Fofa", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    bemvinda = QtGui.QDialog()
    ui = Ui_bemvinda()
    ui.setupUi(bemvinda)
    bemvinda.show()
    sys.exit(app.exec_())

