import GUI
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication([])
    window = GUI.MainWindow()
    window.show()
    sys.exit(app.exec_())