# Copyright (C) 2018 Koni Dev Team, All Rights Reserved
# https://github.com/KoniDevTeam/SiteMonster/
#
# This file is part of Site Monster.
#
# Site Monster is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Site Monster is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Site Monster.  If not, see <https://www.gnu.org/licenses/>.
from api import files
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/monitor.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu_vert_ = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_vert_.sizePolicy().hasHeightForWidth())
        self.menu_vert_.setSizePolicy(sizePolicy)
        self.menu_vert_.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.menu_vert_.setObjectName("menu_vert_")
        self.menu_vert_2 = QtWidgets.QVBoxLayout(self.menu_vert_)
        self.menu_vert_2.setContentsMargins(0, 0, 0, -1)
        self.menu_vert_2.setSpacing(6)
        self.menu_vert_2.setObjectName("menu_vert_2")
        self.menu_btn = QtWidgets.QCheckBox(self.menu_vert_)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_btn.sizePolicy().hasHeightForWidth())
        self.menu_btn.setSizePolicy(sizePolicy)
        self.menu_btn.setMinimumSize(QtCore.QSize(24, 24))
        self.menu_btn.setMaximumSize(QtCore.QSize(32, 32))
        self.menu_btn.setSizeIncrement(QtCore.QSize(1, 1))
        self.menu_btn.setBaseSize(QtCore.QSize(24, 24))
        self.menu_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_btn.setToolTipDuration(1)
        self.menu_btn.setStyleSheet("QCheckBox::indicator{\n"
"    width: 32px;\n"
"    height: 32px;\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"    image: url(" + files.get_media_folder_path().replace('\\', '/') + "/menu.png);\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"    image: url(" + files.get_media_folder_path().replace('\\', '/') + "/back.png);\n"
"}")
        self.menu_btn.setText("")
        self.menu_btn.setIconSize(QtCore.QSize(24, 24))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setTristate(False)
        self.menu_btn.setObjectName("menu_btn")
        self.menu_vert_2.addWidget(self.menu_btn)
        self.fav_only_checkbox = QtWidgets.QCheckBox(self.menu_vert_)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fav_only_checkbox.sizePolicy().hasHeightForWidth())
        self.fav_only_checkbox.setSizePolicy(sizePolicy)
        self.fav_only_checkbox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fav_only_checkbox.setStyleSheet("QCheckBox::indicator {\n"
"    height: 24px;\n"
"    width: 24px;\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"    image: url(" + files.get_media_folder_path().replace('\\', '/') + "/checkbox-off.png);\n"
"}\n"
"QCheckBox::indicator:unchecked:hover{\n"
"    image: url(" + files.get_media_folder_path().replace('\\', '/') + "/checkbox-off-hover.png);\n"
"}\n"
"QCheckBox::indicator:unchecked:pressed{\n"
"    image: url(" + files.get_media_folder_path().replace('\\', '/') + "/checkbox-off-pressed.png);\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"    image: url(" + files.get_media_folder_path().replace('\\', '/') + "/checkbox-on.png);\n"
"}\n"
"QCheckBox::indicator:checked:hover{\n"
"    image: url(" + files.get_media_folder_path().replace('\\', '/') + "/checkbox-on-hover.png);\n"
"}\n"
"QCheckBox::indicator:checked:pressed{\n"
"    image: url(" + files.get_media_folder_path().replace('\\', '/') + "/checkbox-on-pressed.png);\n"
"}\n"
"\n"
"")
        self.fav_only_checkbox.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("" + files.get_media_folder_path() + "/filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fav_only_checkbox.setIcon(icon)
        self.fav_only_checkbox.setIconSize(QtCore.QSize(24, 24))
        self.fav_only_checkbox.setChecked(True)
        self.fav_only_checkbox.setObjectName("fav_only_checkbox")
        self.menu_vert_2.addWidget(self.fav_only_checkbox)
        self.fav_container_ = QtWidgets.QWidget(self.menu_vert_)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fav_container_.sizePolicy().hasHeightForWidth())
        self.fav_container_.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.fav_container_.setFont(font)
        self.fav_container_.setObjectName("fav_container_")
        self.fav_container = QtWidgets.QVBoxLayout(self.fav_container_)
        self.fav_container.setContentsMargins(0, 0, 0, 0)
        self.fav_container.setSpacing(15)
        self.fav_container.setObjectName("fav_container")
        self.fav_btn_example = QtWidgets.QPushButton(self.fav_container_)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fav_btn_example.sizePolicy().hasHeightForWidth())
        self.fav_btn_example.setSizePolicy(sizePolicy)
        self.fav_btn_example.setMinimumSize(QtCore.QSize(24, 24))
        self.fav_btn_example.setMaximumSize(QtCore.QSize(256, 32))
        self.fav_btn_example.setSizeIncrement(QtCore.QSize(0, 0))
        self.fav_btn_example.setBaseSize(QtCore.QSize(32, 32))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("" + files.get_media_folder_path() + "/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fav_btn_example.setIcon(icon1)
        self.fav_btn_example.setIconSize(QtCore.QSize(24, 24))
        self.fav_btn_example.setObjectName("fav_btn_example")
        self.fav_container.addWidget(self.fav_btn_example)
        self.menu_vert_2.addWidget(self.fav_container_)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.menu_vert_2.addItem(spacerItem)
        self.plus_site = QtWidgets.QPushButton(self.menu_vert_)
        self.plus_site.setMinimumSize(QtCore.QSize(24, 24))
        self.plus_site.setMaximumSize(QtCore.QSize(32, 32))
        self.plus_site.setToolTipDuration(3500)
        self.plus_site.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("" + files.get_media_folder_path() + "/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plus_site.setIcon(icon2)
        self.plus_site.setIconSize(QtCore.QSize(24, 24))
        self.plus_site.setFlat(True)
        self.plus_site.setObjectName("plus_site")
        self.menu_vert_2.addWidget(self.plus_site)
        self.settings_btn = QtWidgets.QPushButton(self.menu_vert_)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("" + files.get_media_folder_path() + "/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_btn.setIcon(icon3)
        self.settings_btn.setIconSize(QtCore.QSize(24, 24))
        self.settings_btn.setFlat(True)
        self.settings_btn.setObjectName("settings_btn")
        self.menu_vert_2.addWidget(self.settings_btn)
        self.horizontalLayout.addWidget(self.menu_vert_)
        self.container_ = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.container_.sizePolicy().hasHeightForWidth())
        self.container_.setSizePolicy(sizePolicy)
        self.container_.setAccessibleName("")
        self.container_.setObjectName("container_")
        self.container_2 = QtWidgets.QHBoxLayout(self.container_)
        self.container_2.setContentsMargins(0, 0, -1, 0)
        self.container_2.setObjectName("container_2")
        self.line = QtWidgets.QFrame(self.container_)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.container_2.addWidget(self.line)
        self.content_ = QtWidgets.QWidget(self.container_)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content_.sizePolicy().hasHeightForWidth())
        self.content_.setSizePolicy(sizePolicy)
        self.content_.setObjectName("content_")
        self.content = QtWidgets.QVBoxLayout(self.content_)
        self.content.setContentsMargins(1, 0, 1, 0)
        self.content.setObjectName("content")
        self.message_label = QtWidgets.QLabel(self.content_)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(20)
        self.message_label.setFont(font)
        self.message_label.setWordWrap(True)
        self.message_label.setObjectName("message_label")
        self.content.addWidget(self.message_label)
        self.description_ = QtWidgets.QWidget(self.content_)
        self.description_.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.description_.setFont(font)
        self.description_.setObjectName("description_")
        self.formLayout = QtWidgets.QFormLayout(self.description_)
        self.formLayout.setObjectName("formLayout")
        self.url_label = QtWidgets.QLabel(self.description_)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.url_label.setFont(font)
        self.url_label.setObjectName("url_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.url_label)
        self.url = QtWidgets.QLabel(self.description_)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.url.setFont(font)
        self.url.setObjectName("url")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.url)
        self.status_label = QtWidgets.QLabel(self.description_)
        self.status_label.setObjectName("status_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.status_label)
        self.status = QtWidgets.QLabel(self.description_)
        self.status.setStyleSheet("color: \"red\"")
        self.status.setObjectName("status")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.status)
        self.content.addWidget(self.description_)
        self.site_settings = QtWidgets.QPushButton(self.content_)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.site_settings.setFont(font)
        self.site_settings.setIcon(icon3)
        self.site_settings.setIconSize(QtCore.QSize(24, 24))
        self.site_settings.setObjectName("site_settings")
        self.content.addWidget(self.site_settings)
        self.add_site_btn = QtWidgets.QPushButton(self.content_)
        self.add_site_btn.setEnabled(True)
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
        self.content.addWidget(self.add_site_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.content.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.content.addItem(spacerItem2)
        self.delete_site = QtWidgets.QPushButton(self.content_)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_site.sizePolicy().hasHeightForWidth())
        self.delete_site.setSizePolicy(sizePolicy)
        self.delete_site.setMinimumSize(QtCore.QSize(24, 24))
        self.delete_site.setMaximumSize(QtCore.QSize(32, 32))
        self.delete_site.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.delete_site.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("" + files.get_media_folder_path() + "/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_site.setIcon(icon4)
        self.delete_site.setIconSize(QtCore.QSize(24, 24))
        self.delete_site.setFlat(True)
        self.delete_site.setObjectName("delete_site")
        self.content.addWidget(self.delete_site)
        self.container_2.addWidget(self.content_)
        self.horizontalLayout.addWidget(self.container_)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menuabout = QtWidgets.QMenu(self.menubar)
        self.menuabout.setObjectName("menuabout")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuabout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuabout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_btn.setToolTip(_translate("MainWindow", "Menu"))
        self.fav_btn_example.setText(_translate("MainWindow", "Hello"))
        self.plus_site.setToolTip(_translate("MainWindow", "add one more site"))
        self.settings_btn.setToolTip(_translate("MainWindow", "Settings"))
        self.message_label.setText(_translate("MainWindow", "To see your site status, please add it to site list."))
        self.url_label.setText(_translate("MainWindow", "URL:"))
        self.url.setText(_translate("MainWindow", "TextLabel"))
        self.status_label.setText(_translate("MainWindow", "Status:"))
        self.status.setText(_translate("MainWindow", "OMG"))
        self.site_settings.setText(_translate("MainWindow", "Site settings"))
        self.add_site_btn.setText(_translate("MainWindow", "Add site"))
        self.menuabout.setTitle(_translate("MainWindow", "SiteMonster"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

