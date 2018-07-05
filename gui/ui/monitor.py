# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/monitor.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        Dialog.setMinimumSize(QtCore.QSize(640, 480))
        Dialog.setMaximumSize(QtCore.QSize(1920, 1080))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalWidget_2 = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_2.sizePolicy().hasHeightForWidth())
        self.verticalWidget_2.setSizePolicy(sizePolicy)
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.menu_btn = QtWidgets.QPushButton(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_btn.sizePolicy().hasHeightForWidth())
        self.menu_btn.setSizePolicy(sizePolicy)
        self.menu_btn.setMinimumSize(QtCore.QSize(16, 16))
        self.menu_btn.setMaximumSize(QtCore.QSize(32, 32))
        self.menu_btn.setSizeIncrement(QtCore.QSize(1, 1))
        self.menu_btn.setBaseSize(QtCore.QSize(24, 24))
        self.menu_btn.setToolTipDuration(1)
        self.menu_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../media/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_btn.setIcon(icon)
        self.menu_btn.setIconSize(QtCore.QSize(24, 24))
        self.menu_btn.setCheckable(False)
        self.menu_btn.setDefault(False)
        self.menu_btn.setFlat(True)
        self.menu_btn.setObjectName("menu_btn")
        self.verticalLayout_2.addWidget(self.menu_btn)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalWidget_2)
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../media/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalWidget_2)
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.settings_btn = QtWidgets.QPushButton(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_btn.sizePolicy().hasHeightForWidth())
        self.settings_btn.setSizePolicy(sizePolicy)
        self.settings_btn.setMinimumSize(QtCore.QSize(24, 24))
        self.settings_btn.setMaximumSize(QtCore.QSize(32, 32))
        self.settings_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.settings_btn.setTabletTracking(False)
        self.settings_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.settings_btn.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.settings_btn.setAcceptDrops(False)
        self.settings_btn.setToolTipDuration(1)
        self.settings_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../media/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_btn.setIcon(icon2)
        self.settings_btn.setIconSize(QtCore.QSize(24, 24))
        self.settings_btn.setFlat(True)
        self.settings_btn.setObjectName("settings_btn")
        self.verticalLayout_2.addWidget(self.settings_btn)
        self.horizontalLayout.addWidget(self.verticalWidget_2)
        self.verticalWidget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.add_site_btn = QtWidgets.QPushButton(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_site_btn.sizePolicy().hasHeightForWidth())
        self.add_site_btn.setSizePolicy(sizePolicy)
        self.add_site_btn.setMinimumSize(QtCore.QSize(0, 32))
        self.add_site_btn.setMaximumSize(QtCore.QSize(16777214, 16777214))
        self.add_site_btn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.add_site_btn.setFont(font)
        self.add_site_btn.setObjectName("add_site_btn")
        self.verticalLayout.addWidget(self.add_site_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.verticalWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.menu_btn.setToolTip(_translate("Dialog", "Menu"))
        self.settings_btn.setToolTip(_translate("Dialog", "Settings"))
        self.label_6.setText(_translate("Dialog", "To see your site status, please add it to site list."))
        self.add_site_btn.setText(_translate("Dialog", "Add site"))

