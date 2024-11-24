from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.switch import MDSwitch
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.uix.vibration import Vibration

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

        # Navigate to Settings Screen
        self.settings_button = MDRaisedButton(text='Settings', size_hint=(None, None), size=(200, 50))
        self.settings_button.pos_hint = {"center_x": 0.5, "center_y": 0.3}
        self.settings_button.bind(on_release=self.open_settings)
        self.add_widget(self.settings_button)

        self.alarm_time = None
        self.vibration_enabled = False
        self.sound_enabled = False
        self.sound = None

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
        if self.vibration_enabled:
            Vibration.vibrate()
        if self.sound_enabled and self.sound:
            self.sound.play()

    def open_settings(self, instance):
        self.manager.current = "settings"

# Settings Screen UI
class SettingsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Vibration Toggle
        self.vibration_switch = MDSwitch(active=False, size_hint=(None, None), size=(50, 50))
        self.vibration_switch.pos_hint = {"center_x": 0.5, "center_y": 0.7}
        self.vibration_switch.bind(active=self.toggle_vibration)
        self.add_widget(self.vibration_switch)

        # Sound Toggle
        self.sound_switch = MDSwitch(active=False, size_hint=(None, None), size=(50, 50))
        self.sound_switch.pos_hint = {"center_x": 0.5, "center_y": 0.6}
        self.sound_switch.bind(active=self.toggle_sound)
        self.add_widget(self.sound_switch)

        # Back Button
        self.back_button = MDRaisedButton(text='Back', size_hint=(None, None), size=(200, 50))
        self.back_button.pos_hint = {"center_x": 0.5, "center_y": 0.4}
        self.back_button.bind(on_release=self.go_back)
        self.add_widget(self.back_button)

        self.sound = SoundLoader.load("assets/alarm_sound.mp3")

    def toggle_vibration(self, instance, value):
        # Set the vibration preference
        app = MDApp.get_running_app()
        app.vibration_enabled = value

    def toggle_sound(self, instance, value):
        # Set the sound preference
        app = MDApp.get_running_app()
        app.sound_enabled = value

    def go_back(self, instance):
        self.manager.current = "main"


# Main App
class MyApp(MDApp):
    def build(self):
        self.screen_manager = Builder.load_string("""
ScreenManager:
    MainScreen:
        name: "main"
    SettingsScreen:
        name: "settings"
""")
        return self.screen_manager

    def on_start(self):
        # Initialize default values
        self.vibration_enabled = False
        self.sound_enabled = False


if __name__ == "__main__":
    MyApp().run()
