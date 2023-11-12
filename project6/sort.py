import random
import time
import copy
import sys
import sys


from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QApplication, QGraphicsScene, QGraphicsPixmapItem
from PyQt6.QtWidgets import QPushButton

from sorting import Ui_Form as u
sys.setrecursionlimit(20000)#   解除递归使用次数限制

#   冒泡排序
def bubble_sort(nums):
    lens = len(nums)
    for i in range(lens - 1):
        for j in range(lens - 1 - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

#  快速排序
def quick_sort(nums):
    lens = len(nums)
    if len(nums) <= 1:
        return nums
    p = nums[lens // 2]
    l = [x for x in nums if x < p]
    m = [x for x in nums if x == p]
    r = [x for x in nums if x > p]
    return quick_sort(l) + m + quick_sort(r)

#快速排序2
def QuickSort(li, left, right):
    def partition(li, left, right):
        random_index = random.randrange(left, right)
        li[left], li[random_index] = li[random_index], li[left]
        temp = li[left]
        while left < right:
            while li[right] > temp and left < right:
                right -= 1
            li[left] = li[right]
            while li[left] <= temp and left < right:
                left += 1
            li[right] = li[left]
        li[left] = temp
        return left

    if left < right:
        mid = partition(li, left, right)
        QuickSort(li, left, mid-1)
        QuickSort(li, mid+1, right)

    return li

#归并排序
def MergeSort(li, low, high):
    def merge(li, low, mid, high):
        temp = []
        i = low
        j = mid + 1
        while i <= mid and j <= high:
            if li[i] < li[j]:
                temp.append(li[i])
                i += 1
            else:
                temp.append(li[j])
                j += 1
        while i <= mid:
            temp.append(li[i])
            i += 1
        while j <= high:
            temp.append(li[j])
            j += 1
        li[low:high+1]=temp
    if low < high:
        mid = (low+high)//2
        MergeSort(li, low, mid)
        MergeSort(li, mid + 1, high)
        merge(li,low, mid,high)
    return li

#   希尔排序
def shell_sort(nums):
    lens = len(nums)
    gap = lens // 2
    while gap > 0:
        for i in range(gap, lens):
            t = nums[i]
            j = i
            while j >= gap and nums[j - gap] > t:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = t
        gap //= 2

#   堆排序
##  堆
def heap(nums, n, i):
    largest = i
    l = 2 * i + 1   # 左子树
    r = 2 * i + 2   # 右子树
    if l < n and nums[l] > nums[largest]:   #   比较根结点和左子树
        largest = l
    if r < n and nums[r] > nums[largest]:
        largest = r
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heap(nums, n, largest)

##  堆排序
def heap_sort(nums):
    n = len(nums)
    # 建立最大堆
    for i in range(n // 2 - 1, -1, -1):   #  用于从最后一个非叶子节点开始，逐个向上调整子树，以构建最大堆。
        heap(nums, n, i)
    # 逐个提取最大值，并进行堆调整
    for i in range(n - 1, 0, -1):
         nums[0], nums[i] = nums[i], nums[0]  # 将当前最大值移到数组堆最后面
         heap(nums, i, 0)  # 调整堆

#   基数排序
def counting_sort(nums, e):
    lens = len(nums)
    output = [0] * lens  #   输出数组
    cnt = [0] * 10  #计数数组

    for i in range(lens):
        index = nums[i] // e
        cnt[index % 10] += 1    # 统计每个数字出现的次数

    for i in range(1, 10):
        cnt[i] += cnt[i - 1]     # 将计数数组转换为每个数字在输出数组中的位置

    # 构建排序后的输出数组
    i = lens - 1
    while i >= 0:
        index = nums[i] // e
        output[cnt[index % 10] - 1] = nums[i]
        cnt[index % 10] -= 1
        i -= 1

    for i in range(lens):
        nums[i] = output[i] # 将排序后的数组复制回原始数组

def radix_sort(nums):
    maxi = max(nums)    # 获取数组中的最大值
    e = 1   # 从个位开始

    while maxi // e > 0:
        counting_sort(nums, e)
        e *= 10

class MySort(QMainWindow, u):
    signal = pyqtSignal(str)
    def __init__(self, parent = None):
        super(MySort, self).__init__(parent)
        self.setupUi(self)
        self.connecter()

    def connecter(self):    #把函数与对应按钮相连接
        self.generatedata.clicked.connect(self.generate)
        self.beginsort.clicked.connect(self.sortall)

    def generate(self):#   生成排序数据
        i = 0
        self.nums = []
        while (i < 10000):
            self.nums.append(random.randint(0, 10000))
            i = i + 1
        strr = ', '.join([str(element) for element in self.nums])   # 去掉[]
        self.textEdit.setText(strr)
        self.bubblesort.clear()
        self.quicksort.clear()
        self.shellsort.clear()
        self.heapsort.clear()
        self.radixsort.clear()
        self.comparetime.clear()


    def sortall(self):
        times = {}
        # 冒泡排序
        nums = self.nums
        nums1 = copy.deepcopy(nums)  # 深拷贝
        start = time.perf_counter()  # 开始时间
        bubble_sort(nums1)  # 算法函数
        end = time.perf_counter()  # 结束时间
        time1 = (end - start)
        times['冒泡排序'] = time1
        strr =  ', '.join([str(element) for element in nums1])   # 去掉[]
        self.bubblesort.setText(str(time1)[:10])
        self.textEdit.setText(str(strr))

        # 快速排序
        nums2 = copy.deepcopy(nums)
        start = time.perf_counter()  # 开始时间
        quick_sort(nums2)  # 算法函数
        end = time.perf_counter()  # 结束时间
        time2 = (end - start)
        times['快速排序'] = time2
        self.quicksort.setText(str(time2)[:10])

        # 希尔排序
        nums3 = copy.deepcopy(nums)
        start = time.perf_counter()  # 开始时间
        shell_sort(nums3)  # 算法函数
        end = time.perf_counter()  # 结束时间
        time3 = (end - start)
        times['希尔排序'] = time3
        self.shellsort.setText(str(time3)[:10])

        # 堆排序
        nums4 = copy.deepcopy(nums)
        start = time.perf_counter()  # 开始时间
        heap_sort(nums4)  # 算法函数
        end = time.perf_counter()  # 结束时间
        time4 = (end - start)
        times['堆排序'] = time4
        self.heapsort.setText(str(time4)[:10])

        # 基数排序
        nums5 = copy.deepcopy(nums)
        start = time.perf_counter()  # 开始时间
        radix_sort(nums5)  # 算法函数
        end = time.perf_counter()  # 结束时间
        time5 = (end - start)
        times['基数排序'] = time5
        self.radixsort.setText(str(time5)[:10])

        #比较用时
        sortedtimes = sorted(times.keys(), key=lambda x: times[x], reverse=True)

        # 构建输出字符串
        str1 = ""
        for i, key in enumerate(sortedtimes):
            str1 += key
            if i < len(sortedtimes) - 1:
                str1 += "  >  "

        self.comparetime.setText(str1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MySort()
    win.show()
    sys.exit(app.exec())





