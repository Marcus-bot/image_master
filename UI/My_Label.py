from PyQt5 import QtCore, QtGui, QtWidgets
import cv2 as cv


class My_Label(QtWidgets.QLabel):
    def __init__(self, Frame):
        super(My_Label, self).__init__()
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
        self.left_flag = False
        self.flag2 = False
        self.erase_flag = False
        self.paint_flag = False

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.left_flag = True
            self.erase_flag = False
            self.x0 = event.x()
            self.y0 = event.y()
        if event.buttons() == QtCore.Qt.RightButton:
            self.right_flag = True

    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        self.left_flag = True
        self.erase_flag = False
        self.right_flag = False
        self.mouse_mv_y = ""
        self.mouse_mv_x = ""
        self.last_x = ""
        self.last_y = ""

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        if self.left_flag:  # 鼠标左击
            if event.x() >= 0:
                self.x1 = event.x() if event.x() < self.width() else self.width()
            else:
                self.x1 = 0
            if event.y() >= 0:
                self.y1 = event.y() if event.y() < self.height() else self.height()
            else:
                self.y1 = 0
            self.update()

        if self.right_flag:  # 鼠标右击
            self.x1 = event.x()
            self.y1 = event.y()
            if self.mouse_mv_x != "" and self.mouse_mv_y != "":
                self.label_x = self.label_x + (self.x1 - self.mouse_mv_x)
                self.label_y = self.label_y + (self.y1 - self.mouse_mv_y)
            self.mouse_mv_x = self.x1
            self.mouse_mv_y = self.y1
            self.setGeometry(self.label_x, self.label_y,
                             self.width(), self.height())

    def wheelEvent(self, event):
        self.angle = event.angleDelta() / 8  # 滚轮滚动的角度
        self.angleY = self.angle.y()  # +-15
        if self.angleY > 0:                         # 15向上滚动
            if self.resize_point < 25:  # 放大上下限
                self.resize_point += 1  # 向上滚动，放缩系数+1
        if self.angleY < 0:                         # -15向下滚动
            if self.resize_point > 3:  # 缩小上下限
                self.resize_point -= 1  # 向下滚动，放缩系数-1

        self.cur_resimg = cv.resize(self.image, (int(
            self.image.shape[1]*self.resize_point/10), int(self.image.shape[0]*self.resize_point/10)))  # 图片按10%作为比例进行放缩
        self.cur_reslab_shape = self.cur_resimg.shape
        # 转RGB格式，以在Qlabel中显示
        img2 = cv.cvtColor(self.cur_resimg, cv.COLOR_BGR2RGB)
        QImage = QtGui.QImage(
            img2, self.cur_reslab_shape[1], self.cur_reslab_shape[0], 3*self.cur_reslab_shape[1], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap(QImage).scaled(
            self.cur_reslab_shape[1], self.cur_reslab_shape[0], QtCore.Qt.KeepAspectRatio)

        self.label_wid = self.cur_reslab_shape[1]  # label宽度指针
        self.label_hig = self.cur_reslab_shape[0]  # label高度指针
        self.setGeometry(QtCore.QRect(
            self.label_x, self.label_y, self.label_wid, self.label_hig))
        self.setPixmap(pixmap)
        # 图片缩放指针，代表图片被缩放（由于打开文件夹和切换文件夹中图片时，显示图片是自适应的，缩放是按原图进行缩放的，所以必须区别对待）
        self.has_been_chgd = True

    def set_coordinate(self, pic):
        self.setGeometry(QtCore.QRect(self.label_x, self.label_y,
                         self.width(), self.height()))
        self.setPixmap(pic)
        self.has_been_chgd = True

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


class MyLabel_2(QtWidgets.QLabel):
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
