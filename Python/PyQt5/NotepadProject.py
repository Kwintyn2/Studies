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
        self.setWindowTitle("Cutie Notepad")
        self.show()
    def clear_text(self):
        self.text_area.clear()


    def open_txt(self):
        pass


    def save_txt(self):
        pass









app = QApplication(sys.argv)

notepad = Notepad()

sys.exit(app.exec_())
