# Form implementation generated from reading ui file 'link.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(693, 593)
        self.namebox = QtWidgets.QLineEdit(Dialog)
        self.namebox.setGeometry(QtCore.QRect(110, 100, 113, 25))
        self.namebox.setText("")
        self.namebox.setObjectName("namebox")
        self.idbox = QtWidgets.QLineEdit(Dialog)
        self.idbox.setGeometry(QtCore.QRect(110, 140, 113, 25))
        self.idbox.setText("")
        self.idbox.setObjectName("idbox")
        self.hobbybox = QtWidgets.QLineEdit(Dialog)
        self.hobbybox.setGeometry(QtCore.QRect(110, 220, 113, 25))
        self.hobbybox.setText("")
        self.hobbybox.setObjectName("hobbybox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 100, 45, 25))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 140, 45, 25))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 180, 45, 25))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 220, 45, 25))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(270, 100, 45, 25))
        self.label_5.setObjectName("label_5")
        self.sex = QtWidgets.QComboBox(Dialog)
        self.sex.setGeometry(QtCore.QRect(310, 100, 71, 25))
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(270, 140, 45, 25))
        self.label_6.setObjectName("label_6")
        self.nationbox = QtWidgets.QLineEdit(Dialog)
        self.nationbox.setGeometry(QtCore.QRect(310, 140, 71, 25))
        self.nationbox.setText("")
        self.nationbox.setObjectName("nationbox")
        self.birthdaybox = QtWidgets.QDateEdit(Dialog)
        self.birthdaybox.setGeometry(QtCore.QRect(110, 180, 131, 25))
        self.birthdaybox.setObjectName("birthdaybox")
        self.input = QtWidgets.QPushButton(Dialog)
        self.input.setEnabled(True)
        self.input.setGeometry(QtCore.QRect(300, 220, 113, 32))
        self.input.setMouseTracking(False)
        self.input.setObjectName("input")
        self.putphoto = QtWidgets.QPushButton(Dialog)
        self.putphoto.setGeometry(QtCore.QRect(480, 200, 113, 32))
        self.putphoto.setObjectName("putphoto")
        self.delete_2 = QtWidgets.QPushButton(Dialog)
        self.delete_2.setGeometry(QtCore.QRect(360, 440, 81, 32))
        self.delete_2.setMouseTracking(False)
        self.delete_2.setObjectName("delete_2")
        self.changephoto = QtWidgets.QPushButton(Dialog)
        self.changephoto.setGeometry(QtCore.QRect(480, 460, 113, 32))
        self.changephoto.setObjectName("changephoto")
        self.hobby_2 = QtWidgets.QLineEdit(Dialog)
        self.hobby_2.setGeometry(QtCore.QRect(110, 420, 113, 25))
        self.hobby_2.setText("")
        self.hobby_2.setObjectName("hobby_2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(270, 340, 45, 25))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(70, 380, 45, 25))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(70, 420, 45, 25))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(270, 380, 45, 25))
        self.label_10.setObjectName("label_10")
        self.name_2 = QtWidgets.QLineEdit(Dialog)
        self.name_2.setGeometry(QtCore.QRect(110, 340, 113, 25))
        self.name_2.setText("")
        self.name_2.setObjectName("name_2")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(70, 340, 45, 25))
        self.label_11.setObjectName("label_11")
        self.nation_2 = QtWidgets.QLineEdit(Dialog)
        self.nation_2.setGeometry(QtCore.QRect(310, 380, 71, 25))
        self.nation_2.setText("")
        self.nation_2.setObjectName("nation_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 280, 113, 25))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(180, 280, 45, 25))
        self.label_13.setObjectName("label_13")
        self.find = QtWidgets.QPushButton(Dialog)
        self.find.setGeometry(QtCore.QRect(350, 278, 113, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.find.setFont(font)
        self.find.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.find.setObjectName("find")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(30, 310, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Herculanum")
        font.setPointSize(18)
        font.setItalic(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(30, 70, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Herculanum")
        font.setPointSize(18)
        font.setItalic(True)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(210, 20, 254, 44))
        font = QtGui.QFont()
        font.setPointSize(31)
        font.setItalic(False)
        font.setKerning(True)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.clear = QtWidgets.QPushButton(Dialog)
        self.clear.setGeometry(QtCore.QRect(210, 530, 113, 32))
        self.clear.setObjectName("clear")
        self.Exit = QtWidgets.QPushButton(Dialog)
        self.Exit.setGeometry(QtCore.QRect(350, 530, 113, 32))
        self.Exit.setObjectName("Exit")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(270, 180, 61, 25))
        self.label_12.setObjectName("label_12")
        self.indexbox = QtWidgets.QLineEdit(Dialog)
        self.indexbox.setGeometry(QtCore.QRect(340, 180, 41, 25))
        self.indexbox.setText("")
        self.indexbox.setObjectName("indexbox")
        self.graph = QtWidgets.QLabel(Dialog)
        self.graph.setGeometry(QtCore.QRect(490, 90, 101, 101))
        self.graph.setText("")
        self.graph.setObjectName("graph")
        self.graph_2 = QtWidgets.QLabel(Dialog)
        self.graph_2.setGeometry(QtCore.QRect(480, 340, 101, 101))
        self.graph_2.setText("")
        self.graph_2.setObjectName("graph_2")
        self.birthdayy = QtWidgets.QLineEdit(Dialog)
        self.birthdayy.setGeometry(QtCore.QRect(110, 380, 113, 25))
        self.birthdayy.setText("")
        self.birthdayy.setObjectName("birthdayy")
        self.sexx = QtWidgets.QLineEdit(Dialog)
        self.sexx.setGeometry(QtCore.QRect(310, 340, 71, 25))
        self.sexx.setText("")
        self.sexx.setObjectName("sexx")
        self.changebtn = QtWidgets.QPushButton(Dialog)
        self.changebtn.setGeometry(QtCore.QRect(270, 440, 81, 32))
        self.changebtn.setMouseTracking(False)
        self.changebtn.setObjectName("changebtn")
        self.clear_find = QtWidgets.QPushButton(Dialog)
        self.clear_find.setGeometry(QtCore.QRect(300, 470, 121, 32))
        self.clear_find.setMouseTracking(False)
        self.clear_find.setObjectName("clear_find")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(40, 530, 60, 16))
        self.label_16.setObjectName("label_16")
        self.people = QtWidgets.QTextBrowser(Dialog)
        self.people.setGeometry(QtCore.QRect(100, 530, 41, 21))
        self.people.setObjectName("people")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(150, 530, 21, 16))
        self.label_17.setObjectName("label_17")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "姓名："))
        self.label_2.setText(_translate("Dialog", "学号："))
        self.label_3.setText(_translate("Dialog", "生日："))
        self.label_4.setText(_translate("Dialog", "兴趣："))
        self.label_5.setText(_translate("Dialog", "性别："))
        self.sex.setItemText(0, _translate("Dialog", "男"))
        self.sex.setItemText(1, _translate("Dialog", "女"))
        self.label_6.setText(_translate("Dialog", "民族："))
        self.input.setText(_translate("Dialog", "录入"))
        self.putphoto.setText(_translate("Dialog", "上传照片"))
        self.delete_2.setText(_translate("Dialog", "删除此人"))
        self.changephoto.setText(_translate("Dialog", "替换照片"))
        self.label_7.setText(_translate("Dialog", "性别："))
        self.label_8.setText(_translate("Dialog", "生日："))
        self.label_9.setText(_translate("Dialog", "兴趣："))
        self.label_10.setText(_translate("Dialog", "民族："))
        self.label_11.setText(_translate("Dialog", "姓名："))
        self.label_13.setText(_translate("Dialog", "学号："))
        self.find.setText(_translate("Dialog", "查询"))
        self.label_14.setText(_translate("Dialog", "查询结果"))
        self.label_15.setText(_translate("Dialog", "录入信息"))
        self.label_18.setText(_translate("Dialog", "好友数据管理系统"))
        self.clear.setText(_translate("Dialog", "清空好友"))
        self.Exit.setText(_translate("Dialog", "退出程序"))
        self.label_12.setText(_translate("Dialog", "插入位置："))
        self.changebtn.setText(_translate("Dialog", "修改信息"))
        self.clear_find.setText(_translate("Dialog", "清空查询结果"))
        self.label_16.setText(_translate("Dialog", "现在共有"))
        self.people.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.label_17.setText(_translate("Dialog", "人"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
