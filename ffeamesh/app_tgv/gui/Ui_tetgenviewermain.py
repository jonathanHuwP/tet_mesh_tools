# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\resources\tetgenviewermain.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TetgenViewerMain(object):
    def setupUi(self, TetgenViewerMain):
        TetgenViewerMain.setObjectName("TetgenViewerMain")
        TetgenViewerMain.resize(844, 367)
        TetgenViewerMain.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(TetgenViewerMain)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self._tetViewer = TetViewer(self.groupBox)
        self._tetViewer.setObjectName("_tetViewer")
        self.verticalLayout_2.addWidget(self._tetViewer)
        self._controlsGroup = QtWidgets.QGroupBox(self.groupBox)
        self._controlsGroup.setEnabled(True)
        self._controlsGroup.setObjectName("_controlsGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self._controlsGroup)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self._showTetBox = QtWidgets.QCheckBox(self._controlsGroup)
        self._showTetBox.setCheckable(True)
        self._showTetBox.setChecked(True)
        self._showTetBox.setObjectName("_showTetBox")
        self.horizontalLayout_4.addWidget(self._showTetBox)
        self._surfaceButton = QtWidgets.QCheckBox(self._controlsGroup)
        self._surfaceButton.setEnabled(True)
        self._surfaceButton.setObjectName("_surfaceButton")
        self.horizontalLayout_4.addWidget(self._surfaceButton)
        self._surfaceLatticeButton = QtWidgets.QCheckBox(self._controlsGroup)
        self._surfaceLatticeButton.setEnabled(True)
        self._surfaceLatticeButton.setObjectName("_surfaceLatticeButton")
        self.horizontalLayout_4.addWidget(self._surfaceLatticeButton)
        self._thicknessBox = QtWidgets.QSpinBox(self._controlsGroup)
        self._thicknessBox.setEnabled(True)
        self._thicknessBox.setMinimum(1)
        self._thicknessBox.setMaximum(10)
        self._thicknessBox.setObjectName("_thicknessBox")
        self.horizontalLayout_4.addWidget(self._thicknessBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self._ctrTetButton = QtWidgets.QPushButton(self._controlsGroup)
        self._ctrTetButton.setEnabled(True)
        self._ctrTetButton.setObjectName("_ctrTetButton")
        self.horizontalLayout_3.addWidget(self._ctrTetButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self._ctrMeshButton = QtWidgets.QPushButton(self._controlsGroup)
        self._ctrMeshButton.setEnabled(True)
        self._ctrMeshButton.setObjectName("_ctrMeshButton")
        self.horizontalLayout_3.addWidget(self._ctrMeshButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self._controlsGroup)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self._rotXSlider = QtWidgets.QSlider(self._controlsGroup)
        self._rotXSlider.setEnabled(True)
        self._rotXSlider.setMaximum(360)
        self._rotXSlider.setProperty("value", 0)
        self._rotXSlider.setSliderPosition(0)
        self._rotXSlider.setOrientation(QtCore.Qt.Horizontal)
        self._rotXSlider.setObjectName("_rotXSlider")
        self.horizontalLayout.addWidget(self._rotXSlider)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self._controlsGroup)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self._rotYSlider = QtWidgets.QSlider(self._controlsGroup)
        self._rotYSlider.setEnabled(True)
        self._rotYSlider.setMaximum(360)
        self._rotYSlider.setOrientation(QtCore.Qt.Horizontal)
        self._rotYSlider.setObjectName("_rotYSlider")
        self.horizontalLayout_2.addWidget(self._rotYSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self._controlsGroup)
        self.verticalLayout_2.setStretch(0, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self._tetsTableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self._tetsTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self._tetsTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self._tetsTableWidget.setColumnCount(5)
        self._tetsTableWidget.setObjectName("_tetsTableWidget")
        self._tetsTableWidget.setRowCount(0)
        self._tetsTableWidget.horizontalHeader().setSortIndicatorShown(False)
        self._tetsTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout_4.addWidget(self._tetsTableWidget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self._totalVolLabel = QtWidgets.QLabel(self.groupBox_5)
        self._totalVolLabel.setObjectName("_totalVolLabel")
        self.horizontalLayout_6.addWidget(self._totalVolLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self._totalAreaLabel = QtWidgets.QLabel(self.groupBox_5)
        self._totalAreaLabel.setObjectName("_totalAreaLabel")
        self.horizontalLayout_7.addWidget(self._totalAreaLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_5.addWidget(self.groupBox_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.addWidget(self.splitter)
        TetgenViewerMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TetgenViewerMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        TetgenViewerMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TetgenViewerMain)
        self.statusbar.setObjectName("statusbar")
        TetgenViewerMain.setStatusBar(self.statusbar)
        self._actionLoad = QtWidgets.QAction(TetgenViewerMain)
        self._actionLoad.setObjectName("_actionLoad")
        self._actionExit = QtWidgets.QAction(TetgenViewerMain)
        self._actionExit.setObjectName("_actionExit")
        self._actionSaveImage = QtWidgets.QAction(TetgenViewerMain)
        self._actionSaveImage.setObjectName("_actionSaveImage")
        self._actionSaveTetData = QtWidgets.QAction(TetgenViewerMain)
        self._actionSaveTetData.setObjectName("_actionSaveTetData")
        self._actionSaveSetup = QtWidgets.QAction(TetgenViewerMain)
        self._actionSaveSetup.setObjectName("_actionSaveSetup")
        self._actionLoadSetup = QtWidgets.QAction(TetgenViewerMain)
        self._actionLoadSetup.setObjectName("_actionLoadSetup")
        self._actionPerspective = QtWidgets.QAction(TetgenViewerMain)
        self._actionPerspective.setObjectName("_actionPerspective")
        self._actionOrthogonal = QtWidgets.QAction(TetgenViewerMain)
        self._actionOrthogonal.setObjectName("_actionOrthogonal")
        self._actionBlackBackground = QtWidgets.QAction(TetgenViewerMain)
        self._actionBlackBackground.setObjectName("_actionBlackBackground")
        self._actionWhiteBackground = QtWidgets.QAction(TetgenViewerMain)
        self._actionWhiteBackground.setObjectName("_actionWhiteBackground")
        self._actionGrayBackground = QtWidgets.QAction(TetgenViewerMain)
        self._actionGrayBackground.setObjectName("_actionGrayBackground")
        self.menuFile.addAction(self._actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self._actionSaveImage)
        self.menuFile.addAction(self._actionSaveTetData)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self._actionSaveSetup)
        self.menuFile.addAction(self._actionLoadSetup)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self._actionExit)
        self.menuView.addAction(self._actionPerspective)
        self.menuView.addAction(self._actionOrthogonal)
        self.menuView.addSeparator()
        self.menuView.addAction(self._actionBlackBackground)
        self.menuView.addAction(self._actionWhiteBackground)
        self.menuView.addAction(self._actionGrayBackground)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(TetgenViewerMain)
        self._actionExit.triggered.connect(TetgenViewerMain.close) # type: ignore
        self._actionLoad.triggered.connect(TetgenViewerMain.get_and_load_files) # type: ignore
        self._rotXSlider.valueChanged['int'].connect(self._tetViewer.set_rot_x) # type: ignore
        self._rotYSlider.valueChanged['int'].connect(self._tetViewer.set_rot_y) # type: ignore
        self._tetsTableWidget.itemSelectionChanged.connect(TetgenViewerMain.selection_changed) # type: ignore
        self._actionSaveTetData.triggered.connect(TetgenViewerMain.save_tet_data) # type: ignore
        self._actionSaveImage.triggered.connect(TetgenViewerMain.save_image) # type: ignore
        self._ctrTetButton.clicked.connect(self._tetViewer.centre_tet) # type: ignore
        self._surfaceButton.toggled['bool'].connect(TetgenViewerMain.show_surface) # type: ignore
        self._surfaceLatticeButton.toggled['bool'].connect(TetgenViewerMain.show_surface_lattice) # type: ignore
        self._ctrMeshButton.clicked.connect(self._tetViewer.centre_mesh) # type: ignore
        self._thicknessBox.valueChanged['int'].connect(self._tetViewer.set_thickness) # type: ignore
        self._actionSaveSetup.triggered.connect(TetgenViewerMain.save_setup) # type: ignore
        self._actionLoadSetup.triggered.connect(TetgenViewerMain.load_setup) # type: ignore
        self._showTetBox.toggled['bool'].connect(self._tetViewer.show_current_tet) # type: ignore
        self._actionPerspective.triggered.connect(TetgenViewerMain.view_perspective) # type: ignore
        self._actionOrthogonal.triggered.connect(TetgenViewerMain.view_orthogonal) # type: ignore
        self._actionBlackBackground.triggered.connect(TetgenViewerMain.background_black) # type: ignore
        self._actionGrayBackground.triggered.connect(TetgenViewerMain.background_gray) # type: ignore
        self._actionWhiteBackground.triggered.connect(TetgenViewerMain.background_white) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(TetgenViewerMain)

    def retranslateUi(self, TetgenViewerMain):
        _translate = QtCore.QCoreApplication.translate
        TetgenViewerMain.setWindowTitle(_translate("TetgenViewerMain", "TetgenViewer"))
        self.groupBox.setTitle(_translate("TetgenViewerMain", "Tetrahedra View"))
        self._controlsGroup.setTitle(_translate("TetgenViewerMain", "View Controls"))
        self._showTetBox.setText(_translate("TetgenViewerMain", "Show Tet"))
        self._surfaceButton.setText(_translate("TetgenViewerMain", "Show surface"))
        self._surfaceLatticeButton.setText(_translate("TetgenViewerMain", "Surface Lattice"))
        self._ctrTetButton.setText(_translate("TetgenViewerMain", "Centre Tet"))
        self._ctrMeshButton.setText(_translate("TetgenViewerMain", "Centre Mesh"))
        self.label_2.setText(_translate("TetgenViewerMain", "Rot Horizontal"))
        self.label_3.setText(_translate("TetgenViewerMain", "Rot Vertical    "))
        self.groupBox_2.setTitle(_translate("TetgenViewerMain", "Tetrahedra Data"))
        self.groupBox_5.setTitle(_translate("TetgenViewerMain", "Mesh Properties"))
        self.label_5.setText(_translate("TetgenViewerMain", "Total volume (A^3)"))
        self._totalVolLabel.setText(_translate("TetgenViewerMain", "0.0"))
        self.label_7.setText(_translate("TetgenViewerMain", "Surface area (A^2)"))
        self._totalAreaLabel.setText(_translate("TetgenViewerMain", "0.0"))
        self.menuFile.setTitle(_translate("TetgenViewerMain", "File"))
        self.menuView.setTitle(_translate("TetgenViewerMain", "View"))
        self._actionLoad.setText(_translate("TetgenViewerMain", "Load"))
        self._actionExit.setText(_translate("TetgenViewerMain", "Exit"))
        self._actionSaveImage.setText(_translate("TetgenViewerMain", "Save image"))
        self._actionSaveTetData.setText(_translate("TetgenViewerMain", "Save tet data"))
        self._actionSaveSetup.setText(_translate("TetgenViewerMain", "Save setup"))
        self._actionLoadSetup.setText(_translate("TetgenViewerMain", "Load setup"))
        self._actionPerspective.setText(_translate("TetgenViewerMain", "Perspective"))
        self._actionOrthogonal.setText(_translate("TetgenViewerMain", "Orthogonal"))
        self._actionBlackBackground.setText(_translate("TetgenViewerMain", "Black background"))
        self._actionWhiteBackground.setText(_translate("TetgenViewerMain", "White background"))
        self._actionGrayBackground.setText(_translate("TetgenViewerMain", "Gray background"))
from ffeamesh.app_tgv.gui.tetviewer import TetViewer
