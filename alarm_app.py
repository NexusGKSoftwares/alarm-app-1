import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.popup import Popup

kivy.require('2.0.0')  # Ensure we are using a compatible version of Kivy

class AlarmApp(App):

    def build(self):
        self.alarm_set = False  # Track if the alarm is set
        self.layout = BoxLayout(orientation='vertical')

        # Label to display alarm status
        self.status_label = Label(text='Alarm not set', font_size=24)
        self.layout.add_widget(self.status_label)

        # Button to set the alarm
        self.set_alarm_button = Button(text='Set Alarm', font_size=24)
        self.set_alarm_button.bind(on_press=self.set_alarm)
        self.layout.add_widget(self.set_alarm_button)

        return self.layout

    def set_alarm(self, instance):
        if not self.alarm_set:
            self.alarm_set = True
            self.status_label.text = 'Alarm set for 5 seconds from now.'
            Clock.schedule_once(self.trigger_alarm, 5)  # Trigger alarm after 5 seconds
        else:
            self.status_label.text = 'Alarm already set.'

    def trigger_alarm(self, dt):
        # This function is called when the alarm goes off
        alarm_popup = Popup(title='Alarm!', content=Label(text='Time\'s up!'), size_hint=(None, None), size=(400, 400))
        alarm_popup.open()
        self.alarm_set = False  # Reset the alarm status
        self.status_label.text = 'Alarm not set'

if __name__ == '__main__':
    AlarmApp().run()
