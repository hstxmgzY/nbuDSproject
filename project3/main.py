import os

from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QApplication
import sys
from utils.maze_gui import MazeGui
from PyQt5.QtCore import Qt
from stack import Stack

class DfsQMaze(MazeGui):
    def __init__(self, a=5, b=20):
        super(DfsQMaze, self).__init__(a, b)  # 父类初始化
        # print("start:{},end:{}".format(self.ENTRANCE, self.EXIT))
        # print(self.MAZE)

    def paintEvent(self, paintEvent):
        """
        【注】QWidigets类的方法，所有画图的操作放在这里。实例化时，会自动调用这个方法。
        """
        super(DfsQMaze, self).paintEvent(paintEvent)  # 父类绘画界面初始化
        self.paintDfs()

    def paintDfs(self):
        """将递归的过程画出来，必须通过`paintEvent()`方法调用
        【注】如果在`dfs()`中使用了相关画图、画线等函数，即可在窗口中绘制出来
        """
        self.dfs()
        self.draw_point(self.ENTRANCE, self.pen, self.painter, _color=Qt.blue)
        self.draw_point(self.EXIT, self.pen, self.painter, _color=Qt.red)
        del self.pen, self.painter

    def dfs(self):
        self.xl = len(self.MAZE)  # 迷宫纵向总长度
        self.yl = len(self.MAZE[0])  # 迷宫横向总长度
        self.mtemp = []  # 用来存放到过的位置，若来过该点则为 1
        [self.xend, self.yend] = self.EXIT  # 迷宫出口坐标
        for x in range(0, self.xl):
            list = []
            for y in range(0, self.yl):
                list.append(0)
            self.mtemp.append(list)  # 将mtemp列表全部置零
        [x, y] = self.ENTRANCE  # 迷宫入口坐标
        mystack.push(x)  # 将迷宫第一个位置压入栈
        mystack.push(y)
        self.find_path(x, y)  # 开始寻找出口

    def get_xy(self):  # 返回栈顶元素x，y为当前处理的坐标
        y = mystack.top()
        mystack.pop()
        x = mystack.top()
        mystack.push(y)  # 把y放回去
        return x, y

    def find_path(self, x, y):  # 递归实现
        x0, y0 = self.get_xy()  # 获取栈顶元素坐标（上一个经过位置）
        mystack.push(x)  # 将现在处理的坐标压入栈中
        mystack.push(y)  # 将现在处理的坐标和栈顶元素坐标用绿线相连，说明走过该条路
        self.drawLine([x0, y0], [x, y], color=Qt.green, width_scale=0.55)
        self.mtemp[x][y] = 1  # 将走过的点赋值为1
        if x == self.xend and y == self.yend:  # 若现在处理的点是出口坐标，则函数结束，找到出口
            return
        else:
            # 顺序：右下左上
            # 若右边坐标未超出迷宫，且右边不是墙，且右边没有走到过，则往右边走（调用本函数，递归）
            if y + 1 < self.yl and self.MAZE[x][y + 1] != 1 and self.mtemp[x][y + 1] == 0:
                self.find_path(x, y + 1)
            # 若右边不行，则往下走
            elif x + 1 < self.xl and self.MAZE[x + 1][y] != 1 and self.mtemp[x + 1][y] == 0:
                self.find_path(x + 1, y)
            # 若右边、下边不行，则往左边走
            elif y - 1 >= 0 and self.MAZE[x][y-1] != 1 and self.mtemp[x][y-1] == 0:
                self.find_path(x, y - 1)
            # 若右边、下边，左边都不行，则往上边走
            elif x - 1 >= 0 and self.MAZE[x - 1][y] != 1 and self.mtemp[x - 1][y] == 0:
                self.find_path(x - 1, y)
            # 若四个位置都不能走，则说明近死胡同了，这条路不能走路，返回上一个位置
            else:  # 死胡同
                x0, y0 = self.get_xy()  # 获取现在这个点的位置
                mystack.pop()  # 把上一个位置从栈中弹出
                mystack.pop()
                y = mystack.top()  # 获取上一个点的位置
                mystack.pop()
                x = mystack.top()
                mystack.pop()
                #   将上一个点到死胡同的路标黄，作为记录
                self.drawLine([x0, y0], [x, y], color=Qt.yellow, width_scale=0.55)
                self.find_path(x, y)  # 到上一个点寻找出路

    def mouseDoubleClickEvent(self, a0: QMouseEvent):  # 鼠标双击事件，重新启动，达到刷新效果
        python = sys.executable
        os.execl(python, python, *sys.argv)


if __name__ == "__main__":
    mystack = Stack()
    application = QApplication(sys.argv)
    solver = DfsQMaze()
    sys.exit(application.exec_())
