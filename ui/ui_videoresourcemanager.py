# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_videoresourcemanager.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VideoResourceManagerWidget(object):
    def setupUi(self, VideoResourceManagerWidget):
        VideoResourceManagerWidget.setObjectName("VideoResourceManagerWidget")
        VideoResourceManagerWidget.resize(836, 760)
        self.gridLayout = QtWidgets.QGridLayout(VideoResourceManagerWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.videoInfoFrame = QtWidgets.QFrame(VideoResourceManagerWidget)
        self.videoInfoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.videoInfoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.videoInfoFrame.setObjectName("videoInfoFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.videoInfoFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.videoInfoTableWidget = QtWidgets.QTableWidget(self.videoInfoFrame)
        self.videoInfoTableWidget.setMinimumSize(QtCore.QSize(0, 640))
        self.videoInfoTableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.videoInfoTableWidget.setShowGrid(True)
        self.videoInfoTableWidget.setGridStyle(QtCore.Qt.DashDotLine)
        self.videoInfoTableWidget.setRowCount(0)
        self.videoInfoTableWidget.setObjectName("videoInfoTableWidget")
        self.videoInfoTableWidget.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.videoInfoTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.videoInfoTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.videoInfoTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.videoInfoTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.videoInfoTableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayout_2.addWidget(self.videoInfoTableWidget, 0, 0, 1, 8)
        self.searchVideoLabel = QtWidgets.QLabel(self.videoInfoFrame)
        self.searchVideoLabel.setMinimumSize(QtCore.QSize(60, 20))
        self.searchVideoLabel.setObjectName("searchVideoLabel")
        self.gridLayout_2.addWidget(self.searchVideoLabel, 1, 0, 1, 1)
        self.searchVideoLineEdit = QtWidgets.QLineEdit(self.videoInfoFrame)
        self.searchVideoLineEdit.setMinimumSize(QtCore.QSize(200, 20))
        self.searchVideoLineEdit.setMaximumSize(QtCore.QSize(320, 20))
        self.searchVideoLineEdit.setObjectName("searchVideoLineEdit")
        self.gridLayout_2.addWidget(self.searchVideoLineEdit, 1, 1, 1, 1)
        self.searchVideoButton = QtWidgets.QPushButton(self.videoInfoFrame)
        self.searchVideoButton.setMinimumSize(QtCore.QSize(80, 30))
        self.searchVideoButton.setMaximumSize(QtCore.QSize(80, 30))
        self.searchVideoButton.setObjectName("searchVideoButton")
        self.gridLayout_2.addWidget(self.searchVideoButton, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 3, 1, 1)
        self.addVideoButton = QtWidgets.QPushButton(self.videoInfoFrame)
        self.addVideoButton.setMinimumSize(QtCore.QSize(80, 30))
        self.addVideoButton.setMaximumSize(QtCore.QSize(80, 30))
        self.addVideoButton.setObjectName("addVideoButton")
        self.gridLayout_2.addWidget(self.addVideoButton, 1, 4, 1, 1)
        self.editVideoButton = QtWidgets.QPushButton(self.videoInfoFrame)
        self.editVideoButton.setMinimumSize(QtCore.QSize(80, 30))
        self.editVideoButton.setMaximumSize(QtCore.QSize(80, 30))
        self.editVideoButton.setObjectName("editVideoButton")
        self.gridLayout_2.addWidget(self.editVideoButton, 1, 5, 1, 1)
        self.deleteVideoButton = QtWidgets.QPushButton(self.videoInfoFrame)
        self.deleteVideoButton.setMinimumSize(QtCore.QSize(80, 30))
        self.deleteVideoButton.setMaximumSize(QtCore.QSize(80, 30))
        self.deleteVideoButton.setObjectName("deleteVideoButton")
        self.gridLayout_2.addWidget(self.deleteVideoButton, 1, 6, 1, 1)
        self.playVideoButton = QtWidgets.QPushButton(self.videoInfoFrame)
        self.playVideoButton.setMinimumSize(QtCore.QSize(80, 30))
        self.playVideoButton.setMaximumSize(QtCore.QSize(80, 30))
        self.playVideoButton.setObjectName("playVideoButton")
        self.gridLayout_2.addWidget(self.playVideoButton, 1, 7, 1, 1)
        self.gridLayout.addWidget(self.videoInfoFrame, 0, 0, 1, 4)
        self.potPlayerPathTitleLabel = QtWidgets.QLabel(VideoResourceManagerWidget)
        self.potPlayerPathTitleLabel.setMinimumSize(QtCore.QSize(100, 20))
        self.potPlayerPathTitleLabel.setMaximumSize(QtCore.QSize(100, 20))
        self.potPlayerPathTitleLabel.setObjectName("potPlayerPathTitleLabel")
        self.gridLayout.addWidget(self.potPlayerPathTitleLabel, 1, 0, 1, 1)
        self.potPlayerPathDisplayLabel = QtWidgets.QLabel(VideoResourceManagerWidget)
        self.potPlayerPathDisplayLabel.setMinimumSize(QtCore.QSize(400, 20))
        self.potPlayerPathDisplayLabel.setMaximumSize(QtCore.QSize(400, 20))
        self.potPlayerPathDisplayLabel.setText("")
        self.potPlayerPathDisplayLabel.setObjectName("potPlayerPathDisplayLabel")
        self.gridLayout.addWidget(self.potPlayerPathDisplayLabel, 1, 1, 1, 1)
        self.selectPotPlayerPathButton = QtWidgets.QPushButton(VideoResourceManagerWidget)
        self.selectPotPlayerPathButton.setMinimumSize(QtCore.QSize(80, 30))
        self.selectPotPlayerPathButton.setMaximumSize(QtCore.QSize(80, 30))
        self.selectPotPlayerPathButton.setObjectName("selectPotPlayerPathButton")
        self.gridLayout.addWidget(self.selectPotPlayerPathButton, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(44, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)

        self.retranslateUi(VideoResourceManagerWidget)
        QtCore.QMetaObject.connectSlotsByName(VideoResourceManagerWidget)

    def retranslateUi(self, VideoResourceManagerWidget):
        _translate = QtCore.QCoreApplication.translate
        VideoResourceManagerWidget.setWindowTitle(_translate("VideoResourceManagerWidget", "Video Resource Manager"))
        item = self.videoInfoTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("VideoResourceManagerWidget", "name"))
        item = self.videoInfoTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("VideoResourceManagerWidget", "path"))
        item = self.videoInfoTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("VideoResourceManagerWidget", "start"))
        item = self.videoInfoTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("VideoResourceManagerWidget", "end"))
        item = self.videoInfoTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("VideoResourceManagerWidget", "cost"))
        self.searchVideoLabel.setText(_translate("VideoResourceManagerWidget", "Search:"))
        self.searchVideoButton.setText(_translate("VideoResourceManagerWidget", "Submit"))
        self.addVideoButton.setText(_translate("VideoResourceManagerWidget", "Add"))
        self.editVideoButton.setText(_translate("VideoResourceManagerWidget", "Edit"))
        self.deleteVideoButton.setText(_translate("VideoResourceManagerWidget", "Delete"))
        self.playVideoButton.setText(_translate("VideoResourceManagerWidget", "Play"))
        self.potPlayerPathTitleLabel.setText(_translate("VideoResourceManagerWidget", "PotPlayer Path:"))
        self.selectPotPlayerPathButton.setText(_translate("VideoResourceManagerWidget", "Select"))
