from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivy.uix.image import Image
import time


# Main Screen UI
class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Set an icon at the top of the screen
        self.icon_image = Image(source="assets/icon.png", size_hint=(None, None), size=(100, 100))
        self.icon_image.pos_hint = {"center_x": 0.5, "center_y": 0.9}
        self.add_widget(self.icon_image)

        # Add a countdown label
        self.countdown_label = MDLabel(text="00:00", halign="center", theme_text_color="Secondary")
        self.countdown_label.pos_hint = {"center_x": 0.5, "center_y": 0.7}
        self.add_widget(self.countdown_label)

        # Set Alarm Button
        self.set_alarm_button = MDRaisedButton(text='Set Alarm', size_hint=(None, None), size=(200, 50))
        self.set_alarm_button.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.set_alarm_button.bind(on_release=self.set_alarm)
        self.add_widget(self.set_alarm_button)

    def set_alarm(self, instance):
        # Start the countdown for the alarm (example: 5 minutes)
        self.alarm_time = 5 * 60  # 5 minutes in seconds
        Clock.schedule_interval(self.update_countdown, 1)

    def update_countdown(self, dt):
        if self.alarm_time > 0:
            mins, secs = divmod(self.alarm_time, 60)
            self.countdown_label.text = f"{mins:02d}:{secs:02d}"
            self.alarm_time -= 1
        else:
            Clock.unschedule(self.update_countdown)
            self.trigger_alarm()

    def trigger_alarm(self):
        # Trigger the alarm sound (you can add a custom sound file)
        print("ALARM TRIGGERED!")  # Replace this with actual alarm sound or vibration logic


# Main App
class MyApp(MDApp):
    def build(self):
        self.screen = MainScreen()
        return self.screen


if __name__ == "__main__":
    MyApp().run()
