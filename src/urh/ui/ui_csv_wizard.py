

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_DialogCSVImport(object):
    def setupUi(self, DialogCSVImport):
        DialogCSVImport.setObjectName("DialogCSVImport")
        DialogCSVImport.resize(635, 674)
        self.gridLayout = QtWidgets.QGridLayout(DialogCSVImport)
        self.gridLayout.setObjectName("gridLayout")
        self.labelFileNotFound = QtWidgets.QLabel(DialogCSVImport)
        self.labelFileNotFound.setObjectName("labelFileNotFound")
        self.gridLayout.addWidget(self.labelFileNotFound, 1, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBoxCSVSeparator = QtWidgets.QComboBox(DialogCSVImport)
        self.comboBoxCSVSeparator.setObjectName("comboBoxCSVSeparator")
        self.comboBoxCSVSeparator.addItem("")
        self.comboBoxCSVSeparator.addItem("")
        self.horizontalLayout.addWidget(self.comboBoxCSVSeparator)
        self.btnAddSeparator = QtWidgets.QToolButton(DialogCSVImport)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("."), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddSeparator.setIcon(icon)
        self.btnAddSeparator.setIconSize(QtCore.QSize(16, 16))
        self.btnAddSeparator.setObjectName("btnAddSeparator")
        self.horizontalLayout.addWidget(self.btnAddSeparator)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 2, 1, 1)
        self.spinBoxTimestampColumn = QtWidgets.QSpinBox(DialogCSVImport)
        self.spinBoxTimestampColumn.setMaximum(999999999)
        self.spinBoxTimestampColumn.setObjectName("spinBoxTimestampColumn")
        self.gridLayout.addWidget(self.spinBoxTimestampColumn, 6, 2, 1, 1)
        self.label = QtWidgets.QLabel(DialogCSVImport)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 2)
        self.spinBoxQDataColumn = QtWidgets.QSpinBox(DialogCSVImport)
        self.spinBoxQDataColumn.setMaximum(999999999)
        self.spinBoxQDataColumn.setObjectName("spinBoxQDataColumn")
        self.gridLayout.addWidget(self.spinBoxQDataColumn, 5, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(DialogCSVImport)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(DialogCSVImport)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(DialogCSVImport)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidgetPreview = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidgetPreview.setAlternatingRowColors(True)
        self.tableWidgetPreview.setObjectName("tableWidgetPreview")
        self.tableWidgetPreview.setColumnCount(3)
        self.tableWidgetPreview.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPreview.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPreview.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPreview.setHorizontalHeaderItem(2, item)
        self.tableWidgetPreview.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetPreview.horizontalHeader().setStretchLastSection(False)
        self.tableWidgetPreview.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tableWidgetPreview)
        self.gridLayout.addWidget(self.groupBox, 7, 0, 1, 3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditFilename = QtWidgets.QLineEdit(DialogCSVImport)
        self.lineEditFilename.setObjectName("lineEditFilename")
        self.horizontalLayout_2.addWidget(self.lineEditFilename)
        self.btnChooseFile = QtWidgets.QToolButton(DialogCSVImport)
        self.btnChooseFile.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btnChooseFile.setObjectName("btnChooseFile")
        self.horizontalLayout_2.addWidget(self.btnChooseFile)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)
        self.spinBoxIDataColumn = QtWidgets.QSpinBox(DialogCSVImport)
        self.spinBoxIDataColumn.setMinimum(1)
        self.spinBoxIDataColumn.setMaximum(999999999)
        self.spinBoxIDataColumn.setProperty("value", 1)
        self.spinBoxIDataColumn.setObjectName("spinBoxIDataColumn")
        self.gridLayout.addWidget(self.spinBoxIDataColumn, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(DialogCSVImport)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogCSVImport)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 9, 2, 1, 1)
        self.groupBoxFilePreview = QtWidgets.QGroupBox(DialogCSVImport)
        self.groupBoxFilePreview.setObjectName("groupBoxFilePreview")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxFilePreview)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEditFilePreview = QtWidgets.QPlainTextEdit(self.groupBoxFilePreview)
        self.plainTextEditFilePreview.setUndoRedoEnabled(False)
        self.plainTextEditFilePreview.setReadOnly(True)
        self.plainTextEditFilePreview.setObjectName("plainTextEditFilePreview")
        self.verticalLayout.addWidget(self.plainTextEditFilePreview)
        self.gridLayout.addWidget(self.groupBoxFilePreview, 2, 0, 1, 3)
        self.label_5 = QtWidgets.QLabel(DialogCSVImport)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.btnAutoDefault = QtWidgets.QPushButton(DialogCSVImport)
        self.btnAutoDefault.setDefault(True)
        self.btnAutoDefault.setObjectName("btnAutoDefault")
        self.gridLayout.addWidget(self.btnAutoDefault, 10, 2, 1, 1)

        self.retranslateUi(DialogCSVImport)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogCSVImport.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogCSVImport.reject)
        DialogCSVImport.setTabOrder(self.lineEditFilename, self.btnChooseFile)
        DialogCSVImport.setTabOrder(self.btnChooseFile, self.plainTextEditFilePreview)
        DialogCSVImport.setTabOrder(self.plainTextEditFilePreview, self.comboBoxCSVSeparator)
        DialogCSVImport.setTabOrder(self.comboBoxCSVSeparator, self.btnAddSeparator)
        DialogCSVImport.setTabOrder(self.btnAddSeparator, self.spinBoxIDataColumn)
        DialogCSVImport.setTabOrder(self.spinBoxIDataColumn, self.spinBoxQDataColumn)
        DialogCSVImport.setTabOrder(self.spinBoxQDataColumn, self.spinBoxTimestampColumn)
        DialogCSVImport.setTabOrder(self.spinBoxTimestampColumn, self.tableWidgetPreview)

    def retranslateUi(self, DialogCSVImport):
        DialogCSVImport.setWindowTitle(QtWidgets.QApplication.translate("DialogCSVImport", "CSV Import", None, -1))
        self.labelFileNotFound.setText(QtWidgets.QApplication.translate("DialogCSVImport", "<html><head/><body><p><span style=\" color:#ff0000;\">Could not open the selected file.</span></p></body></html>", None, -1))
        self.comboBoxCSVSeparator.setItemText(0, QtWidgets.QApplication.translate("DialogCSVImport", ",", None, -1))
        self.comboBoxCSVSeparator.setItemText(1, QtWidgets.QApplication.translate("DialogCSVImport", ";", None, -1))
        self.btnAddSeparator.setToolTip(QtWidgets.QApplication.translate("DialogCSVImport", "Add a custom separator.", None, -1))
        self.btnAddSeparator.setText(QtWidgets.QApplication.translate("DialogCSVImport", "...", None, -1))
        self.spinBoxTimestampColumn.setToolTip(QtWidgets.QApplication.translate("DialogCSVImport", "<html><head/><body><p> If your dataset contains timestamps URH will calculate the sample rate from them. You can manually edit the sample rate after import in the signal details.</p></body></html>", None, -1))
        self.spinBoxTimestampColumn.setSpecialValueText(QtWidgets.QApplication.translate("DialogCSVImport", "Not present", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("DialogCSVImport", "I Data Column:", None, -1))
        self.spinBoxQDataColumn.setSpecialValueText(QtWidgets.QApplication.translate("DialogCSVImport", "Not present", None, -1))
        self.label_3.setToolTip(QtWidgets.QApplication.translate("DialogCSVImport", "<html><head/><body><p> If your dataset contains timestamps URH will calculate the sample rate from them. You can manually edit the sample rate after import in the signal details.</p></body></html>", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("DialogCSVImport", "Timestamp Column:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("DialogCSVImport", "Q Data Column:", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("DialogCSVImport", "Preview", None, -1))
        self.tableWidgetPreview.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("DialogCSVImport", "Timestamp", None, -1))
        self.tableWidgetPreview.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("DialogCSVImport", "I", None, -1))
        self.tableWidgetPreview.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("DialogCSVImport", "Q", None, -1))
        self.btnChooseFile.setText(QtWidgets.QApplication.translate("DialogCSVImport", "...", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("DialogCSVImport", "CSV Separator:", None, -1))
        self.groupBoxFilePreview.setTitle(QtWidgets.QApplication.translate("DialogCSVImport", "File Content (at most 100 rows)", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("DialogCSVImport", "File to import:", None, -1))
        self.btnAutoDefault.setText(QtWidgets.QApplication.translate("DialogCSVImport", "Prevent Dialog From Close with Enter", None, -1))

