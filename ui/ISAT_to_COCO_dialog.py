# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/super/PycharmProjects/ISAT_with_segment_anything/ui/ISAT_to_COCO_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(600, 226)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_save_path = QtWidgets.QPushButton(self.widget)
        self.pushButton_save_path.setObjectName("pushButton_save_path")
        self.gridLayout.addWidget(self.pushButton_save_path, 3, 1, 1, 1)
        self.pushButton_label_root = QtWidgets.QPushButton(self.widget)
        self.pushButton_label_root.setObjectName("pushButton_label_root")
        self.gridLayout.addWidget(self.pushButton_label_root, 2, 1, 1, 1)
        self.lineEdit_save_path = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_save_path.setEnabled(True)
        self.lineEdit_save_path.setReadOnly(True)
        self.lineEdit_save_path.setObjectName("lineEdit_save_path")
        self.gridLayout.addWidget(self.lineEdit_save_path, 3, 0, 1, 1)
        self.lineEdit_label_root = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_label_root.setEnabled(True)
        self.lineEdit_label_root.setReadOnly(True)
        self.lineEdit_label_root.setObjectName("lineEdit_label_root")
        self.gridLayout.addWidget(self.lineEdit_label_root, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.textBrowser.setFont(font)
        self.textBrowser.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.widget_3 = QtWidgets.QWidget(Dialog)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addWidget(self.widget_3)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_cache = QtWidgets.QPushButton(self.widget_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/关闭_close-one.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cache.setIcon(icon)
        self.pushButton_cache.setObjectName("pushButton_cache")
        self.horizontalLayout.addWidget(self.pushButton_cache)
        self.pushButton_apply = QtWidgets.QPushButton(self.widget_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/校验_check-one.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_apply.setIcon(icon1)
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.horizontalLayout.addWidget(self.pushButton_apply)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ISAT to COCO"))
        self.pushButton_save_path.setText(_translate("Dialog", "Save path"))
        self.pushButton_label_root.setText(_translate("Dialog", "Jsons root"))
        self.lineEdit_save_path.setPlaceholderText(_translate("Dialog", "COCO json save path"))
        self.lineEdit_label_root.setPlaceholderText(_translate("Dialog", "ISAT jsons root"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\';\"><br /></p></body></html>"))
        self.label.setText(_translate("Dialog", "Convert ISAT jsons to COCO json.The layer attr will be lost."))
        self.pushButton_cache.setText(_translate("Dialog", "cache"))
        self.pushButton_apply.setText(_translate("Dialog", "convert"))
import icons_rc
