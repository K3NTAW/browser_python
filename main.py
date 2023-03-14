import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.browser = QWebEngineView()
    self.browser.setUrl(QUrl("https://duckduckgo.com/?kp=1"))    
    self.setCentralWidget(self.browser)
    self.showMaximized()

    #navbar
    navbar = QToolBar()
    self.addToolBar(navbar)

    #backbutton
    backbtn = QAction('◀', self)
    backbtn.triggered.connect(self.browser.back)
    navbar.addAction(backbtn)

    #forwardbutton
    forwardbtn = QAction(' ▶', self)
    forwardbtn.triggered.connect(self.browser.forward)
    navbar.addAction(forwardbtn)

    #reloadbutton
    reloadbtn = QAction("↻", self)
    reloadbtn.triggered.connect(self.browser.reload)
    navbar.addAction(reloadbtn)

    #homebutton
    homebtn = QAction("⌂", self)
    homebtn.triggered.connect(self.navigate_home)
    navbar.addAction(homebtn)

    #urlbar
    self.url_bar = QLineEdit(self)
    self.url_bar.returnPressed.connect(self.navigate_to_url)
    navbar.addWidget(self.url_bar)

    #urlupdate
    self.browser.urlChanged.connect(self.update_url)

  def navigate_home(self):
    self.browser.setUrl(QUrl("https://duckduckgo.com/?kp=1"))    

  def navigate_to_url(self):
    url = self.url_bar.text()
    self.browser.setUrl(QUrl(url))  

  def update_url(self, q):
    self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName("Kenta Browser")
window = MainWindow()
app.exec_()
