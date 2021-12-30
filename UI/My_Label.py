'''
Author: NWPU python group
Date: 2021-12-28 18:39:38
LastEditTime: 2021-12-30 02:48:38
LastEditor: wqy
Description: file content
'''


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2 as cv


class MyLabel(QtWidgets.QLabel):
    # 继承Qlabel类，重写鼠标和滚轮事件，重写绘制事件
    def __init__(self, Frame):
        super(MyLabel, self).__init__()
        self.cur_img = ""
        self.img_w = ""
        self.img_h = ""
        self.left_flag = False
        self.right_flag = False
        self.label_x = 0  # label当前坐标
        self.label_y = 0
        self.mouse_mv_x = ""  # 鼠标移动上一次坐标
        self.mouse_mv_y = ""
        self.label_wid = self.width()
        self.label_hig = self.height()
        self.image = None

        self.last_x = ""  # 画画上一个点坐标
        self.last_y = ""
        self.mouse_mv_x1 = ""  # 中转点
        self.mouse_mv_y1 = ""
        self.resize_point = 10

        self.x0 = 0
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0
        self.flag2 = False  # 裁剪模式标志位
        self.erase_flag = False  # 是否清除标志位
        self.paint_flag = False  # 是否绘制标志位

    def mousePressEvent(self, event):
        # 鼠标按下事件
        if event.buttons() == QtCore.Qt.LeftButton:
            if self.flag2 == True:
                self.left_flag = True  # 左键按下
                self.erase_flag = False  # 不可执行清除
                self.x0 = event.x()  # 获取坐标
                self.y0 = event.y()
        if event.buttons() == QtCore.Qt.RightButton:
            self.right_flag = True  # 右键按下

    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        self.left_flag = False  # 左键松开
        self.erase_flag = True  # 左键松开后绘制不可清除 ##
        self.right_flag = False  # 右键松开
        self.mouse_mv_y = ""  # 重置移动坐标
        self.mouse_mv_x = ""
        self.last_x = ""
        self.last_y = ""

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        if self.flag2 == True:
            if self.left_flag:  # 鼠标左击
                # 获取移动坐标
                if event.x() >= 0:
                    self.x1 = event.x() if event.x() < self.width() else self.width()
                else:
                    self.x1 = 0
                if event.y() >= 0:
                    self.y1 = event.y() if event.y() < self.height() else self.height()
                else:
                    self.y1 = 0
                # 更新触发paint事件
                self.update()

        if self.right_flag:  # 鼠标右击
            # 获取右键移动量
            self.x1 = event.x()
            self.y1 = event.y()
            if self.mouse_mv_x != "" and self.mouse_mv_y != "":
                self.label_x = self.label_x + (self.x1 - self.mouse_mv_x)
                self.label_y = self.label_y + (self.y1 - self.mouse_mv_y)
            self.mouse_mv_x = self.x1
            self.mouse_mv_y = self.y1
            # 改变label位置，并在对应位置生成等大的label
            self.setGeometry(self.label_x, self.label_y,
                             self.width(), self.height())

    def wheelEvent(self, event):
        # 滚轮缩放事件
        self.angle = event.angleDelta() / 8  # 滚轮滚动的角度
        self.angleY = self.angle.y()  # +-15
        if self.angleY > 0:                         # 15向上滚动
            if self.resize_point < 25:  # 放大上下限
                self.resize_point += 1  # 向上滚动，放缩系数+1
        if self.angleY < 0:                         # -15向下滚动
            if self.resize_point > 3:  # 缩小上下限
                self.resize_point -= 1  # 向下滚动，放缩系数-1
        # 使用opencv resize图片
        self.cur_resimg = cv.resize(self.image, (int(
            self.image.shape[1]*self.resize_point/10), int(self.image.shape[0]*self.resize_point/10)))  # 图片按10%作为比例进行放缩
        self.cur_reslab_shape = self.cur_resimg.shape
        # opecncv读取后为BGR，因此转RGB格式，以在Qlabel中显示
        img2 = cv.cvtColor(self.cur_resimg, cv.COLOR_BGR2RGB)
        QImage = QtGui.QImage(
            img2, self.cur_reslab_shape[1], self.cur_reslab_shape[0], 3*self.cur_reslab_shape[1], QtGui.QImage.Format_RGB888)
        self._pixmap = QtGui.QPixmap(QImage).scaled(
            self.cur_reslab_shape[1], self.cur_reslab_shape[0], QtCore.Qt.KeepAspectRatio)

        self.label_wid = self.cur_reslab_shape[1]  # label宽度指针
        self.label_hig = self.cur_reslab_shape[0]  # label高度指针
        # 在上次移动后位置缩放图片
        self.setGeometry(QtCore.QRect(
            self.label_x, self.label_y, self.label_wid, self.label_hig))
        self.setPixmap(self._pixmap)

    def set_coordinate(self, pic):
        # 在上次移动后的坐标设置label为上次调整后的大小，显示图片
        self.setGeometry(QtCore.QRect(self.label_x, self.label_y,
                         self.width(), self.height()))
        self.setPixmap(pic)
        self._pixmap = pic

    def paintEvent(self, event):
        # 绘制事件
        super().paintEvent(event)
        if self.flag2:  # 在裁剪模式内
            if self.erase_flag == False:  # 如果没按下cancel
                self.paint_flag = True  # 已绘制
                self.rect = QtCore.QRect(self.x0, self.y0, self.x1 -
                                         self.x0, self.y1 - self.y0)
                painter = QtGui.QPainter(self)
                painter.setPen(QtGui.QPen(
                    QtCore.Qt.red, 2, QtCore.Qt.SolidLine))
                painter.drawRect(self.rect)  # 绘制矩形区域

    def erase(self):
        # 清除绘制
        self.erase_flag = True  # 允许清除
        self.paint_flag = False
        self.update()  # 进入绘制事件（会强制重画）


class MyLabel_2(QtWidgets.QLabel):
    # 对比My_label来说，只保留了绘制裁剪功能
    def __init__(self, Frame):
        super(MyLabel_2, self).__init__()
        self.x0 = 0
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0
        self.flag = False
        self.flag2 = False
        self.erase_flag = False
        self.paint_flag = False

    # 鼠标点击事件

    def mousePressEvent(self, event):
        self.flag = True
        self.erase_flag = False
        self.x0 = event.x()
        self.y0 = event.y()

    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        self.flag = False
        self.erase_flag = False

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        if self.flag:
            if event.x() >= 0:
                self.x1 = event.x() if event.x() < self.width() else self.width()
            else:
                self.x1 = 0
            if event.y() >= 0:
                self.y1 = event.y() if event.y() < self.height() else self.height()
            else:
                self.y1 = 0
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.flag2:
            if self.erase_flag == False:
                self.paint_flag = True
                self.rect = QtCore.QRect(self.x0, self.y0, self.x1 -
                                         self.x0, self.y1 - self.y0)
                painter = QtGui.QPainter(self)
                painter.setPen(QtGui.QPen(
                    QtCore.Qt.red, 2, QtCore.Qt.SolidLine))
                painter.drawRect(self.rect)

    def erase(self):
        self.erase_flag = True
        self.paint_flag = False
        self.update()
