from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config




Config.set('graphics','resizable',True)





class LoginUI(App):

    def build(self):


        Layout = RelativeLayout()


        Layout.add_widget(Label(text='Username',
                                size_hint=(.2,.06),
                                pos_hint={'center_x':.32,'center_y':.55}))
        username = TextInput(multiline=False,
                           size_hint=(.2,.06),
                           font_size=16,
                           pos_hint={'center_x':.6,'center_y':.55})
        Layout.add_widget(username)


        Layout.add_widget(Label(text='Password',
                                size_hint=(.2,.06),
                                pos_hint={'center_x':.32,'center_y':.4}))
        password = TextInput(password=True,multiline=False,
                             size_hint=(.2,.06),
                             font_size=16,
                             pos_hint={'center_x':.6,'center_y':.4})
        Layout.add_widget(password)
        


        


        Layout.add_widget(Button(text='Login',
                                 size_hint=(.2,.06),
                                 pos_hint={'center_x':.5,'center_y':.3}))
        return Layout

if __name__=='__main__':
    LoginUI().run()

    



        



