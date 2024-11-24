import pygame
from kivy.clock import Clock

class AlarmHandler:
    def __init__(self):
        self.alarm_set = False
        self.time_left = 0
        self.alarm_sound = "assets/alarm_sound.mp3"  # Path to your alarm sound

    def init_alarm(self):
        pygame.mixer.init()  # Initialize pygame mixer for sound

    def set_alarm(self, time_left):
        self.time_left = time_left
        self.alarm_set = True
        Clock.schedule_interval(self.update_timer, 1)

    def cancel_alarm(self):
        self.alarm_set = False
        Clock.unschedule(self.update_timer)

    def update_timer(self, dt):
        if self.time_left > 0:
            self.time_left -= 1
        else:
            self.trigger_alarm()
            Clock.unschedule(self.update_timer)

    def trigger_alarm(self):
        pygame.mixer.music.load(self.alarm_sound)
        pygame.mixer.music.play()  # Play alarm sound
        self.alarm_set = False

