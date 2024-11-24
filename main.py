from kivy.lang import Builder
from kivy.uix.switch import Switch  # Using Kivy's native Switch instead of MDSwitch
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.uix.slider import Slider
from kivy.clock import Clock

# Your app class
class AlarmApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        
        # Creating the main screen layout
        screen = MDScreen()
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        
        # Add title label
        title_label = MDLabel(
            text="Alarm App", theme_text_color="Secondary", halign="center", font_style="H5"
        )
        layout.add_widget(title_label)
        
        # Add switch for vibration and sound control
        self.switch_layout = BoxLayout(size_hint_y=None, height=50, orientation="horizontal")
        
        self.vibration_switch = Switch(active=True)
        self.vibration_switch.bind(active=self.on_vibration_switch_active)
        
        self.sound_switch = Switch(active=True)
        self.sound_switch.bind(active=self.on_sound_switch_active)
        
        self.switch_layout.add_widget(MDLabel(text="Vibration", theme_text_color="Secondary"))
        self.switch_layout.add_widget(self.vibration_switch)
        
        self.switch_layout.add_widget(MDLabel(text="Sound", theme_text_color="Secondary"))
        self.switch_layout.add_widget(self.sound_switch)
        
        layout.add_widget(self.switch_layout)

        # Add countdown button
        self.countdown_button = MDRaisedButton(
            text="Start Countdown", size_hint=(None, None), size=("200dp", "50dp")
        )
        self.countdown_button.bind(on_press=self.start_countdown)
        layout.add_widget(self.countdown_button)

        # Add countdown label
        self.countdown_label = MDLabel(text="Time Left: 00:00", halign="center", font_style="H6")
        layout.add_widget(self.countdown_label)

        # Add slider for timer
        self.timer_slider = Slider(min=0, max=60, value=10, step=1)
        self.timer_slider.bind(value=self.update_timer)
        layout.add_widget(self.timer_slider)

        # Add the layout to the screen
        screen.add_widget(layout)

        return screen

    def on_vibration_switch_active(self, instance, value):
        # Handle vibration toggle
        if value:
            print("Vibration is enabled.")
        else:
            print("Vibration is disabled.")

    def on_sound_switch_active(self, instance, value):
        # Handle sound toggle
        if value:
            print("Sound is enabled.")
        else:
            print("Sound is disabled.")

    def start_countdown(self, instance):
        # Start countdown when button is pressed
        self.time_left = self.timer_slider.value
        self.update_timer_label()
        self.alarm_sound = SoundLoader.load("alarm_sound.mp3")  # Example sound file
        if self.alarm_sound:
            self.alarm_sound.loop = True
        Clock.schedule_interval(self.countdown, 1)

    def countdown(self, dt):
        # Countdown logic
        if self.time_left > 0:
            self.time_left -= 1
            self.update_timer_label()
        else:
            self.trigger_alarm()

    def update_timer_label(self):
        minutes = int(self.time_left) // 60
        seconds = int(self.time_left) % 60
        self.countdown_label.text = f"Time Left: {minutes:02}:{seconds:02}"

    def update_timer(self, instance, value):
        # Update timer based on slider value
        self.time_left = value
        self.update_timer_label()

    def trigger_alarm(self):
        # Trigger alarm when countdown reaches zero
        if self.alarm_sound:
            self.alarm_sound.play()
        print("Time's up!")

# Run the app
if __name__ == "__main__":
    AlarmApp().run()
