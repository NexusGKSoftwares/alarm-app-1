import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.graphics import Color, Rectangle

kivy.require('2.0.0')  # Ensure we are using a compatible version of Kivy

class AlarmApp(App):

    def build(self):
        self.alarm_set = False  # Track if the alarm is set
        self.time_left = 0  # For countdown timer
        
        # Main layout with vertical alignment
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Set up background color (gradient)
        with self.layout.canvas.before:
            Color(0.0, 0.6, 0.8, 1)  # Light blue
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)
        self.layout.bind(size=self._update_rect, pos=self._update_rect)

        # Title
        self.title_label = Label(text='Set Your Alarm', font_size=40, color=(1, 1, 1, 1))
        self.layout.add_widget(self.title_label)

        # Timer Label
        self.timer_label = Label(text='Time left: 0', font_size=30, color=(1, 1, 1, 1))
        self.layout.add_widget(self.timer_label)

        # Countdown slider (for alarm time)
        self.slider = Slider(min=1, max=60, value=5, step=1)
        self.slider.bind(value=self.update_time)
        self.layout.add_widget(self.slider)

        # Label for slider value
        self.slider_label = Label(text=f'Set time: {int(self.slider.value)} seconds', font_size=24, color=(1, 1, 1, 1))
        self.layout.add_widget(self.slider_label)

        # Alarm Button
        self.set_alarm_button = Button(text='Set Alarm', font_size=28, background_normal='', background_color=(0.0, 0.8, 0.2, 1), color=(1, 1, 1, 1))
        self.set_alarm_button.bind(on_press=self.set_alarm)
        self.layout.add_widget(self.set_alarm_button)

        return self.layout

    def _update_rect(self, *args):
        """ Updates the background rectangle to match the layout size. """
        self.rect.pos = self.layout.pos
        self.rect.size = self.layout.size

    def update_time(self, instance, value):
        """ Update the slider value label. """
        self.slider_label.text = f'Set time: {int(value)} seconds'
        self.time_left = int(value)

    def set_alarm(self, instance):
        """ Set the alarm with a countdown timer. """
        if not self.alarm_set:
            self.alarm_set = True
            self.status_label = Label(text='Alarm set!', font_size=24, color=(1, 1, 1, 1))
            self.layout.add_widget(self.status_label)
            self.status_label.center = (self.layout.center_x, self.layout.center_y - 50)
            self.timer_label.text = f'Time left: {self.time_left} seconds'
            Clock.schedule_interval(self.update_timer, 1)  # Update the countdown every second
            self.set_alarm_button.text = 'Cancel Alarm'
        else:
            self.alarm_set = False
            self.timer_label.text = 'Time left: 0 seconds'
            self.set_alarm_button.text = 'Set Alarm'
            self.status_label.text = 'Alarm canceled'
            self.status_label.center = (self.layout.center_x, self.layout.center_y - 50)
            Clock.unschedule(self.update_timer)

    def update_timer(self, dt):
        """ Update the countdown timer. """
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.text = f'Time left: {self.time_left} seconds'
        else:
            self.trigger_alarm(None)
            Clock.unschedule(self.update_timer)

    def trigger_alarm(self, dt):
        """ Trigger the alarm popup when the time is up. """
        alarm_popup = Popup(title='Alarm!', content=Label(text='Time\'s up!', font_size=30, color=(0.8, 0, 0, 1)),
                            size_hint=(None, None), size=(400, 400), background_color=(1, 0.6, 0.6, 1))
        alarm_popup.open()
        self.alarm_set = False  # Reset the alarm status
        self.set_alarm_button.text = 'Set Alarm'
        self.timer_label.text = 'Time left: 0 seconds'


if __name__ == '__main__':
    AlarmApp().run()
