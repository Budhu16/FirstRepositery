from PyQt5.QtWidgets import QApplication, QMainWindow
from mymain import Ui_mainscreen
import sys
from GOOGLE import Ui_googlescreen
from news import Ui_newswindow
from weather import Ui_WeatherWindow
from PyQt5 import QtCore
from quora import Ui_QuoraWindow
from apple import Ui_applewindow
from flipkartui import Ui_flipwindow
from gmailui import Ui_gmailwindow
from youtubeui import Ui_youtubewindow

class AppleClass(QMainWindow):
     def goback(self):
        self.mc = MainClass()
        self.mc.show()
        self.hide()
        
     def __init__(self):
         super().__init__()
         self.ui=Ui_applewindow()
         self.ui.setupUi(self)
         self.ui.widget.load(QtCore.QUrl('https://www.apple.com/'))
         self.ui.actionExit_2.triggered.connect(self.exitwindow)
         self.ui.actionGO_BACK.triggered.connect(self.goback)
         
     def exitwindow(self):
         self.destroy()
        
class QuoraClass(QMainWindow):
     def goback(self):
        self.mc = MainClass()
        self.mc.show()
        self.hide()
        
     def __init__(self):
         super().__init__()
         self.ui = Ui_QuoraWindow()
         self.ui.setupUi(self)
         self.ui.widget.load(QtCore.QUrl('https://www.quora.com/'))
         self.ui.actionExit.triggered.connect(self.exitwindow)
         self.ui.actionGO_BACK.triggered.connect(self.goback)
         
     def exitwindow(self):
         self.destroy()

class WeatherClass(QMainWindow):
    def goback(self):
        self.mc = MainClass()
        self.mc.show()
        self.hide()
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_WeatherWindow()
        self.ui.setupUi(self)
        self.ui.widget.load(QtCore.QUrl('https://www.ventusky.com/'))
        self.ui.actionExit.triggered.connect(self.exitwindow)
        self.ui.actionGO_BACK.triggered.connect(self.goback)
         
    def exitwindow(self):
        self.destroy()

class YoutubeClass(QMainWindow):
    def goback(self):
        self.mc = MainClass()
        self.mc.show()
        self.hide()
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_youtubewindow()
        self.ui.setupUi(self)
        self.ui.widget.load(QtCore.QUrl('https://www.youtube.com/'))
        self.ui.actionExit.triggered.connect(self.exitwindow)
        self.ui.actionGO_BACK.triggered.connect(self.goback)
         
    def exitwindow(self):
        self.destroy()
     
class NewsClass(QMainWindow):
    def goback(self):
        self.mc = MainClass()
        self.mc.show()
        self.hide()
        
    def __init__(self):
        print('started')
        super().__init__()
        self.ui = Ui_newswindow()
        self.ui.setupUi(self)
        self.ui.actionEXIT.triggered.connect(self.exitwindow)
        self.ui.actionGO_BACK.triggered.connect(self.goback)
        from newsapi import NewsApiClient
        nac = NewsApiClient(api_key = 'f4610dba7eea4338a943ebe88b6258cd')
        print('Started...')
        topheadlines = nac.get_top_headlines(language = 'en', country = 'in')
        self.nameslist = []
        self.authorslist = []
        self.titleslist = []
        self.descriptions = []
        self.totalnews = len(topheadlines['articles'])
        for i in range(len(topheadlines['articles'])):
            self.nameslist.append(topheadlines['articles'][i]['source']['name'])
            self.authorslist.append(topheadlines['articles'][i]['author'])
            self.titleslist.append(topheadlines['articles'][i]['title'])
            self.descriptions.append(topheadlines['articles'][i]['description'])
        self.ui.postname.setText(self.nameslist[0])
        self.ui.postauthor.setText(self.authorslist[0])
        self.ui.title.setText(self.titleslist[0])
        self.ui.textEdit.setText(self.descriptions[0])
        self.currcount = 0
        self.ui.pushButton_2.clicked.connect(self.gonext)
        self.ui.pushButton.clicked.connect(self.goprev)
        #self.ui.actionGO_BACK.triggered.connect(self.goback)

    def gonext(self):
        self.currcount += 1
        self.ui.postname.setText(self.nameslist[self.currcount])
        self.ui.postauthor.setText(self.authorslist[self.currcount])
        self.ui.title.setText(self.titleslist[self.currcount])
        self.ui.textEdit.setText(self.descriptions[self.currcount])

    def goprev(self):
        self.currcount -= 1
        self.ui.postname.setText(self.nameslist[self.currcount])
        self.ui.postauthor.setText(self.authorslist[self.currcount])
        self.ui.title.setText(self.titleslist[self.currcount])
        self.ui.textEdit.setText(self.descriptions[self.currcount])

    def exitwindow(self):
        self.destroy()
        
class GoogleClass(QMainWindow):
    def goback(self):
        self.mc = MainClass()
        self.mc.show()
        self.hide()
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_googlescreen()
        self.ui.setupUi(self)
        self.ui.actionExit_2.triggered.connect(self.exitwindow)
        self.ui.pushButton.clicked.connect(self.showmygoogle)
        self.ui.actionGO_BACK.triggered.connect(self.goback)

    def showmygoogle(self):
        import speech_recognition as sr
        rec = sr.Recognizer()
        self.ui.statusBar.showMessage('Speak...')
        with sr.Microphone() as source:
            audio = rec.listen(source, phrase_time_limit = 5)
        self.ui.statusBar.showMessage('Processing Your Command...')
        try:
            text = rec.recognize_google(audio)
        except sr.RequestError:
            self.ui.statusBar.showMessage('Could\'nt Connect To The Internet! Check Your Network Settings.')
        except sr.UnknownValueError:
            self.ui.statusBar.showMessage('Could\'nt Understand What You Said... Please Click And Speak Again!')
        else:
            import webbrowser
            query = text.split(' ',1)[1]
            webbrowser.open(f'https://www.google.com/search?source=hp&ei=N2VWXbifMduSwgPLma3YAg&q={query}')
        
         
    def exitwindow(self):
        self.destroy()

class FlipkartClass(QMainWindow):
    def goback(self):
        self.mc = MainClass()
        self.mc.show()
        self.hide()
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_flipwindow()
        self.ui.setupUi(self)
        self.ui.widget.load(QtCore.QUrl('https://www.flipkart.com/'))
        self.ui.actionExit.triggered.connect(self.exitwindow)
        self.ui.actionGO_BACK.triggered.connect(self.goback)
         
    def exitwindow(self):
        self.destroy()

class GmailClass(QMainWindow):
    def goback(self):
        self.mc = MainClass()
        self.mc.show()
        self.hide()
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_gmailwindow()
        self.ui.setupUi(self)
        self.ui.widget.load(QtCore.QUrl('https://www.gmail.com/'))
        self.ui.actionExit.triggered.connect(self.exitwindow)
        self.ui.actionGO_BACK.triggered.connect(self.goback)
         
    def exitwindow(self):
        self.destroy()

class MainClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainscreen()
        self.ui.setupUi(self)
        from datetime import datetime
        x = datetime.now()
        d = x.date()
        t = x.time()
        #print(d,t)
        t1 = str(t).rsplit('.',1)[0]
        self.ui.label.setText(str(d).center(15))
        self.ui.label_2.setText(t1.center(15))
        self.ui.presstospeak.clicked.connect(self.fetchcommand)
        self.ui.weatherbtn.clicked.connect(self.showweather)
        self.ui.news.clicked.connect(self.shownews)
        self.ui.quora.clicked.connect(self.showquora)
        self.ui.google.clicked.connect(self.showgoogle)
        self.ui.applebtn.clicked.connect(self.showapple)
        self.ui.flipkart.clicked.connect(self.showflipkart)
        self.ui.gmail.clicked.connect(self.showgmail)
        self.ui.youtube.clicked.connect(self.showyoutube)
        self.ui.exitbutton.clicked.connect(self.exitwindow)

    def exitwindow(self):
        self.destroy()

    def gotomain(self):
        pass

    def showyoutube(self):
        self.yc = YoutubeClass()
        self.yc.show()
        self.hide()

    def showflipkart(self):
        self.fc = FlipkartClass()
        self.fc.show()
        self.hide()

    def showgmail(self):
        self.gc = GmailClass()
        self.gc.show()
        self.hide()

    def showapple(self):
        self.ac = AppleClass()
        self.ac.show()
        self.hide()
        
    def showgoogle(self):
        self.gc = GoogleClass()
        self.gc.show()
        self.hide()

    def showquora(self):
        self.qc = QuoraClass()
        self.qc.show()
        self.hide()

    def shownews(self):
        self.nc = NewsClass()
        self.nc.show()
        self.hide()
        
    def showweather(self):
        self.wc = WeatherClass()
        self.wc.show()
        self.hide()

    def fetchcommand(self):
        import speech_recognition as sr
        rec = sr.Recognizer()
        self.ui.statusBar.showMessage('Speak...')
        with sr.Microphone() as source:
            audio = rec.listen(source, phrase_time_limit = 5)
        self.ui.statusBar.showMessage('Processing Your Command...')
        try:
            text = rec.recognize_google(audio)
        except sr.RequestError:
            self.ui.statusBar.showMessage('Could\'nt Connect To The Internet! Check Your Network Settings.')
        except sr.UnknownValueError:
            self.ui.statusBar.showMessage('Could\'nt Understand What You Said... Please Click And Speak Again!')
        else:
            if text == 'open google':
                self.showgoogle()
            elif text == 'read news':
                self.shownews()
            elif text == 'open apple' or text == 'open apple.com':
                self.showapple()
            elif text == 'check weather' or text == 'weather report':
                self.showweather()
            elif text == 'open flipkart' or text == 'open flipkart.com':
                self.showflipkart()
            elif text == 'open gmail':
                self.showgmail()
            elif text == 'open quora':
                self.showqoura()
            elif text == 'open youtube':
                self.showyoutube()
           

class Controller:
    def __init__(self):
        pass

    def showMain(self):
        self.MC = MainClass()
        self.MC.show()

def main():
    app = QApplication(sys.argv)
    con = Controller()
    con.showMain()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()











