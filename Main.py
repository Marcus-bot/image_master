import sys
import cv2
from UI.UI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget
from PyQt5.QtGui import QPixmap
from command import *
import Transfer_Image_style.ProcessCore as Core
from UI.My_Label import *


class My_Mainwindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(My_Mainwindow, self).__init__()
        self.setupUi(self)
# ---------------------定义一个自己的Label:My_Label------------------------------------
        self.label_processed = My_Label(
            self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_processed.sizePolicy().hasHeightForWidth())
        self.label_processed.setSizePolicy(sizePolicy)
        self.label_processed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_processed.setObjectName("label_processed")
        self.gridLayout_2.addWidget(self.label_processed, 0, 0, 1, 1)

        _translate = QtCore.QCoreApplication.translate
        self.label_processed.setText(_translate("MainWindow", "处理后的图像"))
# ---------------------定义一个自己的Label:My_Label------------------------------------

        self.cmdbar = None
        self.actionOpen.triggered.connect(self.openimage)
        self.actionSave.triggered.connect(self.saveimage)
        self.pushButton_Adjust.clicked.connect(self.Adjust_UI)
        self.pushButton_EdgeSelect.clicked.connect(self.EdgeSelect_UI)
        self.pushButton_Smooth.clicked.connect(self.Smooth_UI)
        self.pushButton_Bin.clicked.connect(self.Bin_UI)
        self.pushButton_ChannelSelect.clicked.connect(self.Channel_UI)
        self.pushButton_contour.clicked.connect(self.Contour_UI)
        self.pushButton_Trans.clicked.connect(self.Transfer_UI)
        self.pushButton_Cut.clicked.connect(self.Cut_UI)
        self.pushButton_lines.clicked.connect(self.Lines_UI)
        self.pushButton_circle.clicked.connect(self.Circle_UI)
        self.pushButton_rot.clicked.connect(self.Rot_UI)

# --------------------------------------------------------------------------------

    def openimage(self):
        image_path, imgType = QFileDialog.getOpenFileName(
            self, "打开图片", "img", "*.jpg;*.tif;*.png;;All Files(*)")
        if image_path == '':
            return 0

        self.image_toshow = QPixmap(image_path).scaled(
            self.label_origin.width(), self.label_origin.height(), QtCore.Qt.KeepAspectRatio)

        self.image_now = cv2.imread(image_path)
        self.image_origin = cv2.imread(image_path)
        self.TempPath = 'TEMP/Temp_last.jpg'
        cv2.imwrite(self.TempPath, self.image_now)
        Path = 'TEMP/Temp_origin.jpg'
        self.label_origin.setPixmap(self.image_toshow)
        self.show_msg('打开成功')

    def saveimage(self):
        FileDir = QFileDialog.getSaveFileName(
            self, "保存图片", "img", "*.jpg;*.tif;*.png;;All Files(*)")
        if FileDir[0] == '':  # bug 点击取消也会要求输入名字
            tips = QMessageBox.question(
                self, 'Message', 'Please input the name!', QMessageBox.Yes, QMessageBox.Yes)
            return 0
        img = self.image_toshow
        img.save(FileDir[0])

    def save_Temp(self):  # 暂时保存修改
        try:
            self.image_now = self.image_temp
            self.TempPath = 'TEMP/Temp_last.jpg'
            cv2.imwrite(self.TempPath, self.image_temp)
        except:
            pass

    def processed_show(self, image):
        path = 'TEMP\Temp.jpg'
        cv2.imwrite(path, image)
        self.image_toshow = QPixmap(path).scaled(
            self.label_processed.label_wid, self.label_processed.label_hig, QtCore.Qt.KeepAspectRatio)
        self.label_processed.set_coordinate(self.image_toshow)
        self.label_processed.image = image

    def cancel_Temp(self):
        # try:
        # self.image_temp = self.image_now
        # self.TempPath = 'TEMP/Temp_last.jpg'
        # cv2.imwrite(self.TempPath)
        self.processed_show(self.image_now)

        # self.cmdbar.gridLayout_cmd.deleteLater()
        self.cmdbar.gridLayoutWidget_cmd.deleteLater()
        self.image_temp = self.image_now
        self.cmdbar = None
        # except:
        #     pass

    def is_opened(self):  # 判断有没有打开图片
        try:
            self.image_toshow
        except:
            tips = QMessageBox.question(
                self, 'Message', 'Please open an image!', QMessageBox.Yes, QMessageBox.Yes)
            return False
        else:
            return True

    def show_msg(self, Msg):
        self.textBrowser_Msg.append('<span style=\" color:#f8f8f8;\">'+Msg)
        self.textBrowser_Msg.moveCursor(self.textBrowser_Msg.textCursor().End)

    def show_his(self, His):
        self.textBrowser_His.append('<span style=\" color:#f8f8f8;\">'+His)
        self.textBrowser_His.moveCursor(self.textBrowser_His.textCursor().End)
# --------------------------------------亮度对比度----------------------------------

    def Adjust_UI(self):
        if self.cmdbar == None:
            if self.is_opened() == True:
                self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
                self.gridLayoutWidget.setGeometry(
                    QtCore.QRect(10, 30, 991, 321))
                self.gridLayoutWidget.setObjectName("gridLayoutWidget")
                self.gridLayoutWidget.show()
                self.cmdbar = cmd_Adjust(self.gridLayoutWidget)
                self.cmdbar.horizontalSlider_a.valueChanged.connect(
                    self.Adjust_core)
                self.cmdbar.horizontalSlider_b.valueChanged.connect(
                    self.Adjust_core)
                self.cmdbar.lineEdit_a.editingFinished.connect(
                    self.Adjust_core)
                self.cmdbar.lineEdit_b.editingFinished.connect(
                    self.Adjust_core)
                self.cmdbar.adjust_yes.clicked.connect(self.save_Temp)
                self.cmdbar.adjust_no.clicked.connect(self.cancel_Temp)
                self.cmdbar.horizontalSlider_a.sliderReleased.connect(
                    self.Adjust_released)
                self.cmdbar.horizontalSlider_b.sliderReleased.connect(
                    self.Adjust_released)

    def Adjust_core(self):
        self.image_temp = Core.Image_Adjust(
            self.image_now, self.cmdbar.a, self.cmdbar.b)
        # self.TempPath = 'TEMP/Temp.jpg'
        # cv2.imwrite(self.TempPath, self.image_temp)
        self.processed_show(self.image_temp)

    def Adjust_released(self):
        self.show_msg('调整成功')
        self.show_his('调整: 对比度 '+str(self.cmdbar.a)+" 亮度: "+str(self.cmdbar.b))
# --------------------------------------边缘检测----------------------------------

    def EdgeSelect_UI(self):
        if self.cmdbar == None:
            if self.is_opened() == True:
                self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
                self.gridLayoutWidget.setGeometry(
                    QtCore.QRect(10, 30, 991, 321))
                self.gridLayoutWidget.setObjectName("gridLayoutWidget")
                self.gridLayoutWidget.show()
                self.cmdbar = Edge_Select(self.gridLayoutWidget)
                self.cmdbar.horizontalSlider_a.valueChanged.connect(
                    self.EdgeSelect_core)
                self.cmdbar.horizontalSlider_b.valueChanged.connect(
                    self.EdgeSelect_core)
                self.cmdbar.horizontalSlider_a.sliderReleased.connect(
                    self.EdgeSelect_released)
                self.cmdbar.horizontalSlider_b.sliderReleased.connect(
                    self.EdgeSelect_released)
                self.cmdbar.adjust_yes.clicked.connect(self.save_Temp)
                self.cmdbar.adjust_no.clicked.connect(self.cancel_Temp)

    def EdgeSelect_core(self):
        self.image_temp = Core.CannyEdge_detect(
            self.image_now, self.cmdbar.a, self.cmdbar.b, 1)  # 1是啥？？算法里没用
        # self.TempPath = 'TEMP/Temp.jpg'
        # cv2.imwrite(self.TempPath, self.image_temp)
        self.processed_show(self.image_temp)

    def EdgeSelect_released(self):
        self.show_msg('边缘检测成功')
        self.show_his('边缘检测: 最小阈值: '+str(self.cmdbar.a) +
                      " 最大阈值: "+str(self.cmdbar.b))
# --------------------------------------平滑滤波----------------------------------

    def Smooth_UI(self):
        if self.cmdbar == None:
            if self.is_opened() == True:
                self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
                self.gridLayoutWidget.setGeometry(
                    QtCore.QRect(10, 30, 991, 321))
                self.gridLayoutWidget.setObjectName("gridLayoutWidget")
                self.gridLayoutWidget.show()
                self.cmdbar = Smooth_Image(self.gridLayoutWidget)
                self.cmdbar.horizontalSlider_a.valueChanged.connect(
                    self.Smooth_core)
                self.cmdbar.horizontalSlider_a.sliderReleased.connect(
                    self.Smooth_released)
                self.cmdbar.adjust_yes.clicked.connect(self.save_Temp)
                self.cmdbar.adjust_no.clicked.connect(self.cancel_Temp)

    def Smooth_core(self):
        self.image_temp = Core.Image_Blur(
            self.image_now, self.cmdbar.a, self.cmdbar.c)
        # self.TempPath = 'TEMP/Temp.jpg'
        # cv2.imwrite(self.TempPath, self.image_temp)
        self.processed_show(self.image_temp)

    def Smooth_released(self):
        self.show_msg('平滑滤波成功')
        self.show_his('平滑滤波 滤波阶数: '+str(self.cmdbar.a) +
                      " 滤波器: "+self.cmdbar.choice)
# ---------------------------------------二值化---------------------------------

    def Bin_UI(self):
        if self.cmdbar == None:
            if self.is_opened() == True:
                self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
                self.gridLayoutWidget.setGeometry(
                    QtCore.QRect(10, 30, 991, 321))
                self.gridLayoutWidget.setObjectName("gridLayoutWidget")
                self.gridLayoutWidget.show()
                self.cmdbar = Bin_Image(self.gridLayoutWidget)
                self.cmdbar.horizontalSlider_a.valueChanged.connect(
                    self.Bin_core)
                self.cmdbar.horizontalSlider_a.sliderReleased.connect(
                    self.Bin_released)
                self.cmdbar.adjust_yes.clicked.connect(self.save_Temp)
                self.cmdbar.adjust_no.clicked.connect(self.cancel_Temp)

    def Bin_core(self):
        self.image_temp = Core.Image_Binarization(
            self.image_now, self.cmdbar.a, 1)
        # self.TempPath = 'TEMP/Temp.jpg'
        # cv2.imwrite(self.TempPath, self.image_temp)
        self.processed_show(self.image_temp)

    def Bin_released(self):
        self.show_msg('二值化成功')
        self.show_his('二值化 阈值: '+str(self.cmdbar.a))
# ----------------------------------------通道提取--------------------------------

    def Channel_UI(self):
        if self.cmdbar == None:
            if self.is_opened() == True:
                self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
                self.gridLayoutWidget.setGeometry(
                    QtCore.QRect(10, 30, 991, 321))
                self.gridLayoutWidget.setObjectName("gridLayoutWidget")
                self.gridLayoutWidget.show()
                self.cmdbar = Channel_Select(self.gridLayoutWidget)
                self.cmdbar.checkBox_r.stateChanged.connect(
                    self.ChannelSelect_core)
                self.cmdbar.checkBox_g.stateChanged.connect(
                    self.ChannelSelect_core)
                self.cmdbar.checkBox_b.stateChanged.connect(
                    self.ChannelSelect_core)

                self.cmdbar.checkBox_r.stateChanged.connect(
                    self.ChannelSelect_released)
                self.cmdbar.checkBox_g.stateChanged.connect(
                    self.ChannelSelect_released)
                self.cmdbar.checkBox_b.stateChanged.connect(
                    self.ChannelSelect_released)
                self.cmdbar.adjust_yes.clicked.connect(self.save_Temp)
                self.cmdbar.adjust_no.clicked.connect(self.cancel_Temp)
                self.cmdbar.verticalSlider_r.valueChanged.connect(
                    self.ChannelSelect_core)
                self.cmdbar.verticalSlider_g.valueChanged.connect(
                    self.ChannelSelect_core)
                self.cmdbar.verticalSlider_b.valueChanged.connect(
                    self.ChannelSelect_core)
                self.cmdbar.verticalSlider_r.sliderReleased.connect(
                    self.ChannelSelect_released)
                self.cmdbar.verticalSlider_g.sliderReleased.connect(
                    self.ChannelSelect_released)
                self.cmdbar.verticalSlider_b.sliderReleased.connect(
                    self.ChannelSelect_released)

    def ChannelSelect_core(self):
        self.image_temp = Core.Channel_Select(
            self.image_now, self.cmdbar.r, self.cmdbar.g, self.cmdbar.b)
        # self.TempPath = 'TEMP/Temp.jpg'
        # cv2.imwrite(self.TempPath, self.image_temp)
        self.processed_show(self.image_temp)

    def ChannelSelect_released(self):
        self.show_msg('提取通道')
        text = 'r:{:.2f} g:{:.2f} b:{:.2f}'.format(
            self.cmdbar.r, self.cmdbar.g, self.cmdbar.b)
        self.show_his('选择通道: '+text)
        text = ''
# ------------------------------------------轮廓检测------------------------------

    def Contour_UI(self):
        if self.cmdbar == None:
            if self.is_opened() == True:
                self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
                self.gridLayoutWidget.setGeometry(
                    QtCore.QRect(10, 30, 991, 321))
                self.gridLayoutWidget.setObjectName("gridLayoutWidget")
                self.gridLayoutWidget.show()
                self.cmdbar = Contour_Detect(self.gridLayoutWidget)
                self.cmdbar.adjust_yes.clicked.connect(self.save_Temp)
                self.cmdbar.adjust_no.clicked.connect(self.cancel_Temp)
                self.cmdbar.horizontalSlider_width.valueChanged.connect(
                    self.ContourDetect_core)
                self.cmdbar.horizontalSlider_width.sliderReleased.connect(
                    self.ContourDetect_released)

    def ContourDetect_core(self):
        self.image_temp = Core.contour_detect(
            self.image_now, self.cmdbar.width)
        # self.TempPath = 'TEMP/Temp.jpg'
        # cv2.imwrite(self.TempPath, self.image_temp)
        self.processed_show(self.image_temp)

    def ContourDetect_released(self):
        self.show_msg('轮廓检测')
        self.show_his('轮廓检测:线条宽度 '+str(self.cmdbar.width))

# ------------------------------------------风格迁移------------------------------

    def Transfer_UI(self):
        if self.cmdbar == None:
            if self.is_opened() == True:
                self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
                self.gridLayoutWidget.setGeometry(
                    QtCore.QRect(10, 30, 991, 321))
                self.gridLayoutWidget.setObjectName("gridLayoutWidget")
                self.gridLayoutWidget.show()
                self.cmdbar = Style_Transfer(self.gridLayoutWidget)
                self.cmdbar.adjust_yes.clicked.connect(self.save_Temp)
                self.cmdbar.adjust_no.clicked.connect(self.cancel_Temp)
                self.cmdbar.horizontalSlider_style.valueChanged.connect(
                    self.Transfer_core)
                self.cmdbar.comboBox_style.currentTextChanged.connect(
                    self.Transfer_core)
                self.cmdbar.comboBox_style.currentTextChanged.connect(
                    self.Transfer_released)
                self.cmdbar.horizontalSlider_style.sliderReleased.connect(
                    self.Transfer_released)

    def Transfer_core(self):
        self.image_temp = Core.style_transfer(
            self.image_now, self.cmdbar.model, self.cmdbar.f)
        self.processed_show(self.image_temp)

    def Transfer_released(self):
        self.show_msg('风格迁移 成功')
        self.show_his('风格迁移: '+self.cmdbar.choice)

# ------------------------------------------裁剪---------------------------------

    def Cut_UI(self):
        if self.cmdbar == None:
            if self.is_opened() == True:
                self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
                self.gridLayoutWidget.setGeometry(
                    QtCore.QRect(10, 30, 991, 321))
                self.gridLayoutWidget.setObjectName("gridLayoutWidget")
                self.gridLayoutWidget.show()
                self.cmdbar = Cut_Image(self.gridLayoutWidget)
                self.cmdbar.adjust_yes.clicked.connect(self.Cut_core)
                self.cmdbar.adjust_yes.clicked.connect(self.save_Temp)
                self.cmdbar.adjust_no.clicked.connect(self.cancel_Temp)
                self.cmdbar.adjust_yes.clicked.connect(self.Cut_Released)
                self.cmdbar.adjust_no.clicked.connect(self.Cut_Released)
                self.cmdbar.adjust_no.clicked.connect(self.Cut_Off)
                self.label_origin.flag2 = True
                self.label_processed.flag2 = True

    def Cut_core(self):
        if self.label_origin.paint_flag == True:
            img = self.image_origin
            width_old = img.shape[1]
            k = width_old / self.image_toshow.width()
            x0 = int((self.label_origin.x0 - (self.label_origin.width() -
                                              self.image_toshow.width()) / 2) * k)
            x1 = int((self.label_origin.x1 - (self.label_origin.width() -
                                              self.image_toshow.width()) / 2) * k)
            y0 = int((self.label_origin.y0 - (self.label_origin.height() -
                                              self.image_toshow.height()) / 2) * k)
            y1 = int((self.label_origin.y1 - (self.label_origin.height() -
                                              self.image_toshow.height()) / 2) * k)
            self.image_temp = img[y0:y1, x0:x1]
            self.processed_show(self.image_temp)
            self.show_msg('裁剪成功')
            self.show_his('裁剪尺寸: x:{} y:{}'.format(x1-x0, y1-y0))

        if self.label_processed.paint_flag == True:
            img = self.image_temp
            width_old = img.shape[1]
            k = width_old / self.image_toshow.width()
            x0 = int((self.label_processed.x0 - (self.label_processed.width() -
                                                 self.image_toshow.width()) / 2) * k)
            x1 = int((self.label_processed.x1 - (self.label_processed.width() -
                                                 self.image_toshow.width()) / 2) * k)
            y0 = int((self.label_processed.y0 - (self.label_processed.height() -
                                                 self.image_toshow.height()) / 2) * k)
            y1 = int((self.label_processed.y1 - (self.label_processed.height() -
                                                 self.image_toshow.height()) / 2) * k)
            self.image_temp = img[y0:y1, x0:x1]
            self.processed_show(self.image_temp)
            self.show_msg('裁剪成功')
            self.show_his('裁剪尺寸: x:{} y:{}'.format(x1-x0, y1-y0))

    def Cut_Released(self):
        self.label_origin.erase()
        self.label_processed.erase()
        pass

    def Cut_Off(self):
        self.label_origin.flag2 = False
        self.label_processed.flag2 = False
# ------------------------------------------直线检测---------------------------------

    def Lines_UI(self):
        if self.cmdbar == None:
            if self.is_opened() == True:
                self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
                self.gridLayoutWidget.setGeometry(
                    QtCore.QRect(10, 30, 991, 321))
                self.gridLayoutWidget.setObjectName("gridLayoutWidget")
                self.gridLayoutWidget.show()
                self.cmdbar = Lines_Detect(self.gridLayoutWidget)
                self.cmdbar.horizontalSlider_a.valueChanged.connect(
                    self.Lines_core)
                self.cmdbar.horizontalSlider_b.valueChanged.connect(
                    self.Lines_core)
                self.cmdbar.adjust_yes.clicked.connect(self.save_Temp)
                self.cmdbar.adjust_no.clicked.connect(self.cancel_Temp)
                self.cmdbar.horizontalSlider_a.sliderReleased.connect(
                    self.Lines_released)
                self.cmdbar.horizontalSlider_b.sliderReleased.connect(
                    self.Lines_released)

    def Lines_core(self):
        self.image_temp = Core.HoughLines_detect(
            self.image_now, self.cmdbar.a, self.cmdbar.b)
        self.processed_show(self.image_temp)

    def Lines_released(self):
        self.show_msg('直线检测完成')
        self.show_his('直线最小长度:{} 最大宽度:{}'.format(self.cmdbar.a, self.cmdbar.b))

# ------------------------------------------旋转---------------------------------
    def Rot_UI(self):
        if self.cmdbar == None:
            if self.is_opened() == True:
                self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
                self.gridLayoutWidget.setGeometry(
                    QtCore.QRect(10, 30, 991, 321))
                self.gridLayoutWidget.setObjectName("gridLayoutWidget")
                self.gridLayoutWidget.show()
                self.cmdbar = Rot_Image(self.gridLayoutWidget)
                self.cmdbar.adjust_yes.clicked.connect(self.save_Temp)
                self.cmdbar.adjust_no.clicked.connect(self.cancel_Temp)
                self.cmdbar.pushButton_left.clicked.connect(self.Rot_core)
                self.cmdbar.pushButton_right.clicked.connect(self.Rot_core)

    def Rot_core(self):
        self.image_temp = Core.Rotate_image(self.image_now, self.cmdbar.angle)
        self.processed_show(self.image_temp)
        self.show_msg('旋转完成')
        self.show_his('旋转')


# ------------------------------------------圆形检测---------------------------------

    def Circle_UI(self):
        if self.cmdbar == None:
            if self.is_opened() == True:
                self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
                self.gridLayoutWidget.setGeometry(
                    QtCore.QRect(10, 30, 991, 321))
                self.gridLayoutWidget.setObjectName("gridLayoutWidget")
                self.gridLayoutWidget.show()
                self.cmdbar = Circle_Detect(self.gridLayoutWidget)
                self.cmdbar.horizontalSlider_a.valueChanged.connect(
                    self.Circle_core)
                self.cmdbar.horizontalSlider_b.valueChanged.connect(
                    self.Circle_core)
                self.cmdbar.horizontalSlider_d.valueChanged.connect(
                    self.Circle_core)
                self.cmdbar.adjust_yes.clicked.connect(self.save_Temp)
                self.cmdbar.adjust_no.clicked.connect(self.cancel_Temp)
                self.cmdbar.horizontalSlider_a.sliderReleased.connect(
                    self.Circle_released)
                self.cmdbar.horizontalSlider_b.sliderReleased.connect(
                    self.Circle_released)
                self.cmdbar.horizontalSlider_d.sliderReleased.connect(
                    self.Circle_released)

    def Circle_core(self):
        self.image_temp = Core.HoughCircle_detect(
            self.image_now, self.cmdbar.a, self.cmdbar.b, self.cmdbar.d)
        self.processed_show(self.image_temp)

    def Circle_released(self):
        self.show_msg('霍夫圆检测完成')
        self.show_his('霍夫圆最小半径:{} 最大半径:{} 最小圆心距:{}'.format(
            self.cmdbar.a, self.cmdbar.b, self.cmdbar.d))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    temp = My_Mainwindow()
    temp.show()
    sys.exit(app.exec_())
