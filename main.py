import sys
import os
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import QTimer
from view import mainNote


class mainapp:
    def __init__(self):
        self.app = QApplication(sys.argv)


    def openmain(self):
        self.view = mainNote()
        self.view.show()

    def run(self):
        self.openmain()
        sys.exit(self.app.exec())


if __name__== "__main__" :
    opmain= mainapp()
    opmain.run()