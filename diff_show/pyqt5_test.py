import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton)

def main():
    app = QApplication(sys.argv)
    a = QWidget()
    a.resize(250, 150)
    a.move(300, 300)
    a.setWindowTitle("title")
    a.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
