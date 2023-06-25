from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
import pygame

Window.size = (350, 580)

global screen

screen = ScreenManager()

class SplashScreen(Screen):
    pass

class Playlist(Screen):        
    pass 


screen.add_widget(SplashScreen(name='splash'))
screen.add_widget(Playlist(name='playlist'))


class Manoelgomes(MDApp):
    def build(self):
        kv = Builder.load_file("tela.kv")
        screen = kv
        return screen         
       
    def play_song(self):        
        self.sound = SoundLoader.load('manoel-gomes-caneta-azul.mp3')
        if self.sound:
            self.sound.play() 

if __name__ == "__main__":
    Manoelgomes().run()
