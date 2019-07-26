# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Slider(QtWidgets.QSlider):
    def mousePressEvent(self, e):
        self.setValue(QtWidgets.QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), self.height() - e.y(), self.height()))

    def mouseMoveEvent(self, e):
        self.setValue(QtWidgets.QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), self.height() - e.y(), self.height()))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.hbox1 = QtWidgets.QHBoxLayout()
        self.hbox1.setObjectName("hbox1")
        self.le1 = QtWidgets.QLabel(self.centralwidget)
        self.le1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.le1.setObjectName("le1")
        self.hbox1.addWidget(self.le1)
        self.vline1 = QtWidgets.QFrame(self.centralwidget)
        self.vline1.setFrameShape(QtWidgets.QFrame.VLine)
        self.vline1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline1.setObjectName("vline1")
        self.hbox1.addWidget(self.vline1)
        self.vbox1 = QtWidgets.QVBoxLayout()
        self.vbox1.setObjectName("vbox1")
        self.vbox2 = QtWidgets.QVBoxLayout()
        self.vbox2.setSpacing(6)
        self.vbox2.setObjectName("vbox2")
        self.le2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le2.sizePolicy().hasHeightForWidth())
        self.le2.setSizePolicy(sizePolicy)
        self.le2.setAlignment(QtCore.Qt.AlignCenter)
        self.le2.setObjectName("le2")
        self.vbox2.addWidget(self.le2)
        self.vslider1 = Slider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vslider1.sizePolicy().hasHeightForWidth())
        self.vslider1.setSizePolicy(sizePolicy)
        self.vslider1.setMinimum(1)
        self.vslider1.setMaximum(99)
        self.vslider1.setSingleStep(2)
        self.vslider1.setOrientation(QtCore.Qt.Vertical)
        self.vslider1.setObjectName("vslider1")
        self.vbox2.addWidget(self.vslider1)
        self.vbox2.setStretch(0, 1)
        self.vbox2.setStretch(1, 9)
        self.vbox1.addLayout(self.vbox2)
        self.hline2 = QtWidgets.QFrame(self.centralwidget)
        self.hline2.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline2.setObjectName("hline2")
        self.vbox1.addWidget(self.hline2)
        self.le3 = QtWidgets.QLabel(self.centralwidget)
        self.le3.setAlignment(QtCore.Qt.AlignCenter)
        self.le3.setObjectName("le3")
        self.vbox1.addWidget(self.le3)
        self.hline1 = QtWidgets.QFrame(self.centralwidget)
        self.hline1.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline1.setObjectName("hline1")
        self.vbox1.addWidget(self.hline1)
        self.gbox1 = QtWidgets.QGridLayout()
        self.gbox1.setObjectName("gbox1")
        self.ptn_reload = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_reload.setObjectName("ptn_reload")
        self.gbox1.addWidget(self.ptn_reload, 6, 2, 1, 1)
        self.ptn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_reset.setObjectName("ptn_reset")
        self.gbox1.addWidget(self.ptn_reset, 6, 0, 1, 1)
        self.ptn_openfolder = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_openfolder.setObjectName("ptn_openfolder")
        self.gbox1.addWidget(self.ptn_openfolder, 2, 2, 1, 1)
        self.ptn_open = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_open.setObjectName("ptn_open")
        self.gbox1.addWidget(self.ptn_open, 2, 0, 1, 1)
        self.ptn_next = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_next.setObjectName("ptn_next")
        self.gbox1.addWidget(self.ptn_next, 3, 2, 1, 1)
        self.ptn_last = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_last.setObjectName("ptn_last")
        self.gbox1.addWidget(self.ptn_last, 3, 0, 1, 1)
        self.ptn_break = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_break.setObjectName("ptn_break")
        self.gbox1.addWidget(self.ptn_break, 5, 0, 1, 1)
        self.ptn_group = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_group.setObjectName("ptn_group")
        self.gbox1.addWidget(self.ptn_group, 5, 2, 1, 1)
        self.ptn_reverse = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_reverse.setObjectName("ptn_reverse")
        self.gbox1.addWidget(self.ptn_reverse, 7, 2, 1, 1)
        self.ptn_save = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_save.setObjectName("ptn_save")
        self.gbox1.addWidget(self.ptn_save, 7, 0, 1, 1)
        self.vbox1.addLayout(self.gbox1)
        self.ptn_quit = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_quit.setObjectName("ptn_quit")
        self.vbox1.addWidget(self.ptn_quit)
        self.hbox1.addLayout(self.vbox1)
        self.hbox1.setStretch(0, 4)
        self.hbox1.setStretch(2, 1)
        self.horizontalLayout_3.addLayout(self.hbox1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 20))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_OpenFolder = QtWidgets.QAction(MainWindow)
        self.action_OpenFolder.setObjectName("action_OpenFolder")
        self.action_Save = QtWidgets.QAction(MainWindow)
        self.action_Save.setObjectName("action_Save")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Reload = QtWidgets.QAction(MainWindow)
        self.action_Reload.setObjectName("action_Reload")
        self.action_Break = QtWidgets.QAction(MainWindow)
        self.action_Break.setObjectName("action_Break")
        self.action_Next = QtWidgets.QAction(MainWindow)
        self.action_Next.setObjectName("action_Next")
        self.action_Last = QtWidgets.QAction(MainWindow)
        self.action_Last.setObjectName("action_Last")
        self.action_Group = QtWidgets.QAction(MainWindow)
        self.action_Group.setObjectName("action_Group")
        self.action_Open = QtWidgets.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Up = QtWidgets.QAction(MainWindow)
        self.action_Up.setObjectName("action_Up")
        self.action_Down = QtWidgets.QAction(MainWindow)
        self.action_Down.setObjectName("action_Down")
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_OpenFolder)
        self.menu_File.addAction(self.action_Reload)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Edit.addAction(self.action_Last)
        self.menu_Edit.addAction(self.action_Next)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_Group)
        self.menu_Edit.addAction(self.action_Break)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_Up)
        self.menu_Edit.addAction(self.action_Down)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Segmentation Demo"))
        self.le1.setText(_translate("MainWindow", "Image"))
        self.le2.setText(_translate("MainWindow", "Kernel Size"))
        self.le3.setText(_translate("MainWindow", "TextLabel"))
        self.ptn_reload.setText(_translate("MainWindow", "&Reload"))
        self.ptn_reset.setText(_translate("MainWindow", "Reset"))
        self.ptn_openfolder.setText(_translate("MainWindow", "&Open Folder"))
        self.ptn_open.setText(_translate("MainWindow", "Open"))
        self.ptn_next.setText(_translate("MainWindow", "&Next"))
        self.ptn_last.setText(_translate("MainWindow", "&Last"))
        self.ptn_break.setText(_translate("MainWindow", "&Break"))
        self.ptn_group.setText(_translate("MainWindow", "&Group"))
        self.ptn_reverse.setText(_translate("MainWindow", "Reverse"))
        self.ptn_save.setText(_translate("MainWindow", "&Save"))
        self.ptn_quit.setText(_translate("MainWindow", "&Quit"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit"))
        self.action_OpenFolder.setText(_translate("MainWindow", "&Open Folder"))
        self.action_OpenFolder.setStatusTip(_translate("MainWindow", "Open an image from the file system"))
        self.action_OpenFolder.setShortcut(_translate("MainWindow", "O"))
        self.action_Save.setText(_translate("MainWindow", "&Save"))
        self.action_Save.setStatusTip(_translate("MainWindow", "Save the segmentations of the image"))
        self.action_Save.setShortcut(_translate("MainWindow", "S"))
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))
        self.action_Quit.setStatusTip(_translate("MainWindow", "Quit the demo"))
        self.action_Quit.setShortcut(_translate("MainWindow", "Q"))
        self.action_Reload.setText(_translate("MainWindow", "&Reload"))
        self.action_Reload.setStatusTip(_translate("MainWindow", "Reload the image"))
        self.action_Reload.setShortcut(_translate("MainWindow", "R"))
        self.action_Break.setText(_translate("MainWindow", "&Break"))
        self.action_Break.setStatusTip(_translate("MainWindow", "Break the contours"))
        self.action_Break.setShortcut(_translate("MainWindow", "B"))
        self.action_Next.setText(_translate("MainWindow", "&Next"))
        self.action_Next.setStatusTip(_translate("MainWindow", "Load next image"))
        self.action_Next.setShortcut(_translate("MainWindow", "N"))
        self.action_Last.setText(_translate("MainWindow", "&Last"))
        self.action_Last.setStatusTip(_translate("MainWindow", "Load last image"))
        self.action_Last.setShortcut(_translate("MainWindow", "L"))
        self.action_Group.setText(_translate("MainWindow", "Group"))
        self.action_Group.setStatusTip(_translate("MainWindow", "Group the contours"))
        self.action_Group.setShortcut(_translate("MainWindow", "G"))
        self.action_Open.setText(_translate("MainWindow", "Open"))
        self.action_Open.setStatusTip(_translate("MainWindow", "Open images"))
        self.action_Up.setText(_translate("MainWindow", "Up"))
        self.action_Up.setShortcut(_translate("MainWindow", "Up"))
        self.action_Down.setText(_translate("MainWindow", "Down"))
        self.action_Down.setShortcut(_translate("MainWindow", "Down"))

