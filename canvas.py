from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from  kivy.core.window import Window
from random import random

from  kivy.graphics import (Color, Ellipse,Rectangle,Line)

class PainterWidget(Widget):
    # def __init__(self,**kwargs):
    #     super(PainterWidget,self).__init__(**kwargs)

    def on_touch_down(self, touch):
        with self.canvas:
            Color(random(),random(),random(),1)
            #Ellipse(pos=(100,100),size=(50,50))
            #Line(points=(300,300,350,400,400,300),close=True,width=5)
            #self.line=Line(points=(),width=10,joint='miter')
            rad=30
            Ellipse(pos=(touch.x - rad/2,touch.y - rad/2),size=(rad,rad))
            touch.ud['line']= Line(points=(touch.x,touch.y),width=15)
    # def on_touch_down(self, touch):
    #     print('Touch_down')
    #     self.line.points+=(touch.x,touch.y)
    def on_touch_move(self, touch):
        touch.ud['line'].points+=(touch.x,touch.y)

class PaintApp(App):
    def build(self):
        parent=Widget()
        self.parent=PainterWidget()
        parent.add_widget(self.parent)

        parent.add_widget(Button(text='Clear', on_press=self.clear_canvas,
                                 size=(100,50)))
        parent.add_widget(Button(text='Save', on_press=self.save,
                                 size=(100, 50),pos=(100,0)))

        return  parent
        # return PainterWidget()
    def clear_canvas(self,instance):
        self.parent.canvas.clear()

    def save(self,instance):
        self.parent.size=(Window.size[0],Window.size[1])
        self.parent.export_to_png('image.png')

PaintApp().run()