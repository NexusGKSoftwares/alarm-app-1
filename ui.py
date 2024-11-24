from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from alarm import AlarmHandler
from kivy.clock import Clock

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.alarm_handler = AlarmHandler()

        # Set up the layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Add icon
        icon = Image(source="assets/icon.png", size_hint=(None, None), size=(100, 100))
        layout.add_widget(icon)

        # Timer label
        self.timer_label = Label(text='Time left: 0', font_size=30)
        layout.add_widget(self.timer_label)

        # Slider for setting alarm time
        self.slider = Slider(min=1, max=60, value=5, step=1)
        self.slider.bind(value=self.update_time)
        layout.add_widget(self.slider)

        # Button to set the alarm
        self.set_alarm_button = MDRaisedButton(text='Set Alarm', size_hint=(None, None), size=(200, 50))
        self.set_alarm_button.bind(on_press=self.set_alarm)
        layout.add_widget(self.set_alarm_button)

        self.add_widget(layout)

    def update_time(self, instance, value):
        self.timer_label.text = f'Time left: {int(value)} seconds'

    def set_alarm(self, instance):
        if not self.alarm_handler.alarm_set:
            self.alarm_handler.set_alarm(int(self.slider.value))
            self.set_alarm_button.text = "Cancel Alarm"
        else:
            self.alarm_handler.cancel_alarm()
            self.set_alarm_button.text = "Set Alarm"

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Switch for enabling vibration
        self.vibration_switch = Switch(active=True)
        self.vibration_switch.bind(active=self.toggle_vibration)
        layout.add_widget(Label(text="Enable Vibration"))
        layout.add_widget(self.vibration_switch)

        # Button to go back to main screen
        self.back_button = MDRaisedButton(text="Back to Main", size_hint=(None, None), size=(200, 50))
        self.back_button.bind(on_press=self.go_back)
        layout.add_widget(self.back_button)

        self.add_widget(layout)

    def toggle_vibration(self, instance, value):
        # Handle vibration logic (placeholder for now)
        print(f"Vibration set to: {value}")

    def go_back(self, instance):
        self.manager.current = 'main'
