# Form implementation generated from reading ui file 'src/ui/white_point_editor.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_white_point_editor(object):
    def setupUi(self, white_point_editor):
        white_point_editor.setObjectName("white_point_editor")
        white_point_editor.resize(906, 814)
        self.horizontalLayout = QtWidgets.QHBoxLayout(white_point_editor)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dockWidget_2 = QtWidgets.QDockWidget(white_point_editor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_2.sizePolicy().hasHeightForWidth())
        self.dockWidget_2.setSizePolicy(sizePolicy)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.color_circle = ColorCircle(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_circle.sizePolicy().hasHeightForWidth())
        self.color_circle.setSizePolicy(sizePolicy)
        self.color_circle.setMinimumSize(QtCore.QSize(100, 120))
        self.color_circle.setObjectName("color_circle")
        self.horizontalLayout_3.addWidget(self.color_circle)
        self.inner_value_slider = QtWidgets.QSlider(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inner_value_slider.sizePolicy().hasHeightForWidth())
        self.inner_value_slider.setSizePolicy(sizePolicy)
        self.inner_value_slider.setMaximum(511)
        self.inner_value_slider.setProperty("value", 511)
        self.inner_value_slider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.inner_value_slider.setObjectName("inner_value_slider")
        self.horizontalLayout_3.addWidget(self.inner_value_slider)
        self.outer_value_slider = QtWidgets.QSlider(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outer_value_slider.sizePolicy().hasHeightForWidth())
        self.outer_value_slider.setSizePolicy(sizePolicy)
        self.outer_value_slider.setMaximum(511)
        self.outer_value_slider.setProperty("value", 511)
        self.outer_value_slider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.outer_value_slider.setObjectName("outer_value_slider")
        self.horizontalLayout_3.addWidget(self.outer_value_slider)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.saturation_sb = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_2)
        self.saturation_sb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.saturation_sb.setDecimals(0)
        self.saturation_sb.setMaximum(255.0)
        self.saturation_sb.setObjectName("saturation_sb")
        self.gridLayout.addWidget(self.saturation_sb, 3, 1, 1, 1)
        self.value_sb = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_2)
        self.value_sb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.value_sb.setDecimals(0)
        self.value_sb.setMaximum(255.0)
        self.value_sb.setProperty("value", 255.0)
        self.value_sb.setObjectName("value_sb")
        self.gridLayout.addWidget(self.value_sb, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.color_blue_sb = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_2)
        self.color_blue_sb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.color_blue_sb.setDecimals(0)
        self.color_blue_sb.setMaximum(255.0)
        self.color_blue_sb.setProperty("value", 255.0)
        self.color_blue_sb.setObjectName("color_blue_sb")
        self.gridLayout.addWidget(self.color_blue_sb, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.hue_sb = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_2)
        self.hue_sb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.hue_sb.setDecimals(0)
        self.hue_sb.setMaximum(359.0)
        self.hue_sb.setObjectName("hue_sb")
        self.gridLayout.addWidget(self.hue_sb, 3, 0, 1, 1)
        self.color_green_sb = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_2)
        self.color_green_sb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.color_green_sb.setDecimals(0)
        self.color_green_sb.setMaximum(255.0)
        self.color_green_sb.setProperty("value", 255.0)
        self.color_green_sb.setObjectName("color_green_sb")
        self.gridLayout.addWidget(self.color_green_sb, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.color_red_sb = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_2)
        self.color_red_sb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.color_red_sb.setDecimals(0)
        self.color_red_sb.setMaximum(255.0)
        self.color_red_sb.setProperty("value", 255.0)
        self.color_red_sb.setObjectName("color_red_sb")
        self.gridLayout.addWidget(self.color_red_sb, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.reset_btn = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.reset_btn.setObjectName("reset_btn")
        self.horizontalLayout_5.addWidget(self.reset_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.line = QtWidgets.QFrame(self.dockWidgetContents_2)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_11 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.size_slider = QtWidgets.QSlider(self.dockWidgetContents_2)
        self.size_slider.setMinimum(10)
        self.size_slider.setMaximum(100)
        self.size_slider.setProperty("value", 30)
        self.size_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.size_slider.setObjectName("size_slider")
        self.gridLayout_2.addWidget(self.size_slider, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.reset_size_btn = QtWidgets.QToolButton(self.dockWidgetContents_2)
        self.reset_size_btn.setText("")
        self.reset_size_btn.setObjectName("reset_size_btn")
        self.gridLayout_2.addWidget(self.reset_size_btn, 0, 2, 1, 1)
        self.center_btn = QtWidgets.QToolButton(self.dockWidgetContents_2)
        self.center_btn.setText("")
        self.center_btn.setObjectName("center_btn")
        self.gridLayout_2.addWidget(self.center_btn, 0, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.measure_btn = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.measure_btn.setObjectName("measure_btn")
        self.horizontalLayout_2.addWidget(self.measure_btn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        self.horizontalLayout.addWidget(self.dockWidget_2)
        self.graphicsView = WhitepointView(white_point_editor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.graphicsView.setRenderHints(QtGui.QPainter.RenderHint.TextAntialiasing)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)

        self.retranslateUi(white_point_editor)
        QtCore.QMetaObject.connectSlotsByName(white_point_editor)

    def retranslateUi(self, white_point_editor):
        _translate = QtCore.QCoreApplication.translate
        white_point_editor.setWindowTitle(_translate("white_point_editor", "Form"))
        self.label_10.setText(_translate("white_point_editor", "Weißpunkt"))
        self.label_3.setText(_translate("white_point_editor", "Blau"))
        self.label_2.setText(_translate("white_point_editor", "Grün"))
        self.label.setText(_translate("white_point_editor", "Rot"))
        self.label_6.setText(_translate("white_point_editor", "Helligkeit"))
        self.label_4.setText(_translate("white_point_editor", "Farbton"))
        self.label_5.setText(_translate("white_point_editor", "Sättigung"))
        self.reset_btn.setText(_translate("white_point_editor", "Zurücksetzen"))
        self.label_11.setText(_translate("white_point_editor", "Messfenster"))
        self.label_7.setText(_translate("white_point_editor", "Größe"))
        self.measure_btn.setText(_translate("white_point_editor", "Messen"))
from src.views.whitepoint_view import WhitepointView
from src.widgets.color_circle import ColorCircle