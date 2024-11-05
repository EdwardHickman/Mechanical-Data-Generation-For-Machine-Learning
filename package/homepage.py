import os
import threading
import time
import webbrowser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QColor, QDesktopServices
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QUrl

from package import selenium_utils
from package import select
from package import extra


def open_excel():
    os.startfile("message.xlsx")


class Ui_main_window(QMainWindow):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(800, 100)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        main_window.setFont(font)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")

        # the place where you type
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 40, 223, 20))
        self.lineEdit.setObjectName("lineEdit")
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.lineEdit.setFont(font)

        # loading label
        # TODO: ask to remove or turn it into a loading symbol or meter
        # self.loading = QtWidgets.QLabel(self.centralwidget)
        # self.loading.setGeometry(QtCore.QRect(30, 100, 271, 31))
        # font = QtGui.QFont()
        # font.setFamily("Open Sans")
        # font.setPointSize(16)
        # self.loading.setFont(font)
        # self.loading.setObjectName("loading")

        # the area where the graph is displayed
        # self.graph = QtWidgets.QLabel(self.centralwidget)
        # self.graph.setGeometry(QtCore.QRect(10, 190, 501, 341))
        # self.graph.setText("")
        # # self.graph.setPixmap(QtGui.QPixmap("../../../Downloads/stress_strain_demo_example.png"))
        # self.graph.setScaledContents(True)
        # self.graph.setObjectName("graph")

        # the link where the image came from
        # TODO: ask the group if we could scrap this or give it actual functionality i guess, celeste said do this
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setGeometry(QtCore.QRect(10, 530, 441, 16))
        # font = QtGui.QFont()
        # font.setFamily("Open Sans")
        # font.setPointSize(10)
        # self.label_2.setFont(font)
        # self.label_2.setObjectName("label_2")
        #
        # # was this helpful?
        # self.helpful = QtWidgets.QLabel(self.centralwidget)
        # self.helpful.setGeometry(QtCore.QRect(530, 210, 171, 21))
        # font = QtGui.QFont()
        # font.setFamily("Open Sans")
        # font.setPointSize(12)
        # self.helpful.setFont(font)
        # self.helpful.setObjectName("helpful")

        # yes
        # TODO: clicking this button runs wasif and eddie's part
        # TODO: add an icon instead of "yes", celeste said dont do this
        # self.yes_button = QtWidgets.QPushButton(self.centralwidget)
        # self.yes_button.setGeometry(QtCore.QRect(540, 260, 75, 23))
        # font = QtGui.QFont()
        # font.setFamily("Open Sans")
        # self.yes_button.setFont(font)
        # self.yes_button.setObjectName("yes_button")

        # no
        # TODO: clicking no generates a new image and the process restarts
        # TODO: add an icon instead of "no", celeste said dont do this
        # self.no_button = QtWidgets.QPushButton(self.centralwidget)
        # self.no_button.setGeometry(QtCore.QRect(540, 310, 75, 23))
        # font = QtGui.QFont()
        # font.setFamily("Open Sans")
        # self.no_button.setFont(font)
        # self.no_button.setObjectName("no_button")

        # ??? idk what this does
        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        # search/go button that starts scraper
        self.go_button = QtWidgets.QPushButton(self.centralwidget)
        self.go_button.setGeometry(QtCore.QRect(265, 39, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.go_button.setFont(font)
        self.go_button.setObjectName("pushButton_4")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.go_button.setIcon(icon)

        # self.go_button.clicked.connect(lambda: selenium_utils.get_images(2, 10, self.lineEdit.text()))
        # self.lineEdit.returnPressed.connect(lambda: selenium_utils.get_images(2, 10, self.lineEdit.text()))
        self.go_button.clicked.connect(self.go_button_action)
        self.lineEdit.returnPressed.connect(self.go_button_action)

        #TODO: call the method below instead of running these above lines

        # Add a help button cb-7-1001
        self.helpButton = QtWidgets.QPushButton(self.centralwidget)
        self.helpButton.setObjectName("helpButton")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/white-help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpButton.setIcon(icon)
        self.helpButton.setIconSize(QtCore.QSize(25, 25))
        self.helpButton.setGeometry(QtCore.QRect(730, 20, 25, 25))
        self.helpButton.clicked.connect(self.open_link)

        # calles the function that changes titles and labels
        self.retranslateUi(main_window)

        # calls the function that changes the window to dark mode
        self.set_dark_mode(main_window)

        # ???
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Stress-Strain Tool"))
        self.lineEdit.setPlaceholderText(_translate("main_window", "Enter a Material Name Here"))
        # self.loading.setText(_translate("main_window", ""))
        # self.label_2.setText(_translate("main_window", "Image based on: https://www.mdpi.com/1996-1944/11/4/513/htm"))
        # self.helpful.setText(_translate("main_window", "Was this helpful?"))
        # self.yes_button.setText(_translate("main_window", "Yes"))
        # self.no_button.setText(_translate("main_window", "No"))
        # self.go_button.setText(_translate("main_window", "GO"))
        # self.loading.setHidden(False)
        # self.results.setHidden(True)
        # self.label_2.setHidden(True)
        # self.yes_button.setHidden(True)
        # self.no_button.setHidden(True)
        # self.graph.setHidden(True)
        # self.pushButton.setHidden(True)
        # self.helpful.setHidden(True)

    def set_dark_mode(self, main_window):
        # set the dark color palette
        palette = QPalette()
        palette.setColor(palette.Window, Qt.black)
        palette.setColor(palette.WindowText, Qt.white)
        palette.setColor(palette.Base, Qt.darkGray)
        palette.setColor(palette.AlternateBase, Qt.gray)
        palette.setColor(palette.ToolTipBase, Qt.white)
        palette.setColor(palette.ToolTipText, Qt.white)
        palette.setColor(palette.Text, Qt.white)
        palette.setColor(palette.Button, Qt.darkGray)
        palette.setColor(palette.ButtonText, Qt.white)
        palette.setColor(palette.BrightText, Qt.red)
        self.setPalette(palette)
        main_window.setPalette(palette)
        # Set the dark style sheet.
        style_sheet = (
            """
                QWidget {
                    background-color: #222;
                    color: #fff;
                }
                QPushButton {
                    background-color: #555;
                    color: #fff;
                    border: 1px solid #333;
                    border-radius: 3px;
                    padding: 5px;
                }
                QPushButton:hover {
                    background-color: #777;
                }
                QPushButton:pressed {
                    background-color: #999;
                }"""
        )
        self.setStyleSheet(style_sheet)
        main_window.setStyleSheet(style_sheet)

    def go_button_action(self):
        selenium_utils.get_images(2, 10, self.lineEdit.text())
        self.MainWindow = QtWidgets.QMainWindow()
        extra.parse_xlsx("points", "output_csv", "output_png")
        select.selection_screen(self, self.MainWindow)
        self.MainWindow.show()
        #time.sleep(10)

    def open_link(self):
        # Open the link
        # url = QUrl("https://github.com/Wasif24/Squidstone33")
        # QDesktopServices.openUrl(url)
        os.startfile("README_capstone.txt")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
