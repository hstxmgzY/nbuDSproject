import sys
from PyQt6.QtCore import Qt
from PyQt6 import QtCore, QtGui, QtWidgets

from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QApplication, QGraphicsScene, QGraphicsPixmapItem
from PyQt6.QtWidgets import QPushButton

from link import Ui_Dialog as u

class Node():   #链表中的一个结点
    def __init__(self, id=None, name=None, birthday=None, sex=None, photo=None, nation=None, hobby=None, index=None):
        self._id = id
        self._name = name
        self._birthday = birthday
        self._sex = sex
        self._photo = photo
        self._nation = nation
        self._hobby = hobby
        self._index = index
        self._next = None
    def change_name(self, name):
        self._name = name
    def change_birthday(self, birthday):
        self._birthday = birthday
    def change_sex(self, sex):
        self._sex = sex
    def change_photo(self, photo):
        self._photo = photo
    def change_nation(self, nation):
        self._nation = nation
    def change_hobby(self, hobby):
        self._hobby = hobby

class linklist():
    def __init__(self):
        node = Node()
        self.head = node

    def is_empty(self):
        return self.head._next == None

    def get_length(self):
        if self.is_empty() == False:
            cnt =0
            h = self.head._next
            while h != None:
                cnt += 1
                h = h._next
            return cnt
        else:
            return 0

    def insert(self, index, item):
        pre = self.head
        p = self.head._next
        index -=1
        while index:
            p = p._next
            pre = pre._next
            index -= 1
        pre._next = item
        item._next = p

    def remove(self, index):
        pre = self.head
        p = self.head._next
        index -= 1
        while index:
            p = p._next
            pre = pre._next
            index-=1
        pre._next = p._next
        del p

    def find(self, iid):
        p = self.head
        while p != None:
            if p._id == iid:
                return p
            else:
                p = p._next
        return 0

    def clear(self):
        self.head = None

friends_link = linklist()

class MyLink(QMainWindow, u):
    signal = pyqtSignal(str)
    def __init__(self, parent = None):
        super(MyLink, self).__init__(parent)
        self.pic_path = ''
        self.setupUi(self)
        self.connecter()

    def connecter(self):    #把函数与对应按钮相连接
        self.putphoto.clicked.connect(self.put_photo)
        self.input.clicked.connect(self.insert_item)
        self.find.clicked.connect(self.find_item)
        self.delete_2.clicked.connect(self.del_item)
        self.clear.clicked.connect(self.clear_items)
        self.changebtn.clicked.connect(self.change_item)
        self.changephoto.clicked.connect(self.change_photo)
        self.clear_find.clicked.connect(self.clear_finditem)
        self.Exit.clicked.connect(self.click_button)


    def put_photo(self):    #上传图片
        file, filetype = QFileDialog.getOpenFileName(self,"打开图片", "",
                                                       "All Pixmaps(*.bmp;*.cur;*.gif;*.icns;*.ico;*.jpeg;*.jpg;*.pbm;*.pgm;*.png;*.ppm;*.svg;*.svgz;*.tga;*.tif;*.tiff;*. wbmp;*.webp;*.xbm;*.xpm)")
        img = QtGui.QPixmap(file).scaled(self.graph.width(), self.graph.height(), Qt.AspectRatioMode.KeepAspectRatio)
        self.graph.setPixmap(img)
        self.pic_path = file    #打开图片

    def change_photo(self): #修改图片
        file, filetype = QFileDialog.getOpenFileName(self, "打开图片", "",
                                                     "All Pixmaps(*.bmp;*.cur;*.gif;*.icns;*.ico;*.jpeg;*.jpg;*.pbm;*.pgm;*.png;*.ppm;*.svg;*.svgz;*.tga;*.tif;*.tiff;*. wbmp;*.webp;*.xbm;*.xpm)")
        img = QtGui.QPixmap(file).scaled(self.graph.width(), self.graph.height(), Qt.AspectRatioMode.KeepAspectRatio)
        self.graph_2.setPixmap(img)
        self.pic_path = file  # 打开图片


    def insert_item(self):  #插入信息
        if self.namebox.text() == '' or self.idbox.text() =='' or self.hobbybox.text() =='' or self.nationbox.text()=='':
            QMessageBox.about(self, "提示", "信息未填写完整！")
            return
        if self.indexbox.text().isdigit():
            index = int(self.indexbox.text())
        else:
            QMessageBox.about(self, "提示", "插入位置请填写数字！")
            return
        name = self.namebox.text()
        id = self.idbox.text()
        birthday = self.birthdaybox.text()
        hobby = self.hobbybox.text()
        nation = self.nationbox.text()
        sex = self.sex.currentText()

        if index <= 0 or index > friends_link.get_length() + 1:
            QMessageBox.about(self, "Warning", "插入元素下标越界！")
            return

        node = Node(id, name, birthday, sex, self.pic_path, nation, hobby, index)
        friends_link.insert(index, node)
        self.people.setText(str(friends_link.get_length()))
        QMessageBox.about(self, "提示", "恭喜你！添加成功！")
        self.pic_path = ''
        self.namebox.clear()
        self.idbox.clear()
        self.birthdaybox.clear()
        self.nationbox.clear()
        self.hobbybox.clear()
        self.graph.clear()
        self.indexbox.clear()

    def find_item(self):        #查找信息
        iid = self.lineEdit_4.text()
        node = friends_link.find(iid)
        if node == 0:
            QMessageBox.warning(self, "警告", "查无此人！")
            self.lineEdit_4.clear()
        else:
            self.name_2.setText(node._name)
            self.birthdayy.setText(node._birthday)
            self.hobby_2.setText(node._hobby)
            self.nation_2.setText(node._nation)
            self.sexx.setText(node._sex)
            img = QtGui.QPixmap(node._photo).scaled(self.graph.width(), self.graph.height(), Qt.AspectRatioMode.KeepAspectRatio)
            self.graph_2.setPixmap(img)

    def del_item(self):     #删除信息
        iid = self.lineEdit_4.text()
        node = friends_link.find(iid)
        friends_link.remove(node._index)
        self.people.setText(str(friends_link.get_length()))
        QMessageBox.about(self, "提示", "删除成功")

    def clear_items(self):      #清空链表
        friends_link.clear()
        self.people.setText('0')
        QMessageBox.about(self, "提示", "已成功清空！")

    def change_item(self):      #修改信息
        iid = self.lineEdit_4.text()
        node = friends_link.find(iid)
        if self.name_2.text() == '' or self.hobby_2.text() =='' or self.nation_2.text()=='' or self.sexx.text == '' or self.birthdayy.text =='':
            QMessageBox.about(self, "提示", "信息未填写完整！")
            return
        if self.sexx.text() not in ['男', '女']:
            QMessageBox.about(self, "提示", "请在性别一栏填入\"男\"或\"女\"")
            return
        name = self.name_2.text()
        node.change_name(name)
        birthday = self.birthdayy.text()
        node.change_birthday(birthday)
        hobby = self.hobby_2.text()
        node.change_hobby(hobby)
        nation = self.nation_2.text()
        node.change_nation(nation)
        sex = self.sexx.text()
        node.change_sex(sex)
        node.change_photo(self.pic_path)
        QMessageBox.about(self, "提示", "恭喜你！修改成功！")

    def clear_finditem(self):   #清空查询的信息
        self.pic_path = ''
        self.name_2.clear()
        self.birthdayy.clear()
        self.nation_2.clear()
        self.hobby_2.clear()
        self.graph_2.clear()
        self.sexx.clear()


    def click_button(self):
        confirm_exit = QMessageBox.question(
            self, "提示", "你确定要退出吗😭",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if confirm_exit == QMessageBox.StandardButton.Yes:
            QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyLink()
    win.show()
    sys.exit(app.exec())