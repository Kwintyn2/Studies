import sys
import os

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QPushButton, QVBoxLayout, QFileDialog, QHBoxLayout

from PyQt5.QtWidgets import QAction, qApp, QMainWindow

class Notepad(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text_area = QTextEdit()

        self.clear = QPushButton("Clear")
        self.open = QPushButton("Open")
        self.save = QPushButton("Save")

        h_box = QHBoxLayout()

        h_box.addWidget(self.clear)
        h_box.addWidget(self.open)
        h_box.addWidget(self.save)

        v_box = QVBoxLayout()
        v_box.addWidget(self.text_area)

        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.clear.clicked.connect(self.clear_text)
        self.open.clicked.connect(self.open_txt)
        self.save.clicked.connect(self.save_txt)

    def clear_text(self):
        self.text_area.clear()


    def open_txt(self):
        folder_name = QFileDialog.getOpenFileName(self, "Open Folder", os.getenv("HOME"))

        with open(folder_name[0], "r") as file:
            self.text_area.setText(file.read())



    def save_txt(self):
        folder_name = QFileDialog.getSaveFileName(self, "Save txt", os.getenv("HOME"))

        with open(folder_name[0], "w") as file:

            file.write(self.text_area.toPlainText())

class Menu(QMainWindow):

    def __init__(self):
        super().__init__()

        self.window_main = Notepad()
        self.setCentralWidget(self.window_main)

        menu_bar = self.menuBar()

        folder = menu_bar.addMenu("Folder")
        edit = menu_bar.addMenu("Edit")

        open_folder = QAction("Open Folder", self)
        open_folder.setShortcut("Ctrl+O")

        folder_save = QAction("Save Folder", self)
        folder_save.setShortcut("Ctrl+S")

        app_exit = QAction("Exit", self)
        app_exit.setShortcut("Ctrl+Q")

        folder.addAction(open_folder)
        folder.addAction(folder_save)
        folder.addAction(app_exit),

        clear = QAction("Clear", self)
        edit.addAction(clear)


        search_and_change = edit.addMenu("Search And Change")
        search = QAction("Search", self)
        change = QAction("Change", self)

        search_and_change.addAction(search)
        search_and_change.addAction(change)

        folder.triggered.connect(self.response)
        edit.triggered.connect(self.response)

        app_exit.triggered.connect(self.app_exit_def)
        self.setWindowTitle("Cutie Notepad")

        self.show()

    def app_exit_def(self):
        qApp.quit()

    def response(self, action):
        if action.text() == "Open Folder":
            self.window_main.open_txt()
            print("Clicked to 'Open Folder'")
        elif action.text() == "Save Folder":
            self.window_main.save_txt()
            print("Clicked to 'Save Folder'")
        elif action.text() == "Clear":
            self.window_main.clear_text()
            print("Clicked to 'Clear'")













app = QApplication(sys.argv)

notepad = Menu()

sys.exit(app.exec_())
