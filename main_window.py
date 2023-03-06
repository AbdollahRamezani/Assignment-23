# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(488, 533)
        self.menu_newgame = QAction(MainWindow)
        self.menu_newgame.setObjectName(u"menu_newgame")
        self.menu_openfile = QAction(MainWindow)
        self.menu_openfile.setObjectName(u"menu_openfile")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 471, 471))
        self.grid_Layout = QGridLayout(self.gridLayoutWidget)
        self.grid_Layout.setObjectName(u"grid_Layout")
        self.grid_Layout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 488, 22))
        self.menuGame = QMenu(self.menuBar)
        self.menuGame.setObjectName(u"menuGame")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuGame.menuAction())
        self.menuGame.addSeparator()
        self.menuGame.addAction(self.menu_newgame)
        self.menuGame.addAction(self.menu_openfile)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sudoku Game", None))
        self.menu_newgame.setText(QCoreApplication.translate("MainWindow", u"NewGame", None))
        self.menu_openfile.setText(QCoreApplication.translate("MainWindow", u"OpenFile", None))
        self.menuGame.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
    # retranslateUi

