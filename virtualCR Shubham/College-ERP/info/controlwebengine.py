from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView,QWebEnginePage
from webenginedemo import Ui_MainWindow
from PyQt5.QtCore import QUrl
import sys


class MainClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.widget.setHtml('<h2 align = "center">Welcome To PyQt5 WebEngine</h2>')
        #wep = QWebEnginePage
        #wp = wep.page('check.html')
        p = QWebEnginePage(5)
        p.page('check.html')

class Control:
    def __init__(self):
        pass
    def showMain(self):
        self.mc = MainClass()
        self.mc.show()


app = QApplication(sys.argv)
con = Control()
con.showMain()
sys.exit(app.exec_())




