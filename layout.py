from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        al = AnchorLayout()
        #bl= BoxLayout(orientation='vertical',size_hint=[.5,.5])
        bl = BoxLayout(orientation='vertical', size_hint=[None, None],size=[300,200])
        bl.add_widget( TextInput())
        bl.add_widget(TextInput())
        bl.add_widget(Button(text='Войти'))
        al.add_widget(bl)
        #for x in range(50):
        return al

        # gl=GridLayout(cols=3,padding=[30],spacing=5)
        #
        # for x in range(50):
        #     gl.add_widget( Button( text="Кнопка "+x.__str__()))
        #
        # return gl


        # bl=BoxLayout(orientation='horizontal',padding=[25],spacing=100)
        #
        # bl.add_widget( Button( text="Кнопка"))
        # bl.add_widget(Button(text="Кнопка2"))
        # bl.add_widget(Button(text="Кнопка3"))
        # return bl

#if __name__ == "__main1__":
MyApp().run()