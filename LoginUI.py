from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput



class LoginUI(GridLayout):

    def __init__(self, **kwargs):
        super(LoginUI,self).__init__(**kwargs)
       
        self.cols = 2
        self.add_widget(Label(text='User Name',size_hint= (None, None),height= 15))
        self.username = TextInput(multiline=False,size_hint= (None, None),height= 15)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password',size_hint= (None, None),height= 15))
        self.password = TextInput(password=True, multiline=False,size_hint= (None, None),height= 15)
        self.add_widget(self.password)

class MyApp(App):

    def build(self):
        return LoginUI()



if __name__=='__main__':

    MyApp().run()

    
        
