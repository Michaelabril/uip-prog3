
# import
import calendar
import time
import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.event import EventDispatcher
from kivy.uix.textinput import TextInput

# Constructor se utiliza para cargar todos los archivos Kivy que se carga en el archivo main.py

Builder.load_file('dates.kv')

# clase del archivo calender.kv
class Calender(BoxLayout):
    def __init__(self,**kwargs):
        super(Calender,self).__init__(**kwargs)
    def cambiarMes(self, meses):
        directo ={"Jan":1,"Feb":2,"Mar":3,"April":4,"May":5,"June":6,"July":7,"Aug":8,"Sept":9,"Oct":10,"Nov":11,"Dec":12}
        clave = directo[meses]
        print(clave)

# clase del archivo status.kv
class Status(BoxLayout,EventDispatcher):

    def __init__(self,**kwargs):
        super(Status,self).__init__(**kwargs)


# clase para Recordatorio de fechas
class Reminder(BoxLayout):
    def __init__(self,**kwargs):
        super(Reminder,self).__init__(**kwargs)

        self.orientation = 'vertical'
        self.add_widget(TextInput())
        self.b = BoxLayout(orientation = 'horizontal' , size_hint = (1,.15))
        self.add_widget(self.b)
        self.b.add_widget(Button(on_release = self.on_release,text = "OK!"))

    def on_release(self,event):
        print ("EVENTO AGREGADO!")

# ------------------------------------------------------------------------------------------------#

# clase de archivo dates.kv

class Dates(GridLayout):
    now = datetime.datetime.now()
    mes = int(  time.strftime("%m"))
    anno = int (time.strftime("%y"))

    def __init__ (self,**kwargs):#sirve para inicializar **kwargs
        super(Dates,self).__init__(**kwargs)
        self.cols = 7
        self.c  = calendar.monthcalendar(self.anno,self.mes)


#calendar.month Devuelve el calendario de un mes en una cadena de múltiples líneas usando el formatmonth ( ) de la clase TextCalendar .
        for i in self.c:
            for j in i:
                if j == 0:
                    self.add_widget(Button(id=self.id,on_release = self.on_release,text = '{j}'.format(j='')))
                else:
                    self.add_widget(Button(on_release = self.on_release, text = '{j}'.format(j=j)))




    def on_dismiss(self, arg):
        # Hacer algo en cierre de la ventana emergente
        pass

    def on_release(self,event):
        print ("FECHA " + event.text)
        event.background_color = 1,0,0,1
        self.popup = Popup(title= "Introducir evento :",
        content = Reminder(),
        size_hint=(None, None), size=(self.width*3/4, self.height))
        self.popup.bind(on_dismiss = self.on_dismiss)
        self.popup.open()


# ------------------------------------------------------------------------------------------------#

# class for months.kv file
class Months(BoxLayout):
    def __init__(self,**kwargs):
        super(Months,self).__init__(**kwargs)

# mainApp class
class mainApp(App):
    time = StringProperty()

    def update(self,*args):
        self.time = str(time.asctime())
    def build(self):
        self.title = "Calendario"
        self.load_kv('calender.kv')
        Clock.schedule_interval(self.update,1)
        return Calender()


#
if __name__ =='__main__':
    app = mainApp()
    app.run()