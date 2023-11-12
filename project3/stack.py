class Stack(object):
    def __init__(self):# 创建私有list初始化栈
        self.__list = []
    # 判空
    def is_empty(self):
        return self.__list == []
    # 入栈
    def push(self,item):
        self.__list.append(item)
    # 出栈
    def pop(self):
        if self.is_empty():
            return
        else:
            return self.__list.pop()
    # 查看顶部元素
    def top(self):
        if self.is_empty():
            return False  #空了 返回错
        else:
            return self.__list[-1]