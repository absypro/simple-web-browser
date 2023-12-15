



from PyQt5 import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui , QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *



class my_web_browser(QMainWindow):

    def __init__(self):
        #        super(my_web_browser, self).__init__(*args, **kwargs)

        self.window = QWidget()
        self.window.setWindowTitle("absy web browser")
        self.window.setStyleSheet("background:  #161219 ;")
        self.window.setFixedWidth(1000)

        # layout ###############################################

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

#       here the url bar
        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)
        self.url_bar.setStyleSheet("border: 5px  solid  '#BC006C' ; " +" border-radius: 30px ;"  + "color: 'white'  ;")



        #  here we define the Go button
        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)
        self.go_btn.setStyleSheet("border: 25px  solid  '#BC006C' ; " + " border-radius: 30px ;" + "font-size: 30px;" + "color: 'white'  ;")

        # here we define back button
        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)
        self.back_btn.setStyleSheet("border: 25px  solid  '#BC006C' ; " + " border-radius: 30px ;" + "font-size: 30px;" + "color: 'white'  ;")


        # here we define forword button
        self.forword_btn = QPushButton(">")
        self.forword_btn.setMinimumHeight(30)
        self.forword_btn.setStyleSheet("border: 25px  solid  '#BC006C' ; " + " border-radius: 30px ;" + "font-size: 30px;" + "color: 'white'  ;")

#   here we place them in our window horizontal
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forword_btn)


        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))

        self.back_btn.clicked.connect(self.browser.back)

        self.forword_btn.clicked.connect(self.browser.forward)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://localhost"))

        self.window.setLayout(self.layout)
        self.window.show()


    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url + ".com"

            self.url_bar.setText(url)

        self.browser.setUrl(QUrl(url))


app = QApplication([])
window = my_web_browser()

app.exec_()


