from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from ui import MainScreen, SettingsScreen
from alarm import AlarmHandler

class MyApp(App):

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(SettingsScreen(name='settings'))
        return self.sm

if __name__ == '__main__':
    AlarmHandler().init_alarm()  # Initialize alarm logic
    MyApp().run()
