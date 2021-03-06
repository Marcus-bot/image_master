# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from UI.My_Label import MyLabel, MyLabel_2


class QScrollArea(QtWidgets.QScrollArea):
    def wheelEvent(self, event):
        pass


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(2560, 1600))
        MainWindow.setBaseSize(QtCore.QSize(1280, 720))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(54, 59, 64);\n"
                                 "color: rgb(222, 222, 222);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 12, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_Bin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Bin.setObjectName("pushButton_Bin")
        self.verticalLayout.addWidget(self.pushButton_Bin)
        self.pushButton_ChannelSelect = QtWidgets.QPushButton(
            self.centralwidget)
        self.pushButton_ChannelSelect.setObjectName("pushButton_ChannelSelect")
        self.verticalLayout.addWidget(self.pushButton_ChannelSelect)
        self.pushButton_Adjust = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Adjust.setObjectName("pushButton_Adjust")
        self.verticalLayout.addWidget(self.pushButton_Adjust)
        self.pushButton_Smooth = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Smooth.setObjectName("pushButton_Smooth")
        self.verticalLayout.addWidget(self.pushButton_Smooth)
        self.pushButton_EdgeSelect = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_EdgeSelect.setObjectName("pushButton_EdgeSelect")
        self.verticalLayout.addWidget(self.pushButton_EdgeSelect)
        self.pushButton_contour = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_contour.setObjectName("pushButton_contour")
        self.verticalLayout.addWidget(self.pushButton_contour)
        self.pushButton_Trans = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Trans.setObjectName("pushButton_Trans")
        self.verticalLayout.addWidget(self.pushButton_Trans)
        self.pushButton_Cut = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Cut.setObjectName("pushButton_Cut")
        self.verticalLayout.addWidget(self.pushButton_Cut)
        self.pushButton_lines = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_lines.setObjectName("pushButton_lines")
        self.verticalLayout.addWidget(self.pushButton_lines)
        self.pushButton_circle = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_circle.setObjectName("pushButton_circle")
        self.verticalLayout.addWidget(self.pushButton_circle)
        self.pushButton_rot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rot.setObjectName("pushButton_rot")
        self.verticalLayout.addWidget(self.pushButton_rot)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 835, 536))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

        self.label_origin = MyLabel_2(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_origin.sizePolicy().hasHeightForWidth())
        self.label_origin.setSizePolicy(sizePolicy)
        self.label_origin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_origin.setObjectName("label_origin")
        self.gridLayout.addWidget(self.label_origin, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.scrollArea_2 = QScrollArea(self.centralwidget)
        self.scrollArea_2.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(
            QtCore.QRect(0, 0, 835, 536))
        self.scrollAreaWidgetContents_2.setObjectName(
            "scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(
            self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.scrollArea_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_processed = MyLabel(
            self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_processed.sizePolicy().hasHeightForWidth())
        self.label_processed.setSizePolicy(sizePolicy)
        self.label_processed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_processed.setObjectName("label_processed")
        self.gridLayout_2.addWidget(self.label_processed, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("color: rgb(54, 59, 64);\n"
                                     "selection-background-color: rgb(54, 59, 64);\n"
                                     "")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textBrowser_His = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_His.setObjectName("textBrowser_His")
        self.gridLayout_4.addWidget(self.textBrowser_His, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textBrowser_Msg = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_Msg.setObjectName("textBrowser_Msg")
        self.gridLayout_5.addWidget(self.textBrowser_Msg, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 37))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(40, 40))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "../../Image_process/UI/icons/Open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "../../Image_process/UI/icons/Save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setObjectName("actionSave")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            "../../Image_process/UI/icons/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon2)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(
            "../../Image_process/UI/icons/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon3)
        self.actionRedo.setObjectName("actionRedo")
        self.actionClose = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(
            "../../Image_process/UI/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon4)
        self.actionClose.setObjectName("actionClose")
        self.actionAbout_us = QtWidgets.QAction(MainWindow)
        self.actionAbout_us.setCheckable(True)
        self.actionAbout_us.setObjectName("actionAbout_us")
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.actionClose)
        self.menu_2.addAction(self.actionUndo)
        self.menu_2.addAction(self.actionRedo)
        self.menu_3.addAction(self.actionAbout_us)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "Image Master"))
        self.pushButton_Bin.setText(_translate("MainWindow", "?????????"))
        self.pushButton_ChannelSelect.setText(_translate("MainWindow", "????????????"))
        self.pushButton_Adjust.setText(_translate("MainWindow", "??????"))
        self.pushButton_Smooth.setText(_translate("MainWindow", "??????"))
        self.pushButton_EdgeSelect.setText(_translate("MainWindow", "????????????"))
        self.pushButton_contour.setText(_translate("MainWindow", "????????????"))
        self.pushButton_Trans.setText(_translate("MainWindow", "????????????"))
        self.pushButton_Cut.setText(_translate("MainWindow", "??????"))
        self.pushButton_lines.setText(_translate("MainWindow", "????????????"))
        self.pushButton_circle.setText(_translate("MainWindow", "????????????"))
        self.pushButton_rot.setText(_translate("MainWindow", "??????"))
        self.label_origin.setText(_translate("MainWindow", "??????"))
        self.label_processed.setText(_translate("MainWindow", "??????????????????"))
        self.groupBox.setTitle(_translate("MainWindow", "?????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), _translate("MainWindow", "history"))
        self.textBrowser_Msg.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("MainWindow", "Message"))
        self.menu.setTitle(_translate("MainWindow", "??????"))
        self.menu_2.setTitle(_translate("MainWindow", "??????"))
        self.menu_3.setTitle(_translate("MainWindow", "??????"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionAbout_us.setText(_translate("MainWindow", "About us"))
