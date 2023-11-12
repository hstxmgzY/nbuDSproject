
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

    def remove_by_id(self, iid):
        # 根据学号删除节点
        pre = self.head
        p = self.head._next
        while p:
            if p._id == iid:
                pre._next = p._next
                del p
                return True  # 返回True表示删除成功
            else:
                pre = p
                p = p._next
        return False  # 返回False表示未找到对应学号的节点

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

def main():
    # 创建链表对象
    friends_link = linklist()

    while True:
        print("1. 添加信息")
        print("2. 删除信息")
        print("3. 查找信息")
        print("4. 显示所有信息")
        print("5. 退出")

        choice = input("请输入您的选择: ")

        if choice == "1":
            # 添加信息
            id = input("请输入学号: ")
            name = input("请输入姓名: ")
            birthday = input("请输入生日: ")
            sex = input("请输入性别: ")
            photo = input("请输入照片: ")
            nation = input("请输入民族: ")
            hobby = input("请输入爱好: ")
            index = input("请输入索引: ")

            # 创建节点对象
            node = Node(id=id, name=name, birthday=birthday, sex=sex, photo=photo, nation=nation, hobby=hobby, index=index)
            # 在链表末尾插入节点
            friends_link.insert(friends_link.get_length() + 1, node)
            print("信息添加成功！")

        elif choice == "2":
            # 删除信息
            id = input("请输入要删除的学号: ")
            if friends_link.remove_by_id(id):
                print("信息删除成功！")
            else:
                print("未找到对应学号的信息！")

        elif choice == "3":
            # 查找信息
            id = input("请输入要查找的学号: ")
            node = friends_link.find(id)
            if node:
                print("找到对应的信息:")
                print("学号:", node._id)
                print("姓名:", node._name)
                print("生日:", node._birthday)
                print("性别:", node._sex)
                print("照片:", node._photo)
                print("民族:", node._nation)
                print("爱好:", node._hobby)
                print("索引:", node._index)
            else:
                print("未找到对应学号的信息！")

        elif choice == "4":
            # 显示所有信息
            if friends_link.is_empty():
                print("链表为空，没有信息！")
            else:
                print("所有信息如下:")
                p = friends_link.head._next
                while p:
                    print("学号:", p._id)
                    print("姓名:", p._name)
                    print("生日:", p._birthday)
                    print("性别:", p._sex)
                    print("照片:", p._photo)
                    print("民族:", p._nation)
                    print("爱好:", p._hobby)
                    print("索引:", p._index)
                    print("----------------------")
                    p = p._next

        elif choice == "5":
            # 退出程序
            print("谢谢使用，再见！")
            break

        else:
            print("无效的选择，请重新输入！")


# 在程序入口调用main函数
if __name__ == "__main__":
    main()


