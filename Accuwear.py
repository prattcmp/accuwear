import sys
from accuweather import get_weather
from multiprocessing import Queue
from newsearch import get_tweets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
    
def window():
   app = QApplication(sys.argv)
   win = QWidget()
   
   image_url, weather_description, temperature = get_weather()
   tweets = get_tweets()
   
   sponsor = QLabel()
   sponsor.setPixmap(QPixmap(resource_path("images/accuweather.png")))
   sponsor.setFixedHeight(15)
   sponsor.setFixedWidth(78)
   sponsor.setScaledContents(True)
   
   image = QLabel()
   image.setPixmap(QPixmap(resource_path(image_url)))
   image.setScaledContents(True)
   description = QLabel(weather_description)
   description.setAlignment(Qt.AlignCenter)
   
   tempLabel = QLabel(str(temperature) + '° F')
   tempLabel.setAlignment(Qt.AlignCenter)
   progressBar = QProgressBar()
   progressBar.setValue(((temperature / 130.0) * 100))
   
   temperatureBox = QHBoxLayout()
   temperatureBox.addWidget(progressBar)
   temperatureBox.addWidget(tempLabel)
   
   tweet1 = QLabel(tweets[0])
   tweet2 = QLabel(tweets[1])
   tweet3 = QLabel(tweets[2])
   tweet4 = QLabel(tweets[3])
   
   groupBox = QGroupBox("AccuTweets")
   vbox = QVBoxLayout()
   vbox.addWidget(tweet1)
   vbox.addWidget(tweet2)
   vbox.addWidget(tweet3)
   vbox.addWidget(tweet4)
   groupBox.setLayout(vbox)
   
   vbox = QVBoxLayout()
   vbox.addWidget(sponsor)
   vbox.addWidget(image)
   vbox.addStretch()
   vbox.addWidget(description)
   vbox.addStretch()
   vbox.addLayout(temperatureBox)
   vbox.addWidget(groupBox)

   
   vbox.setAlignment(Qt.AlignCenter)
   win.setLayout(vbox)

   win.setWindowTitle("Accuwear")
   win.setFixedSize(500, 600)
   
   p = win.palette()
   p.setColor(win.backgroundRole(), Qt.white)
   win.setPalette(p)
   win.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()