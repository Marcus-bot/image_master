from PyQt5 import QtCore, QtGui, QtWidgets
from Main import My_Mainwindow


class cmd_Adjust(My_Mainwindow, QtWidgets.QWidget):
    # 调整控制台
    def __init__(self, widget):
        super(cmd_Adjust, self).__init__()

        self.gridLayoutWidget_cmd = widget
        self.gridLayout_cmd = QtWidgets.QGridLayout(self.gridLayoutWidget_cmd)
        self.gridLayout_cmd.setContentsMargins(20, 10, 20, 10)
        self.gridLayout_cmd.setObjectName("gridLayout_cmd")
# ----------------------------中间为UI界面---------------------------
        # 在layout中生成label
        self.label_a = QtWidgets.QLabel(self.gridLayoutWidget_cmd)
        self.label_a = QtWidgets.QLabel(self.gridLayoutWidget_cmd)
        self.label_a.setObjectName("label_a")
        self.gridLayout_cmd.addWidget(self.label_a, 0, 0, 1, 1)
        self.lineEdit_a = QtWidgets.QLineEdit(self.gridLayoutWidget_cmd)
        self.lineEdit_a.setObjectName("lineEdit_a")
        self.gridLayout_cmd.addWidget(self.lineEdit_a, 0, 2, 1, 1)
        self.horizontalSlider_a = QtWidgets.QSlider(self.gridLayoutWidget_cmd)
        self.horizontalSlider_a.setStatusTip("")
        self.horizontalSlider_a.setAccessibleName("")
        self.horizontalSlider_a.setAccessibleDescription("")
        self.horizontalSlider_a.setMinimum(-99)
        self.horizontalSlider_a.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_a.setObjectName("horizontalSlider_a")
        self.gridLayout_cmd.addWidget(self.horizontalSlider_a, 0, 1, 1, 1)
        self.horizontalSlider_b = QtWidgets.QSlider(self.gridLayoutWidget_cmd)
        self.horizontalSlider_b.setMinimum(-99)
        self.horizontalSlider_b.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_b.setObjectName("horizontalSlider_b")
        self.gridLayout_cmd.addWidget(self.horizontalSlider_b, 1, 1, 1, 1)
        self.lineEdit_b = QtWidgets.QLineEdit(self.gridLayoutWidget_cmd)
        self.lineEdit_b.setObjectName("lineEdit_b")
        self.gridLayout_cmd.addWidget(self.lineEdit_b, 1, 2, 1, 1)
        self.label_b = QtWidgets.QLabel(self.gridLayoutWidget_cmd)
        self.label_b.setObjectName("label_b")
        self.gridLayout_cmd.addWidget(self.label_b, 1, 0, 1, 1)
        self.adjust_yes = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_yes.setObjectName("adjust_yes")
        self.gridLayout_cmd.addWidget(self.adjust_yes, 2, 0, 1, 1)
        self.adjust_no = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_no.setObjectName("adjust_no")
        self.gridLayout_cmd.addWidget(self.adjust_no, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem, 2, 1, 1, 1)
        self.gridLayout_cmd.setColumnStretch(0, 1)
        self.gridLayout_cmd.setColumnStretch(1, 4)
        self.gridLayout_cmd.setColumnStretch(2, 1)
# --------------------------中间为UI界面-----------------------------
        self.retranslate()

        self.lineEdit_a.setValidator(QtGui.QIntValidator(-99, 99))
        self.lineEdit_b.setValidator(QtGui.QIntValidator(-99, 99))
        self.a = self.horizontalSlider_a.value()  # 初始化 sliderbar值
        self.b = self.horizontalSlider_b.value()

        # 链接参数改变
        self.horizontalSlider_a.valueChanged.connect(self.changed_a)
        self.horizontalSlider_b.valueChanged.connect(self.changed_b)
        self.lineEdit_a.editingFinished.connect(self.set_a)
        self.lineEdit_b.editingFinished.connect(self.set_b)

    def retranslate(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_a.setText(_translate("MainWindow", "对比度"))
        self.horizontalSlider_a.setToolTip(
            _translate("MainWindow", "范围：-99到99"))
        self.horizontalSlider_b.setToolTip(
            _translate("MainWindow", "范围：-99到99"))
        self.label_b.setText(_translate("MainWindow", "亮度"))
        self.adjust_yes.setText(_translate("MainWindow", "OK"))
        self.adjust_no.setText(_translate("MainWindow", "cancel"))

    def changed_a(self):
        # 获取slider值，更新editor
        self.a = self.horizontalSlider_a.value()
        self.lineEdit_a.setText(str(self.a))

    def changed_b(self):
        self.b = self.horizontalSlider_b.value()
        self.lineEdit_b.setText(str(self.b))

    def set_a(self):
        # 使用lineedit设置值，同步更新slider
        self.a = int(self.lineEdit_a.text())
        self.horizontalSlider_a.setValue(self.a)

    def set_b(self):
        self.b = int(self.lineEdit_b.text())
        self.horizontalSlider_b.setValue(self.b)


class Edge_Select(My_Mainwindow, QtWidgets.QWidget):

    def __init__(self, widget):
        super(Edge_Select, self).__init__()
        self.gridLayoutWidget_cmd = widget
        self.gridLayout_cmd = QtWidgets.QGridLayout(self.gridLayoutWidget_cmd)
        self.gridLayout_cmd.setContentsMargins(20, 10, 20, 10)
        self.gridLayout_cmd.setObjectName("gridLayout_cmd")
# ----------------------------中间为UI界面---------------------------
        self.adjust_yes = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_yes.setObjectName("adjust_yes")
        self.gridLayout_cmd.addWidget(self.adjust_yes, 2, 0, 1, 1)
        self.label_max = QtWidgets.QLabel(self.gridLayoutWidget_cmd)
        self.label_max.setObjectName("label_max")
        self.gridLayout_cmd.addWidget(self.label_max, 1, 0, 1, 1)
        self.label_min = QtWidgets.QLabel(self.gridLayoutWidget_cmd)
        self.label_min.setObjectName("label_min")
        self.gridLayout_cmd.addWidget(self.label_min, 0, 0, 1, 1)
        self.horizontalSlider_b = QtWidgets.QSlider(self.gridLayoutWidget_cmd)
        self.horizontalSlider_b.setMinimum(-150)
        self.horizontalSlider_b.setMaximum(705)
        self.horizontalSlider_b.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_b.setObjectName("horizontalSlider_b")
        self.gridLayout_cmd.addWidget(self.horizontalSlider_b, 1, 1, 1, 1)
        self.horizontalSlider_a = QtWidgets.QSlider(self.gridLayoutWidget_cmd)
        self.horizontalSlider_a.setStatusTip("")
        self.horizontalSlider_a.setAccessibleName("")
        self.horizontalSlider_a.setAccessibleDescription("")
        self.horizontalSlider_a.setMinimum(-50)
        self.horizontalSlider_a.setMaximum(805)
        self.horizontalSlider_a.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_a.setObjectName("horizontalSlider_a")
        self.gridLayout_cmd.addWidget(self.horizontalSlider_a, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_cmd)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_cmd.addWidget(self.comboBox, 0, 2, 1, 1)
        self.adjust_no = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_no.setObjectName("adjust_no")
        self.gridLayout_cmd.addWidget(self.adjust_no, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem1, 1, 2, 1, 1)
        self.gridLayout_cmd.setColumnStretch(0, 1)
        self.gridLayout_cmd.setColumnStretch(1, 4)
        self.gridLayout_cmd.setColumnStretch(2, 1)
# --------------------------中间为UI界面-----------------------------
        self.retranslate()

        self.a = self.horizontalSlider_a.value()
        self.b = self.horizontalSlider_b.value()

        self.horizontalSlider_a.valueChanged.connect(self.changed_a)
        self.horizontalSlider_b.valueChanged.connect(self.changed_b)

    def retranslate(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_min.setText(_translate("MainWindow", "最小阈值"))
        self.horizontalSlider_a.setToolTip(
            _translate("MainWindow", "范围：-50到805"))
        self.horizontalSlider_b.setToolTip(
            _translate("MainWindow", "范围：-150到705"))
        self.label_max.setText(_translate("MainWindow", "最大阈值"))
        self.adjust_yes.setText(_translate("MainWindow", "OK"))
        self.adjust_no.setText(_translate("MainWindow", "cancel"))
        self.choice = 'Canny'
        self.comboBox.addItem(self.choice)

    def changed_a(self):
        self.a = self.horizontalSlider_a.value()

    def changed_b(self):
        self.b = self.horizontalSlider_b.value()


class Smooth_Image(My_Mainwindow, QtWidgets.QWidget):
    # 滤波器
    def __init__(self, widget):
        super(Smooth_Image, self).__init__()

        self.gridLayoutWidget_cmd = widget
        self.gridLayout_cmd = QtWidgets.QGridLayout(self.gridLayoutWidget_cmd)
        self.gridLayout_cmd.setContentsMargins(20, 10, 20, 10)
        self.gridLayout_cmd.setObjectName("gridLayout_cmd")
# ----------------------------中间为UI界面---------------------------
        self.adjust_yes = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_yes.setObjectName("adjust_yes")
        self.gridLayout_cmd.addWidget(self.adjust_yes, 2, 0, 1, 1)
        self.label_smooth = QtWidgets.QLabel(self.gridLayoutWidget_cmd)
        self.label_smooth.setObjectName("label_smooth")
        self.gridLayout_cmd.addWidget(self.label_smooth, 1, 0, 1, 1)
        self.horizontalSlider_a = QtWidgets.QSlider(self.gridLayoutWidget_cmd)
        self.horizontalSlider_a.setMinimum(0)
        self.horizontalSlider_a.setMaximum(10)
        self.horizontalSlider_a.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_a.setObjectName("horizontalSlider_a")
        self.gridLayout_cmd.addWidget(self.horizontalSlider_a, 1, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_cmd)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_cmd.addWidget(self.comboBox, 0, 2, 1, 1)
        self.adjust_no = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_no.setObjectName("adjust_no")
        self.gridLayout_cmd.addWidget(self.adjust_no, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem, 2, 1, 1, 1)
        self.lineEdit_smooth = QtWidgets.QLineEdit(self.gridLayoutWidget_cmd)
        self.lineEdit_smooth.setObjectName("lineEdit_smooth")
        self.lineEdit_smooth.setValidator(QtGui.QIntValidator(0, 10))
        self.gridLayout_cmd.addWidget(self.lineEdit_smooth, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem2, 0, 1, 1, 1)
        self.gridLayout_cmd.setColumnStretch(0, 1)
        self.gridLayout_cmd.setColumnStretch(1, 4)
        self.gridLayout_cmd.setColumnStretch(2, 1)
# --------------------------中间为UI界面-----------------------------
        self.retranslate()
        self.a = self.horizontalSlider_a.value()
        self.c = 1
        # 链接滤波器阶数处理
        self.horizontalSlider_a.valueChanged.connect(self.changed_a)
        self.comboBox.currentTextChanged.connect(self.changed_choice)
        self.lineEdit_smooth.editingFinished.connect(self.set_a)

    def retranslate(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_smooth.setText(_translate("MainWindow", "滤波阶数"))
        self.horizontalSlider_a.setToolTip(
            _translate("MainWindow", "范围：0到10"))
        self.adjust_yes.setText(_translate("MainWindow", "OK"))
        self.adjust_no.setText(_translate("MainWindow", "cancel"))

        self.choice = '均值滤波'  # 添加comboBox
        self.choice_list = ['中值滤波', '双边滤波', '高斯滤波']
        self.comboBox.addItem(self.choice)
        self.comboBox.addItems(self.choice_list)
    # slider和edit同步改变函数

    def changed_a(self):
        self.a = self.horizontalSlider_a.value()
        self.lineEdit_smooth.setText(str(self.a))

    def set_a(self):
        self.a = int(self.lineEdit_smooth.text())
        self.horizontalSlider_a.setValue(self.a)

    def changed_choice(self):
        self.choice = self.comboBox.currentText()
        self.a = 0
        self.horizontalSlider_a.setValue(self.a)
        if self.choice == '均值滤波':
            self.c = 1
        elif self.choice == '中值滤波':
            self.c = 2
        elif self.choice == '双边滤波':
            self.c = 3
        else:
            self.c = 4


class Bin_Image(My_Mainwindow, QtWidgets.QWidget):
    # 二值化
    def __init__(self, widget):
        super(Bin_Image, self).__init__()

        self.gridLayoutWidget_cmd = widget
        self.gridLayout_cmd = QtWidgets.QGridLayout(self.gridLayoutWidget_cmd)
        self.gridLayout_cmd.setContentsMargins(20, 10, 20, 10)
        self.gridLayout_cmd.setObjectName("gridLayout_cmd")
# ----------------------------中间为UI界面---------------------------
        self.adjust_no = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_no.setObjectName("adjust_no")
        self.gridLayout_cmd.addWidget(self.adjust_no, 1, 2, 1, 1)
        self.adjust_yes = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_yes.setObjectName("adjust_yes")
        self.gridLayout_cmd.addWidget(self.adjust_yes, 1, 0, 1, 1)
        self.label_bin = QtWidgets.QLabel(self.gridLayoutWidget_cmd)
        self.label_bin.setObjectName("label_bin")
        self.gridLayout_cmd.addWidget(self.label_bin, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem, 1, 1, 1, 1)
        self.horizontalSlider_a = QtWidgets.QSlider(self.gridLayoutWidget_cmd)
        self.horizontalSlider_a.setMinimum(0)
        self.horizontalSlider_a.setMaximum(255)
        self.horizontalSlider_a.setProperty("value", 128)
        self.horizontalSlider_a.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_a.setObjectName("horizontalSlider_a")
        self.gridLayout_cmd.addWidget(self.horizontalSlider_a, 0, 1, 1, 1)
        self.lineEdit_bin = QtWidgets.QLineEdit(self.gridLayoutWidget_cmd)
        self.lineEdit_bin.setObjectName("lineEdit_bin")
        self.gridLayout_cmd.addWidget(self.lineEdit_bin, 0, 2, 1, 1)
        self.gridLayout_cmd.setColumnStretch(0, 1)
        self.gridLayout_cmd.setColumnStretch(1, 4)
        self.gridLayout_cmd.setColumnStretch(2, 1)
# --------------------------中间为UI界面-----------------------------
        self.retranslate()
        self.a = self.horizontalSlider_a.value()
        self.lineEdit_bin.setText(str(self.a))
        self.horizontalSlider_a.valueChanged.connect(self.changed_a)
        self.lineEdit_bin.editingFinished.connect(self.set_a)

    def retranslate(self):
        _translate = QtCore.QCoreApplication.translate
        self.horizontalSlider_a.setToolTip(
            _translate("MainWindow", "范围：0到10"))
        self.adjust_yes.setText(_translate("MainWindow", "OK"))
        self.adjust_no.setText(_translate("MainWindow", "cancel"))
        self.horizontalSlider_a.setToolTip(
            _translate("MainWindow", "范围：0到255"))

    def changed_a(self):
        # 二值化阈值
        self.a = self.horizontalSlider_a.value()
        self.lineEdit_bin.setText(str(self.a))

    def set_a(self):
        self.a = int(self.lineEdit_bin.text())
        self.horizontalSlider_a.setValue(self.a)


class Channel_Select(My_Mainwindow, QtWidgets.QWidget):

    def __init__(self, widget):
        super(Channel_Select, self).__init__()

        self.gridLayoutWidget_cmd = widget
        self.gridLayout_cmd = QtWidgets.QGridLayout(self.gridLayoutWidget_cmd)
        self.gridLayout_cmd.setContentsMargins(20, 10, 20, 10)
        self.gridLayout_cmd.setObjectName("gridLayout_cmd")
# ----------------------------中间为UI界面---------------------------
        self.adjust_no = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_no.setObjectName("adjust_no")
        self.gridLayout_cmd.addWidget(self.adjust_no, 2, 2, 1, 1)
        self.checkBox_g = QtWidgets.QCheckBox(self.gridLayoutWidget_cmd)
        self.checkBox_g.setObjectName("checkBox_g")
        self.gridLayout_cmd.addWidget(
            self.checkBox_g, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.checkBox_b = QtWidgets.QCheckBox(self.gridLayoutWidget_cmd)
        self.checkBox_b.setObjectName("checkBox_b")
        self.gridLayout_cmd.addWidget(
            self.checkBox_b, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.checkBox_r = QtWidgets.QCheckBox(self.gridLayoutWidget_cmd)
        self.checkBox_r.setObjectName("checkBox_r")
        self.gridLayout_cmd.addWidget(
            self.checkBox_r, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.adjust_yes = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_yes.setObjectName("adjust_yes")
        self.gridLayout_cmd.addWidget(self.adjust_yes, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem, 2, 1, 1, 1)
        self.verticalSlider_r = QtWidgets.QSlider(self.gridLayoutWidget_cmd)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.verticalSlider_r.sizePolicy().hasHeightForWidth())
        self.verticalSlider_r.setSizePolicy(sizePolicy)
        self.verticalSlider_r.setMaximum(100)
        self.verticalSlider_r.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_r.setObjectName("verticalSlider_r")
        self.gridLayout_cmd.addWidget(
            self.verticalSlider_r, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalSlider_g = QtWidgets.QSlider(self.gridLayoutWidget_cmd)
        self.verticalSlider_g.setMaximum(100)
        self.verticalSlider_g.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_g.setObjectName("verticalSlider_g")
        self.gridLayout_cmd.addWidget(
            self.verticalSlider_g, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalSlider_b = QtWidgets.QSlider(self.gridLayoutWidget_cmd)
        self.verticalSlider_b.setMaximum(100)
        self.verticalSlider_b.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_b.setObjectName("verticalSlider_b")
        self.gridLayout_cmd.addWidget(
            self.verticalSlider_b, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_cmd.setColumnStretch(0, 1)
        self.gridLayout_cmd.setColumnStretch(1, 3)
        self.gridLayout_cmd.setColumnStretch(2, 1)
        self.gridLayout_cmd.setRowStretch(0, 1)
        self.gridLayout_cmd.setRowStretch(1, 2)
        self.gridLayout_cmd.setRowStretch(2, 1)
# --------------------------中间为UI界面-----------------------------
        self.retranslate()
        # checkbox默认勾选
        self.checkBox_r.setChecked(True)
        self.checkBox_g.setChecked(True)
        self.checkBox_b.setChecked(True)
        # 通道默认全选
        self.verticalSlider_r.setValue(100)
        self.verticalSlider_g.setValue(100)
        self.verticalSlider_b.setValue(100)
        self.r = 1
        self.g = 1
        self.b = 1
        self.checkBox_r.stateChanged.connect(self.changed_r)
        self.checkBox_g.stateChanged.connect(self.changed_g)
        self.checkBox_b.stateChanged.connect(self.changed_b)
        self.verticalSlider_r.valueChanged.connect(self.vchange_rgb)
        self.verticalSlider_g.valueChanged.connect(self.vchange_rgb)
        self.verticalSlider_b.valueChanged.connect(self.vchange_rgb)

    def retranslate(self):
        _translate = QtCore.QCoreApplication.translate
        self.adjust_yes.setText(_translate("MainWindow", "OK"))
        self.adjust_no.setText(_translate("MainWindow", "cancel"))
        self.checkBox_g.setText(_translate("MainWindow", "Green"))
        self.checkBox_b.setText(_translate("MainWindow", "Blue"))
        self.checkBox_r.setText(_translate("MainWindow", "Red"))
    # checkbox更改rgb参数

    def changed_r(self):
        if self.checkBox_r.isChecked():
            self.r = 1
            self.verticalSlider_r.setValue(100)
        else:
            self.r = 0
            self.verticalSlider_r.setValue(0)

    def changed_g(self):
        if self.checkBox_g.isChecked():
            self.g = 1
            self.verticalSlider_g.setValue(100)
        else:
            self.g = 0
            self.verticalSlider_g.setValue(0)

    def changed_b(self):
        if self.checkBox_b.isChecked():
            self.b = 1
            self.verticalSlider_b.setValue(100)
        else:
            self.b = 0
            self.verticalSlider_b.setValue(0)
    # slider 更改参数

    def vchange_rgb(self):
        self.r = self.verticalSlider_r.value()/100.0
        self.g = self.verticalSlider_g.value()/100.0
        self.b = self.verticalSlider_b.value()/100.0
        if self.r == 0:
            self.checkBox_r.setChecked(False)
        else:
            self.checkBox_r.setChecked(True)

        if self.g == 0:
            self.checkBox_g.setChecked(False)
        else:
            self.checkBox_g.setChecked(True)

        if self.b == 0:
            self.checkBox_b.setChecked(False)
        else:
            self.checkBox_b.setChecked(True)


class Contour_Detect(My_Mainwindow, QtWidgets.QWidget):
    # 轮廓检测
    def __init__(self, widget):
        super(Contour_Detect, self).__init__()

        self.gridLayoutWidget_cmd = widget
        self.gridLayout_cmd = QtWidgets.QGridLayout(self.gridLayoutWidget_cmd)
        self.gridLayout_cmd.setContentsMargins(20, 10, 20, 10)
        self.gridLayout_cmd.setObjectName("gridLayout_cmd")
# ----------------------------中间为UI界面---------------------------
        self.adjust_no = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_no.setObjectName("adjust_no")
        self.gridLayout_cmd.addWidget(self.adjust_no, 1, 2, 1, 1)
        self.label_width = QtWidgets.QLabel(self.gridLayoutWidget_cmd)
        self.label_width.setObjectName("label_width")
        self.gridLayout_cmd.addWidget(self.label_width, 0, 0, 1, 1)
        self.adjust_yes = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_yes.setObjectName("adjust_yes")
        self.gridLayout_cmd.addWidget(self.adjust_yes, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem1, 0, 2, 1, 1)
        self.horizontalSlider_width = QtWidgets.QSlider(
            self.gridLayoutWidget_cmd)
        self.horizontalSlider_width.setMinimum(1)
        self.horizontalSlider_width.setMaximum(4)
        self.horizontalSlider_width.setPageStep(1)
        self.horizontalSlider_width.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_width.setInvertedAppearance(False)
        self.horizontalSlider_width.setInvertedControls(False)
        self.horizontalSlider_width.setTickPosition(
            QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_width.setObjectName("horizontalSlider_width")
        self.gridLayout_cmd.addWidget(self.horizontalSlider_width, 0, 1, 1, 1)
        self.gridLayout_cmd.setColumnStretch(0, 1)
        self.gridLayout_cmd.setColumnStretch(1, 4)
        self.gridLayout_cmd.setColumnStretch(2, 1)
# --------------------------中间为UI界面-----------------------------
        self.retranslate()
        self.width = self.horizontalSlider_width.value()
        self.horizontalSlider_width.valueChanged.connect(self.changed_width)

    def retranslate(self):
        _translate = QtCore.QCoreApplication.translate
        self.horizontalSlider_width.setToolTip(
            _translate("MainWindow", "范围：1到4"))
        self.adjust_yes.setText(_translate("MainWindow", "OK"))
        self.adjust_no.setText(_translate("MainWindow", "cancel"))
        self.label_width.setText(_translate("MainWindow", "轮廓宽度"))

    def changed_width(self):
        # 获取轮廓宽度
        self.width = self.horizontalSlider_width.value()


class Style_Transfer(My_Mainwindow, QtWidgets.QWidget):
    # 风格迁移
    def __init__(self, widget):
        super(Style_Transfer, self).__init__()

        self.gridLayoutWidget_cmd = widget
        self.gridLayout_cmd = QtWidgets.QGridLayout(self.gridLayoutWidget_cmd)
        self.gridLayout_cmd.setContentsMargins(20, 10, 20, 10)
        self.gridLayout_cmd.setObjectName("gridLayout_cmd")
# ----------------------------中间为UI界面---------------------------
        self.adjust_no = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_no.setObjectName("adjust_no")
        self.gridLayout_cmd.addWidget(self.adjust_no, 2, 2, 1, 1)
        self.label_style = QtWidgets.QLabel(self.gridLayoutWidget_cmd)
        self.label_style.setObjectName("label_style")
        self.gridLayout_cmd.addWidget(self.label_style, 0, 0, 1, 1)
        self.adjust_yes = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_yes.setObjectName("adjust_yes")
        self.gridLayout_cmd.addWidget(self.adjust_yes, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem, 2, 1, 1, 1)
        self.comboBox_style = QtWidgets.QComboBox(self.gridLayoutWidget_cmd)
        self.comboBox_style.setObjectName("comboBox_style")
        self.gridLayout_cmd.addWidget(self.comboBox_style, 0, 2, 1, 1)
        self.label_width_2 = QtWidgets.QLabel(self.gridLayoutWidget_cmd)
        self.label_width_2.setObjectName("label_width_2")
        self.gridLayout_cmd.addWidget(self.label_width_2, 1, 0, 1, 1)
        self.horizontalSlider_style = QtWidgets.QSlider(
            self.gridLayoutWidget_cmd)
        self.horizontalSlider_style.setMinimum(1)
        self.horizontalSlider_style.setMaximum(3)
        self.horizontalSlider_style.setSingleStep(1)
        self.horizontalSlider_style.setPageStep(1)
        self.horizontalSlider_style.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_style.setInvertedAppearance(False)
        self.horizontalSlider_style.setInvertedControls(False)
        self.horizontalSlider_style.setTickPosition(
            QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_style.setObjectName("horizontalSlider_style")
        self.gridLayout_cmd.addWidget(self.horizontalSlider_style, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem2, 1, 2, 1, 1)
        self.gridLayout_cmd.setColumnStretch(0, 1)
        self.gridLayout_cmd.setColumnStretch(1, 4)
        self.gridLayout_cmd.setColumnStretch(2, 1)
# --------------------------中间为UI界面-----------------------------
        self.retranslate()
        self.f = 1  # 初始化滤波器参数（大于等于1的奇数）
        self.comboBox_style.currentTextChanged.connect(self.changed_style)
        self.horizontalSlider_style.valueChanged.connect(self.changed_f)

    def retranslate(self):
        _translate = QtCore.QCoreApplication.translate
        self.adjust_yes.setText(_translate("MainWindow", "OK"))
        self.adjust_no.setText(_translate("MainWindow", "cancel"))
        self.label_width_2.setText(_translate("MainWindow", "中值滤波参数"))
        self.label_style.setText(_translate("MainWindow", "选择风格"))
        # 设置模型名称
        self.choice = 'the_wave'
        self.model = 'Transfer_Image_style/the_wave.t7'
        self.choice_list = ['the_scream', 'udnie', 'mosaic',
                            'la_muse', 'feathers', 'composition_vii', 'candy']
        self.comboBox_style.addItem(self.choice)
        self.comboBox_style.addItems(self.choice_list)

    def changed_f(self):
        self.f = 2*self.horizontalSlider_style.value()-1

    def changed_style(self):
        self.choice = self.comboBox_style.currentText()
        # 获取模型文件地址
        self.model = 'Transfer_Image_style/'+self.choice+'.t7'


class Cut_Image(My_Mainwindow, QtWidgets.QWidget):
    # 图像裁剪UI
    def __init__(self, widget):
        super(Cut_Image, self).__init__()

        self.gridLayoutWidget_cmd = widget
        self.gridLayout_cmd = QtWidgets.QGridLayout(self.gridLayoutWidget_cmd)
        self.gridLayout_cmd.setContentsMargins(20, 10, 20, 10)
        self.gridLayout_cmd.setObjectName("gridLayout_cmd")
# ----------------------------中间为UI界面---------------------------
        self.adjust_no = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_no.setObjectName("adjust_no")
        self.gridLayout_cmd.addWidget(self.adjust_no, 2, 2, 1, 1)
        self.adjust_yes = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_yes.setObjectName("adjust_yes")
        self.gridLayout_cmd.addWidget(self.adjust_yes, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_cmd.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_cmd.addItem(spacerItem3, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem4, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_cmd)
        self.label.setObjectName("label")
        self.gridLayout_cmd.addWidget(
            self.label, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_cmd)
        self.label_2.setObjectName("label_2")
        self.gridLayout_cmd.addWidget(
            self.label_2, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_cmd.setColumnStretch(0, 1)
        self.gridLayout_cmd.setColumnStretch(1, 4)
        self.gridLayout_cmd.setColumnStretch(2, 1)
# --------------------------中间为UI界面-----------------------------
        self.retranslate()

    def retranslate(self):
        _translate = QtCore.QCoreApplication.translate
        self.adjust_yes.setText(_translate("MainWindow", "OK"))
        self.adjust_no.setText(_translate("MainWindow", "cancel"))
        self.label.setText(_translate("MainWindow", "裁剪完成"))
        self.label_2.setText(_translate("MainWindow", "取消"))


class Lines_Detect(My_Mainwindow, QtWidgets.QWidget):
    # 直线检测UI
    def __init__(self, widget):
        super(Lines_Detect, self).__init__()

        self.gridLayoutWidget_cmd = widget
        self.gridLayout_cmd = QtWidgets.QGridLayout(self.gridLayoutWidget_cmd)
        self.gridLayout_cmd.setContentsMargins(20, 10, 20, 10)
        self.gridLayout_cmd.setObjectName("gridLayout_cmd")
# ----------------------------中间为UI界面---------------------------
        self.adjust_no = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_no.setObjectName("adjust_no")
        self.gridLayout_cmd.addWidget(self.adjust_no, 2, 2, 1, 1)
        self.label_maxgap = QtWidgets.QLabel(self.gridLayoutWidget_cmd)
        self.label_maxgap.setObjectName("label_maxgap")
        self.gridLayout_cmd.addWidget(
            self.label_maxgap, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_minlen = QtWidgets.QLabel(self.gridLayoutWidget_cmd)
        self.label_minlen.setObjectName("label_minlen")
        self.gridLayout_cmd.addWidget(
            self.label_minlen, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.adjust_yes = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_yes.setObjectName("adjust_yes")
        self.gridLayout_cmd.addWidget(self.adjust_yes, 2, 0, 1, 1)
        self.horizontalSlider_a = QtWidgets.QSlider(self.gridLayoutWidget_cmd)
        self.horizontalSlider_a.setMinimum(-100)
        self.horizontalSlider_a.setMaximum(700)
        self.horizontalSlider_a.setPageStep(50)
        self.horizontalSlider_a.setProperty("value", -100)
        self.horizontalSlider_a.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_a.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_a.setObjectName("horizontalSlider_a")
        self.gridLayout_cmd.addWidget(self.horizontalSlider_a, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem2, 1, 2, 1, 1)
        self.horizontalSlider_b = QtWidgets.QSlider(self.gridLayoutWidget_cmd)
        self.horizontalSlider_b.setMinimum(-10)
        self.horizontalSlider_b.setMaximum(90)
        self.horizontalSlider_b.setSingleStep(10)
        self.horizontalSlider_b.setPageStep(1)
        self.horizontalSlider_b.setProperty("value", -10)
        self.horizontalSlider_b.setSliderPosition(-10)
        self.horizontalSlider_b.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_b.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_b.setObjectName("horizontalSlider_b")
        self.gridLayout_cmd.addWidget(self.horizontalSlider_b, 1, 1, 1, 1)
        self.gridLayout_cmd.setColumnStretch(0, 1)
        self.gridLayout_cmd.setColumnStretch(1, 4)
        self.gridLayout_cmd.setColumnStretch(2, 1)
# --------------------------中间为UI界面-----------------------------
        self.retranslate()
        # 初始化参数
        self.a = self.horizontalSlider_a.value()
        self.b = self.horizontalSlider_b.value()

        self.horizontalSlider_a.valueChanged.connect(self.changed_a)
        self.horizontalSlider_b.valueChanged.connect(self.changed_b)

    def retranslate(self):
        _translate = QtCore.QCoreApplication.translate
        self.horizontalSlider_a.setToolTip(_translate("MainWindow", "最小长度"))
        self.horizontalSlider_b.setToolTip(_translate("MainWindow", "最大间隔"))
        self.label_maxgap.setText(_translate("MainWindow", "最大间隙"))
        self.label_minlen.setText(_translate("MainWindow", "最小长度"))
        self.adjust_yes.setText(_translate("MainWindow", "OK"))
        self.adjust_no.setText(_translate("MainWindow", "cancel"))

    def changed_a(self):
        self.a = self.horizontalSlider_a.value()

    def changed_b(self):
        self.b = self.horizontalSlider_b.value()


class Circle_Detect(My_Mainwindow, QtWidgets.QWidget):
    # 圆检测
    def __init__(self, widget):
        super(Circle_Detect, self).__init__()

        self.gridLayoutWidget_cmd = widget
        self.gridLayout_cmd = QtWidgets.QGridLayout(self.gridLayoutWidget_cmd)
        self.gridLayout_cmd.setContentsMargins(20, 10, 20, 10)
        self.gridLayout_cmd.setObjectName("gridLayout_cmd")
# ----------------------------中间为UI界面---------------------------
        self.adjust_no = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_no.setObjectName("adjust_no")
        self.gridLayout_cmd.addWidget(self.adjust_no, 3, 2, 1, 1)
        self.label_maxRad = QtWidgets.QLabel(self.gridLayoutWidget_cmd)
        self.label_maxRad.setObjectName("label_maxRad")
        self.gridLayout_cmd.addWidget(
            self.label_maxRad, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_minRad = QtWidgets.QLabel(self.gridLayoutWidget_cmd)
        self.label_minRad.setObjectName("label_minRad")
        self.gridLayout_cmd.addWidget(
            self.label_minRad, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.adjust_yes = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_yes.setObjectName("adjust_yes")
        self.gridLayout_cmd.addWidget(self.adjust_yes, 3, 0, 1, 1)
        self.horizontalSlider_a = QtWidgets.QSlider(self.gridLayoutWidget_cmd)
        self.horizontalSlider_a.setMinimum(-50)
        self.horizontalSlider_a.setMaximum(300)
        self.horizontalSlider_a.setSingleStep(50)
        self.horizontalSlider_a.setPageStep(50)
        self.horizontalSlider_a.setProperty("value", 0)
        self.horizontalSlider_a.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_a.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_a.setObjectName("horizontalSlider_a")
        self.gridLayout_cmd.addWidget(self.horizontalSlider_a, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem1, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem2, 1, 2, 1, 1)
        self.horizontalSlider_b = QtWidgets.QSlider(self.gridLayoutWidget_cmd)
        self.horizontalSlider_b.setMinimum(-300)
        self.horizontalSlider_b.setMaximum(500)
        self.horizontalSlider_b.setSingleStep(50)
        self.horizontalSlider_b.setPageStep(1)
        self.horizontalSlider_b.setProperty("value", 0)
        self.horizontalSlider_b.setSliderPosition(0)
        self.horizontalSlider_b.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_b.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_b.setObjectName("horizontalSlider_b")
        self.gridLayout_cmd.addWidget(self.horizontalSlider_b, 1, 1, 1, 1)
        self.label_mindist = QtWidgets.QLabel(self.gridLayoutWidget_cmd)
        self.label_mindist.setObjectName("label_mindist")
        self.gridLayout_cmd.addWidget(
            self.label_mindist, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalSlider_d = QtWidgets.QSlider(self.gridLayoutWidget_cmd)
        self.horizontalSlider_d.setMinimum(-180)
        self.horizontalSlider_d.setMaximum(500)
        self.horizontalSlider_d.setSingleStep(50)
        self.horizontalSlider_d.setPageStep(1)
        self.horizontalSlider_d.setProperty("value", 0)
        self.horizontalSlider_d.setSliderPosition(0)
        self.horizontalSlider_d.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_d.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_d.setObjectName("horizontalSlider_d")
        self.gridLayout_cmd.addWidget(self.horizontalSlider_d, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem3, 2, 2, 1, 1)
        self.gridLayout_cmd.setColumnStretch(0, 1)
        self.gridLayout_cmd.setColumnStretch(1, 4)
        self.gridLayout_cmd.setColumnStretch(2, 1)
# --------------------------中间为UI界面-----------------------------
        self.retranslate()

        self.a = self.horizontalSlider_a.value()
        self.b = self.horizontalSlider_b.value()
        self.d = self.horizontalSlider_d.value()

        self.horizontalSlider_a.valueChanged.connect(self.changed_a)
        self.horizontalSlider_b.valueChanged.connect(self.changed_b)
        self.horizontalSlider_d.valueChanged.connect(self.changed_d)

    def retranslate(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_maxRad.setText(_translate("MainWindow", "最大半径"))
        self.label_minRad.setText(_translate("MainWindow", "最小半径"))
        self.label_mindist.setText(_translate("MainWindow", "最小圆心距"))
        self.adjust_yes.setText(_translate("MainWindow", "OK"))
        self.adjust_no.setText(_translate("MainWindow", "cancel"))

    def changed_a(self):
        self.a = self.horizontalSlider_a.value()

    def changed_b(self):
        self.b = self.horizontalSlider_b.value()

    def changed_d(self):
        self.d = self.horizontalSlider_d.value()


class Rot_Image(My_Mainwindow, QtWidgets.QWidget):
    # 图像旋转
    def __init__(self, widget):
        super(Rot_Image, self).__init__()

        self.gridLayoutWidget_cmd = widget
        self.gridLayout_cmd = QtWidgets.QGridLayout(self.gridLayoutWidget_cmd)
        self.gridLayout_cmd.setContentsMargins(20, 10, 20, 10)
        self.gridLayout_cmd.setObjectName("gridLayout_cmd")
# ----------------------------中间为UI界面---------------------------
        self.adjust_no = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_no.setObjectName("adjust_no")
        self.gridLayout_cmd.addWidget(self.adjust_no, 1, 2, 1, 1)
        self.adjust_yes = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        self.adjust_yes.setObjectName("adjust_yes")
        self.gridLayout_cmd.addWidget(self.adjust_yes, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem, 1, 1, 1, 1)
        self.pushButton_left = QtWidgets.QPushButton(self.gridLayoutWidget_cmd)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_left.sizePolicy().hasHeightForWidth())
        self.pushButton_left.setSizePolicy(sizePolicy)
        self.pushButton_left.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_left.setFont(font)
        self.pushButton_left.setObjectName("pushButton_left")
        self.gridLayout_cmd.addWidget(
            self.pushButton_left, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_right = QtWidgets.QPushButton(
            self.gridLayoutWidget_cmd)
        self.pushButton_right.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_right.setFont(font)
        self.pushButton_right.setAutoRepeatInterval(100)
        self.pushButton_right.setObjectName("pushButton_right")
        self.gridLayout_cmd.addWidget(
            self.pushButton_right, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_cmd.addItem(spacerItem1, 0, 1, 1, 1)
        self.gridLayout_cmd.setColumnStretch(0, 1)
        self.gridLayout_cmd.setColumnStretch(1, 4)
        self.gridLayout_cmd.setColumnStretch(2, 1)
        self.gridLayout_cmd.setRowStretch(0, 1)
        self.gridLayout_cmd.setRowStretch(1, 1)
# --------------------------中间为UI界面-----------------------------
        self.retranslate()
        self.angle = 1
        self.pushButton_left.clicked.connect(self.rot_left)
        self.pushButton_right.clicked.connect(self.rot_right)

    def retranslate(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_left.setText(_translate("MainWindow", "左转"))
        self.pushButton_right.setText(_translate("MainWindow", "右转"))
        self.adjust_yes.setText(_translate("MainWindow", "OK"))
        self.adjust_no.setText(_translate("MainWindow", "cancel"))

    def rot_left(self):
        # 共0 90 180 360 四个状态  限制angle取值为1234
        self.angle -= 1
        self.angle = 4 if self.angle == 0 else self.angle

    def rot_right(self):
        self.angle += 1
        self.angle = 1 if self.angle == 5 else self.angle
